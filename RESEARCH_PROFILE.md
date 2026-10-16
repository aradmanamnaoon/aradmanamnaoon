# Technical & Research Profile

**Seyyed Arad Hosseini Moghaddam**  
*AI engineer and data scientist | Medical imaging, NLP, reproducible ML software*

[Portfolio](https://aradmanamnaoon.github.io/) · [GitHub](https://github.com/aradmanamnaoon) · [Hugging Face](https://huggingface.co/aradmanamnaoon) · [Technical writing](https://aradmanamnaoon.github.io/blog/)

> **Evidence policy (updated 16 October 2026).** This profile links to publicly accessible software and model artifacts. It does not assert a degree, academic affiliation, peer-reviewed paper, award, grant, clinical validation, research appointment, or independent adoption. Metrics are attributed to their source and clearly distinguished from independently reproduced results. Public accounts support artifact ownership but not identity-document verification or sole authorship.

## Profile

I develop machine-learning systems spanning deep learning for medical imaging, Persian NLP and language-model training, structured extraction, and agent-based retrieval workflows. My publicly documented work also includes tooling to audit data-split leakage and evaluation integrity.

I am developing research interests in **computational neuroscience and psychology**, with an emphasis on reproducible software, defensible evaluation, responsible data handling, and collaborative scientific tooling.

## Selected work and direct evidence

| Artifact | Publicly inspectable work | Evidence boundary |
| --- | --- | --- |
| [3D cardiac MRI segmentation](https://github.com/aradmanamnaoon/medical-image-segmentation) | PyTorch/MONAI 3D U-Net, NIfTI data pipeline, sliding-window inference and code for two-class (background/left-atrium) segmentation on Medical Segmentation Decathlon Task02 Heart. | [Training summary](https://github.com/aradmanamnaoon/medical-image-segmentation/blob/main/results/training_summary.txt) reports Dice 0.8821 (epoch 92); full external reproduction and clinical validation are not established. |
| [Persian GPT from scratch](https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch) | Published model artifact with tokenizer/training and author-reported language-model evaluation. | A [pinned safetensors-header audit](audits/PERSIAN_LM_HEADER_REPORT.md) counted **134,994,432 stored tensor elements** (149 tensors) in the public checkpoint; the card states 110.4M. This does not resolve runtime weight tying or reproduce test perplexity. |
| [AI Research Assistant Platform](https://github.com/aradmanamnaoon/ai-research-assistant-platform) | LangGraph research-agent workflow, retrieval, tools, FastAPI and evaluation interfaces. | README describes offline test coverage; the existence of tests is not proof of independent answer quality or deployment uptake. |
| [CohortSeal](https://github.com/aradmanamnaoon/cohortseal) | Patient-group and exact-duplicate split auditing for research metadata. | Synthetic demonstration is not medical validity or verified real-world adoption. |
| [Holdout Ledger](https://github.com/aradmanamnaoon/Holdout-Ledger) | Text/group leakage checks and reviewable repairs for ML evaluation splits. | A clean audit cannot establish absence of all contamination, especially unobserved near duplicates. |
| [PsyLex Studio](https://github.com/aradmanamnaoon/PsyLex-Studio) | English–Persian psychology terminology and translation workbench. | Source code and documented Windows release are public; professional translation quality is not independently validated. |
| [Messy2JSON](https://huggingface.co/aradmanamnaoon/messy2json-qwen-0.5b) | Experimental QLoRA text-to-JSON structured extraction model. | Reported metrics come from the author card and are not an external schema-validity/generalization benchmark. |
| [NLLB psychology EN→FA model](https://huggingface.co/aradmanamnaoon/nllb-en-fa-psych-translation) | English-to-Persian model adaptation for psychology-related language. | Training-data provenance and held-out BLEU/chrF/COMET evaluation remain incompletely documented. |
| [Jibay2 Medical adapter](https://huggingface.co/aradmanamnaoon/jibay2-medical-v2) | Experimental clinical-note language-model adaptation. | **Not formally clinically validated**; not suitable for medical decision-making without independent validation. |

## Relevant technical methods

- **ML and deep learning:** Python, PyTorch, MONAI, computer vision, training and inference pipelines, reproducibility checks.
- **Language and agent systems:** Transformers, Hugging Face, LoRA/QLoRA, LangGraph, RAG, retrieval and evaluation.
- **Engineering:** FastAPI, Git/GitHub, Docker, GitHub Actions and version-controlled experiment documentation.
- **Research methods (developing focus):** split integrity, data provenance, evaluation baselines, transparent limitations, statistical analysis, and applied AI for psychology/neuroscience research.

## Collaboration interests

I am interested in well-scoped, evidence-led work on scientific software, behavioral/neuroscience benchmarks, reproducible medical-imaging pipelines, open data governance, and evaluation methodology. A useful collaboration starts with an explicit research question, source/usage rights, a reproducible baseline, and clear contributor responsibilities.

**Credit and AI-use policy:** Scientific outputs should identify actual human contributors, third-party dependencies, dataset permissions and any material AI-assisted contribution. Publishing software is not itself a peer-reviewed finding.

## Verification and availability

- **Software and models:** Follow the repository and model-card links above; inspect current commits, licenses, scripts, model versions and limitations.
- **Scores:** Where stated, values are **author-reported**, not an independently certified result.
- **Academic status and formal credentials:** No degrees, school completion, fellowships, grant funding, verified publication record or ORCID identifier are asserted here. Such claims require original verification and human approval before inclusion.
- **Privacy:** This profile intentionally avoids publishing personal identity documents, school records or private contact details.

**Last reviewed:** 16 October 2026. Evidence is a snapshot, not a guarantee of ongoing accuracy.
