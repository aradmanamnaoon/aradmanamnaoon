# Seyyed Arad Hosseini Moghaddam

**AI Engineer & Data Scientist** · `ARADMANAMNAOON`

I build machine-learning software spanning computer vision, medical imaging,
natural-language processing, and agent-based retrieval. My published repositories
and model cards document a PyTorch/MONAI cardiac MRI segmentation project,
a research-assistant platform, data-leakage auditing tools, and Persian NLP model
artifacts. I prioritize traceable evaluations, limitations, and reproducible
research engineering; third-party adoption and experimental results are assessed
per project rather than assumed.

[Portfolio](https://aradmanamnaoon.github.io/) ·
[Projects](https://aradmanamnaoon.github.io/projects/) · [Technical
Writing](https://aradmanamnaoon.github.io/blog/) · [Hugging
Face](https://huggingface.co/aradmanamnaoon) ·
[LinkedIn](https://www.linkedin.com/in/seyyed-arad-hosseini-moghaddam)

## What I work on

-   **Agentic AI & RAG:** multi-agent workflows, retrieval, tool use,
    reflection, persistence, evaluation, and observability.
-   **Language models:** training transformers from scratch, QLoRA/LoRA
    fine-tuning, structured extraction, and machine translation.
-   **Persian NLP:** Persian language modeling, English-to-Persian
    translation, tokenization, and dataset preparation.
-   **Medical AI:** 3D medical-image segmentation and research-oriented
    clinical NLP.
-   **ML engineering:** PyTorch, Transformers, LangGraph, LangSmith,
    FastAPI, Docker, ChromaDB, PEFT, TRL, and MONAI.

## Selected work

| Public artifact | Documented scope | Evidence boundary |
| --- | --- | --- |
| [AI Research Assistant Platform](https://github.com/aradmanamnaoon/ai-research-assistant-platform) | LangGraph multi-agent research workflow, retrieval, reflection, FastAPI, and evaluation utilities | README reports 103 offline tests; this profile does not independently verify CI or deployed answer quality. |
| [Persian language model from scratch](https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch) | Decoder-only Persian LM, tokenizer, training corpus, and evaluation documentation | Card reports test perplexity 14.52; metric and parameter count need reproducible independent checks before citation. |
| [3D Cardiac MRI Segmentation](https://github.com/aradmanamnaoon/medical-image-segmentation) | MONAI/PyTorch 3D U-Net segmentation and sliding-window inference | README reports best validation Dice 0.8821; not independently reproduced or clinically validated. |
| [Messy2JSON](https://huggingface.co/aradmanamnaoon/messy2json-qwen-0.5b) | QLoRA-based text-to-JSON extraction | Model card contains author-reported validation metrics; external reliability and schema-validity assessment are not established here. |
| [NLLB English–Persian Psychology Translation](https://huggingface.co/aradmanamnaoon/nllb-en-fa-psych-translation) | Domain-focused EN→FA model adaptation | Training-data provenance and held-out BLEU/chrF/COMET are incomplete in the public model card. Not for clinical decisions. |
| [Jibay2 Medical](https://huggingface.co/aradmanamnaoon/jibay2-medical-v2) | Experimental QLoRA medical-note summarization adapter | Author-reported validation loss is not a measure of clinical correctness; no formal medical validation is established. |
| [CohortSeal](https://github.com/aradmanamnaoon/cohortseal) | Patient-group and exact-duplicate split auditing for medical imaging metadata | Synthetic benchmarks and audit rules do not establish clinical validation or external cohort performance. |
| [Holdout Ledger](https://github.com/aradmanamnaoon/Holdout-Ledger) | Text/group leakage audits with preserved reviewable evaluation boundaries | README-reported test and coverage claims require inspection of corresponding CI evidence. |

## Research direction and collaboration

I am developing a research direction in reproducible computational psychology
and neuroscience, particularly scientific software, benchmark design,
methodologically sound ML evaluation, and responsible data governance.
This is a developing research interest, **not** a claim of formal research
affiliation, a peer-reviewed publication, or independent clinical validation.

### How to interpret this portfolio

These are traceable software and model artifacts. Repo ownership and self-reported
validation results are not third-party scientific endorsements. For publication,
research collaboration, or grant use, inspect the corresponding code, datasets,
licenses, data splits, checkpoints, scripts, and independently verified results.
Credit human contributors and disclose material AI-assisted work in the relevant
project documentation.

## Public models & data

My Hugging Face work includes Persian language modeling,
English-to-Persian translation, structured extraction, clinical NLP,
LoRA/QLoRA adapters, and a cleaned Persian Wikipedia dataset.

**Hugging Face:**
[huggingface.co/aradmanamnaoon](https://huggingface.co/aradmanamnaoon)

## Technical writing

I write first-hand engineering notes about model training, debugging,
experiments, and the parts of ML projects that do not fit neatly into a
README.

**Latest:** [A Hugging Face Gradient Accumulation Bug Almost Ruined My
19-Hour NLLB Training
Run](https://aradmanamnaoon.github.io/blog/hugging-face-nllb-gradient-accumulation-bug/)

## Core stack

`Python` · `PyTorch` · `Transformers` · `LangGraph` · `LangChain` ·
`LangSmith` · `RAG` · `ChromaDB` · `FastAPI` · `Docker` · `PEFT` ·
`QLoRA` · `TRL` · `MONAI`

------------------------------------------------------------------------

**Portfolio:**
[aradmanamnaoon.github.io](https://aradmanamnaoon.github.io/)\
**Projects:**
[aradmanamnaoon.github.io/projects](https://aradmanamnaoon.github.io/projects/)\
**Hugging Face:**
[huggingface.co/aradmanamnaoon](https://huggingface.co/aradmanamnaoon)
