"""Read public Hugging Face safetensors HEADER ONLY; no model weights executed.

The header describes tensor names, shapes, dtypes, and file offsets. It can
support a stored-parameter count but does not prove that tensors contain equal
weights, that a model loaded correctly, or that original training reproduced.
HTTP requests are capped to a short range and a 4 MiB header limit.
"""
from __future__ import annotations

import json
import math
import struct
import urllib.error
import urllib.request
from pathlib import Path

REPO = "aradmanamnaoon/persian-lm-from-scratch"
API = f"https://huggingface.co/api/models/{REPO}"
MAX_HEADER_BYTES = 4 * 1024 * 1024


def get_bytes(url: str, limit: int, range_header: str | None = None) -> bytes:
    headers = {"User-Agent": "GA-01A-evidence-audit/1.0"}
    if range_header:
        headers["Range"] = range_header
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=50) as response:
        return response.read(limit + 1)[:limit]


def tensor_header(url: str) -> dict:
    first = get_bytes(url, 8, "bytes=0-7")
    if len(first) != 8:
        raise RuntimeError("Could not fetch eight-byte safetensors header length")
    n = struct.unpack("<Q", first)[0]
    if n == 0 or n > MAX_HEADER_BYTES:
        raise RuntimeError(f"Header length outside safe bounds: {n}")
    # Fetch the 8-byte prefix and header together so HTTP Range behavior is
    # clear regardless of whether the server returns 200 or 206.
    headers = {"User-Agent": "GA-01A-evidence-audit/1.0", "Range": f"bytes=0-{n+7}"}
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        raw = response.read(n + 8)
    if len(raw) != n + 8 or struct.unpack("<Q", raw[:8])[0] != n:
        raise RuntimeError("Safetensors header not returned in full or changed mid-request")
    value = json.loads(raw[8:].decode("utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError("Invalid safetensors header")
    return value


def main() -> None:
    api = json.loads(get_bytes(API, 2 * 1024 * 1024).decode("utf-8"))
    rev = api.get("sha")
    if not isinstance(rev, str) or len(rev) < 12:
        raise RuntimeError("Model revision unavailable from official Hugging Face API")
    url = f"https://huggingface.co/{REPO}/resolve/{rev}/model.safetensors"
    hdr = tensor_header(url)
    tensors = {k: v for k, v in hdr.items() if k != "__metadata__"}
    total = 0
    by_dtype: dict[str, int] = {}
    names = []
    for k, value in tensors.items():
        if not isinstance(value, dict) or not isinstance(value.get("shape"), list):
            raise RuntimeError("Malformed tensor shape in safetensors header")
        shape = value["shape"]
        if any(not isinstance(i, int) or i < 0 for i in shape):
            raise RuntimeError("Invalid tensor dimension")
        count = math.prod(shape)
        total += count
        by_dtype[value.get("dtype", "?")] = by_dtype.get(value.get("dtype", "?"), 0) + count
        if any(fragment in k.lower() for fragment in ("lm_head", "head.weight", "embed", "wte", "tok_emb", "token")):
            names.append({"tensor": k, "shape": shape, "elements": count})
    report = {
        "repo": REPO,
        "revision": rev,
        "file": "model.safetensors",
        "source": f"https://huggingface.co/{REPO}/tree/{rev}",
        "tensor_count": len(tensors),
        "stored_elements": total,
        "stored_parameters_millions": round(total / 1_000_000, 4),
        "stored_elements_by_dtype": by_dtype,
        "embedding_and_output_head_tensors": names,
        "interpretation": "Stored safetensors elements only. Does not prove runtime tying, exact historical training, or performance metrics.",
    }
    Path("persian_checkpoint_header_report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
