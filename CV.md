# Evidence-Based Technical CV — Seyyed Arad Hosseini Moghaddam

**AI Engineer & Data Scientist**  
**Research direction:** Reproducible machine learning, medical imaging, computational psychology and neuroscience.

[Portfolio](https://aradmanamnaoon.github.io/) · [Code](https://github.com/aradmanamnaoon) · [Models and datasets](https://huggingface.co/aradmanamnaoon) · [Research profile](RESEARCH_PROFILE.md)

*Version: 16 October 2026. This is an evidence-based technical portfolio CV, not proof of degree completion, formal employment, peer-reviewed publication, or institutional affiliation.*

## Professional summary

I develop software and machine-learning artifacts across medical-image segmentation, Persian NLP, language-model adaptation, research agents, and data-integrity auditing. My current research interests involve reproducible AI methods for psychology and neuroscience, with attention to group leakage, provenance, transparent evaluation and responsible scientific communication.

## Selected technical work

### 3D cardiac MRI segmentation — MONAI / PyTorch
[Source and audit scope](https://github.com/aradmanamnaoon/medical-image-segmentation)
- Developed a two-class 3D U-Net pipeline for left-atrium versus background segmentation on the Medical Segmentation Decathlon Task02 Heart data; includes MRI preprocessing, training, sliding-window inference and qualitative visualization.
- The repository's own [training summary](https://github.com/aradmanamnaoon/medical-image-segmentation/blob/main/results/training_summary.txt) reports **validation Dice 0.8821 at epoch 92**. This is *author-reported*, not independently reproduced or clinically validated.
- Current code lacks a public checkpoint, verified external test performance and demonstrated patient-level split independence.

### CohortSeal and Holdout Ledger — evaluation integrity
[CohortSeal](https://github.com/aradmanamnaoon/cohortseal) · [Holdout Ledger](https://github.com/aradmanamnaoon/Holdout-Ledger)
- Public research-software artifacts for detecting exact/group-level data contamination, retaining reviewable split boundaries and reporting potential leakage.
- Synthetic benchmarks and README test claims are project-level artifacts; third-party adoption and clinical efficacy are not asserted.

### AI Research Assistant Platform — agentic retrieval systems
[Code](https://github.com/aradmanamnaoon/ai-research-assistant-platform)
- Documents LangGraph multi-agent workflows, retrieval, research synthesis, FastAPI endpoints, and deterministic offline testing.
- Test counts and evaluation descriptions are author-provided; independent answer-quality benchmarking has not been established.

### Persian GPT — language-model experiment
[Model card](https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch)
- Public model and tokenizer artifacts describing from-scratch Persian Wikipedia language-model training and held-out evaluation.
- Author reports test perplexity **14.52**. Exported model parameter count and weight tying have an unresolved discrepancy; claims should await a checkpoint audit.

### Persian NLP, translation, and structured extraction
[NLLB EN→FA psychology](https://huggingface.co/aradmanamnaoon/nllb-en-fa-psych-translation) · [Messy2JSON](https://huggingface.co/aradmanamnaoon/messy2json-qwen-0.5b) · [PsyLex Studio](https://github.com/aradmanamnaoon/PsyLex-Studio)
- Public artifacts for English–Persian psychology-domain machine translation, QLoRA text-to-JSON extraction, and a local-first psychology terminology workbench.
- Model-card evaluations and dataset provenance need separate verification; professional translation and clinical uses are not validated.

## Methods and technical stack

- **ML / medical imaging:** Python, PyTorch, MONAI, 3D U-Net, NIfTI preprocessing, patch-based training, inference and evaluation.
- **Language models:** Transformers, tokenization, Hugging Face, PEFT / LoRA / QLoRA, fine-tuning and corpus workflows.
- **Systems:** LangGraph, RAG, FastAPI, Git/GitHub, GitHub Actions, Docker and software documentation.
- **Research interests:** Reproducibility, auditability, data provenance, patient/group-level splitting, benchmark design, statistics for psychology and humanities data.

## Research and collaboration interests

Open-science ML infrastructure; computational psychiatry/neuroscience and psychology (developing interest); responsible medical AI evaluation; scientifically useful, well-tested research software. I am interested in projects with explicit research questions, legal data access, clear roles, and reproducible baseline evaluation.

## Evidence and declarations

This document does **not** assert an academic degree, current university membership, clinical credential, grant, peer-reviewed paper, award, independent clinical outcome, or verified authorship of cited third-party papers. Education credentials and researcher IDs should only be added after human verification of primary records. GitHub/Hugging Face hosting demonstrates linked artifacts, not guaranteed solo authorship. Model scores are clearly marked **author-reported** unless independently reproduced.

**See [RESEARCH_PROFILE.md](RESEARCH_PROFILE.md) for source-linked technical detail and limitations.**
