# PromptOps: Phases & Findings

PromptOps is the practice of standardizing how prompts for generative AI systems are **designed, tested, deployed, monitored, and governed** — so that AI behavior becomes predictable, measurable, and improvable over time, much like DevOps did for software.

This repository documents a six-phase PromptOps lifecycle with examples, prompt patterns, and evaluation code that apply to **any** prompt-driven application — chatbots, document Q&A, code assistants, content generation, classification, summarization, and more.

---

## Contents

### Concepts
- [Why PromptOps & Success Criteria](docs/success-criteria.md)
- [Tooling Landscape](docs/tooling-landscape.md)

### The Six Phases
1. [Prompt Design](docs/01-prompt-design.md)
2. [Prompt Versioning](docs/02-prompt-versioning.md)
3. [Prompt Testing & Evaluation](docs/03-testing-and-evaluation.md)
4. [Prompt Deployment](docs/04-deployment.md)
5. [Monitoring & Observability](docs/05-monitoring-and-observability.md)
6. [Governance & Collaboration](docs/06-governance-and-collaboration.md)

### Hands-On
- [Examples](examples/README.md) — runnable prompts and a Python eval.

---

## Repository Structure

```
.
├── README.md
├── LICENSE
├── .gitignore
├── docs/        # One markdown file per topic / phase
└── examples/    # Prompt templates and runnable code
```

## Getting Started

```bash
git clone https://github.com/<your-username>/promptops.git
cd promptops
```

Start with [docs/success-criteria.md](docs/success-criteria.md), then walk through the phases in order.

## Contributing

Issues and pull requests are welcome. Please open an issue first to discuss substantial changes.
