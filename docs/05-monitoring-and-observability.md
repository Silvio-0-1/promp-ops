# Phase 5 — Monitoring & Observability

Evals tell you how a prompt behaves on a fixed dataset. Monitoring tells you how it behaves on **real user traffic**.

## What to Capture per Production Call

- **Input** — the user query / variables.
- **Output** — the model response.
- **Metadata** — request ID, latency, model name & version, token usage, safety/content-filter status.
- **User feedback** — thumbs up/down, ratings, free-text comments.
- **Downstream signals** — task completion, conversion, escalation to a human.

## Observability Features to Look For

- **Trace logging** — every interaction stored with prompt, response, and metadata.
- **Feedback scoring** — user ratings mapped to custom scoring logic.
- **Timeline visualization** — traces displayed chronologically for inspection.
- **Filtering & analysis** — slice by time window, model version, score, user segment.
- **Alerting** — automatic notifications when scores or latency drift.

Platforms such as Braintrust, Langfuse, LangSmith, PromptLayer, and Arize provide these capabilities out of the box.

---

Previous: [Phase 4 — Deployment](04-deployment.md) · Next: [Phase 6 — Governance & Collaboration](06-governance-and-collaboration.md)
