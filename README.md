# Seyyed Arad Hosseini Moghaddam

**AI Engineer & Data Scientist** · Medical Imaging · Persian NLP · Reliable ML Engineering

I build and document machine-learning systems: **3D medical-image segmentation, language models, agent-based research tools, and data-integrity software**. My developing academic interest is reproducible computational psychology and neuroscience.

[**Portfolio**](https://aradmanamnaoon.github.io/) · [**Evidence-linked technical profile**](RESEARCH_PROFILE.md) · [**Download CV (PDF)**](https://aradmanamnaoon.github.io/Profile.pdf) · [**Hugging Face**](https://huggingface.co/aradmanamnaoon) · [**Writing**](https://aradmanamnaoon.github.io/blog/) · [**LinkedIn**](https://www.linkedin.com/in/seyyed-arad-hosseini-moghaddam)

### Three projects open for serious technical feedback

I'm highlighting **three distinct, publicly inspectable projects** rather than asking people to endorse a long list. If you have relevant experience, please inspect the actual artifact and share an honest, specific technical observation.

| Project | What you can evaluate | Scope and evidence boundary |
| --- | --- | --- |
| **[Holdout Ledger](https://github.com/aradmanamnaoon/Holdout-Ledger)** · [three-minute synthetic walkthrough](https://github.com/aradmanamnaoon/Holdout-Ledger/blob/main/docs/first-run.md) | Local Python tool for cross-split text and declared-group leakage witnesses, offline reports and reviewed repairs | CI-tested synthetic example; not proven to find all leakage or validated on clinical datasets |
| **[3D Cardiac MRI Segmentation](https://github.com/aradmanamnaoon/medical-image-segmentation)** · [case study](https://aradmanamnaoon.github.io/projects/3d-cardiac-mri-segmentation/) | PyTorch/MONAI left-atrium segmentation pipeline, preprocessing, training and sliding-window inference | Passing engineering checks; **0.8821 Dice is author-reported**, not independently reproduced or clinically validated |
| **[PsyLex Studio](https://github.com/aradmanamnaoon/PsyLex-Studio)** · [Windows v0.6.5 release](https://github.com/aradmanamnaoon/PsyLex-Studio/releases/tag/v0.6.5) | Local-first English–Persian psychology terminology, translation, OCR and document workflows | Downloadable application; output needs human verification, and Python 3.13 installation CI currently needs attention |

For candid feedback, use the project's GitHub Issues or [connect on LinkedIn](https://www.linkedin.com/in/seyyed-arad-hosseini-moghaddam). Please do **not** share confidential research, patient information or proprietary corpora in public issues. Recommendations should reflect **direct knowledge of my work**, not a request to promote or star a repository.



---

## What I build

| Focus | Public examples | Questions I care about |
| --- | --- | --- |
| **Medical imaging** | [3D cardiac MRI segmentation](https://github.com/aradmanamnaoon/medical-image-segmentation) · [CohortSeal](https://github.com/aradmanamnaoon/cohortseal) | Are the datasets and evaluation boundaries defensible? |
| **Models & Persian NLP** | [Persian GPT](https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch) · [NLLB EN→FA psychology](https://huggingface.co/aradmanamnaoon/nllb-en-fa-psych-translation) · [Messy2JSON](https://huggingface.co/aradmanamnaoon/messy2json-qwen-0.5b) | What do training metrics actually establish—and what do they not? |
| **Agentic AI & research software** | [AI Research Assistant](https://github.com/aradmanamnaoon/ai-research-assistant-platform) · [Agent Guardrails](https://github.com/aradmanamnaoon/agent-guardrails) | Can a workflow be audited, bounded and meaningfully evaluated? |
| **Evaluation integrity** | [Holdout Ledger](https://github.com/aradmanamnaoon/Holdout-Ledger) · [CohortSeal](https://github.com/aradmanamnaoon/cohortseal) | Are train/test splits, group identities and data lineage protected? |
| **Psychology-language tools** | [PsyLex Studio](https://github.com/aradmanamnaoon/PsyLex-Studio) | Can researchers inspect terminology sources and review model translations? |

## Selected engineering evidence

- **3D MRI segmentation:** The linked MONAI/PyTorch repository defines a two-class *background/left-atrium* U-Net experiment on the Medical Segmentation Decathlon Task02 Heart data. Its [training summary](https://github.com/aradmanamnaoon/medical-image-segmentation/blob/main/results/training_summary.txt) reports a best validation Dice of **0.8821 at epoch 92**. This is an *author-reported* score, not independently reproduced or clinically validated.
- **Persian language model:** [Hugging Face artifact](https://huggingface.co/aradmanamnaoon/persian-lm-from-scratch) includes the author's corpus/tokenizer/training description and reported held-out evaluation. A [pinned public safetensors-header audit](audits/PERSIAN_LM_HEADER_REPORT.md) found **134,994,432 stored tensor elements** versus the model card's 110.4M claim. Runtime weight sharing and test perplexity are not independently verified.
- **Agent-based research platform:** [Repository](https://github.com/aradmanamnaoon/ai-research-assistant-platform) documents a LangGraph/FastAPI application, retrieval and deterministic offline tests. These verify software interfaces, **not** independently measured research-answer quality.
- **Medical evaluation integrity:** [CohortSeal](https://github.com/aradmanamnaoon/cohortseal) checks patient-group and exact-duplicate boundaries in research metadata. Synthetic examples do **not** certify clinical validity or real-world adoption.
- **Experimental medical NLP:** [Jibay2 adapter](https://huggingface.co/aradmanamnaoon/jibay2-medical-v2) documents model adaptation. It has **no established formal clinical validation**; training loss must not be presented as medical reliability.

## Tools and methods

**Deep learning & ML:** Python, PyTorch, MONAI, Hugging Face Transformers, PEFT, LoRA/QLoRA, computer vision, model evaluation.  
**Agents & software:** LangGraph, RAG, LangChain, FastAPI, GitHub Actions, Docker, data pipelines and reproducibility tooling.  
**Quantitative questions:** Statistics, data science for psychology and humanities datasets, experimental design and leakage-aware evaluation.

## Research direction & collaboration

I'm developing a research path at the intersection of **AI, psychology and neuroscience**. I'm interested in well-scoped contributions to reproducible scientific software, behavioral benchmarks, neuro/medical imaging tooling and transparent evaluation practices.

A useful collaboration starts with a clear scientific question, genuine dataset rights, reproducible baselines, explicit limitations, and attribution of human and AI-assisted work. Current public projects are evidence of software/model artifacts—not a claim of academic affiliation, peer-reviewed publications, external clinical validation or independent adoption.

**For technical detail and qualification of claims, see the [evidence-linked profile](RESEARCH_PROFILE.md).**

---

**Explore:** [Projects](https://aradmanamnaoon.github.io/projects/) · [Hugging Face models and datasets](https://huggingface.co/aradmanamnaoon) · [Technical articles](https://aradmanamnaoon.github.io/blog/)

<sub>Last reviewed 2026-10-16 · Public artifacts and author-reported metrics are identified separately from independently verified scientific outcomes.</sub>
