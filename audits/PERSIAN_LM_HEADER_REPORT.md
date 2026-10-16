# Persian LM checkpoint tensor-header audit

**Checked:** 16 October 2026  
**Public model:** [aradmanamnaoon/persian-lm-from-scratch](https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch)  
**Exact model revision inspected:** [b443d45edab7a464edb25f49d0c4b44f05f4a739](https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch/tree/b443d45edab7a464edb25f49d0c4b44f05f4a739)  
**Evidence:** [GitHub Actions run 38866742042 (success)](https://github.com/aradmanamnaoon/aradmanamnaoon/actions/runs/38866742042), and [follow-up embedding-name audit (success)](https://github.com/aradmanamnaoon/aradmanamnaoon/actions/runs/38867424811), with 90-day JSON workflow artifacts and [auditor source](persian_checkpoint_header.py)

## Observed public checkpoint metadata

| Property | Result |
| --- | --- |
| File | `model.safetensors` |
| File revision | `b443d45edab7a464edb25f49d0c4b44f05f4a739` |
| Stored tensors | **149** |
| Total tensor elements across stored tensors | **134,994,432** (**134.9944 million**) |
| Stored tensor dtype | **F16** for all 134,994,432 elements |
| Explicit output-head tensor | `lm_head.weight`, shape **32,000 x 768**, **24,576,000** elements |
| Explicit token-embedding tensor | `tok_emb.weight`, shape **32,000 x 768**, **24,576,000** elements |
| Model-card architecture count | **110.4M (author stated)** |
| Difference (stored elements minus stated architecture count) | **approximately 24.6 million** |

The counts are derived from the downloaded **safetensors header only**, not from model loading, model weights execution, or a training run. The file revision is pinned, the algorithm is included in this repository, and the hosted audit's output provides a machine-checkable artifact.

## What this means, and does not mean

The current file stores about 135 million floating-point tensor elements. This differs from the card's ~110.4 million architecture-parameter claim. The public checkpoint serializes **both** `tok_emb.weight` and `lm_head.weight` as separately named 32,000 x 768 tensors (24,576,000 elements each); the extra stored output-head matrix nearly accounts for the numerical discrepancy. **This does not prove that the two embedding/output matrices have distinct numeric values or that the loaded model does or does not tie their weights at runtime.** A runtime and checkpoint-level investigation is needed for that question.

The previously reported **test perplexity 14.52** and model quality claims remain **author-reported**; this audit did not load data, reproduce tokenization, or run evaluation. A metadata-only count does not independently validate the training corpus, scoring protocol, license, or original training checkpoint.

## Required HF model-card correction

Revise the existing Hugging Face model card to distinguish **intended architecture count (~110.4M)** from **published checkpoint stored element count (134,994,432 on pinned revision)**. Treat runtime tying as **unverified** until actual code/config weight aliasing and numerical tensor equality have been checked. Do not silently present 110.4M as the verified size of the publicly distributed weights.

Only the verified file-level count above should be cited as such. This report is evidence of an auditable metadata inspection—not a peer-reviewed publication, paper, or an independent benchmark.
