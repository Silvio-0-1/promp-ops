# Phase 2 — Prompt Versioning

Every change to a prompt should be saved as a **new version** with a unique ID and stored in a central registry. This enables teams to:

- Track how a prompt has evolved.
- Compare evaluation results across versions.
- Safely roll out improvements.
- Roll back instantly if a new version regresses.

## Example: Iterative Improvement of a Support-Reply Prompt

### v1 — Minimal

```text
System: You are a helpful customer support assistant.
User: Reply to this customer message: {{message}}
```

### v2 — Add structure and constraints

```text
System:
You are a customer support assistant. Be polite, concise, and never promise refunds
or timelines you cannot verify.

User:
Customer message:
{{message}}

Respond with:
1. A short acknowledgement.
2. A suggested next step.
```

### v3 — Add format, guardrails, and fallback

```text
System:
You are a customer support assistant for a software product. Your goals are to be
empathetic, accurate, and safe.

User:
Customer message:
{{message}}

Instructions:
- Acknowledge the user's issue in one sentence.
- Suggest one concrete next step.
- Never invent product features, prices, or policies.
- If the request is outside your scope, reply: "I'll connect you with a human agent."

Output format:
Acknowledgement:
Next step:
Escalation needed (yes/no):
```

Prompt platforms let you switch between versions, A/B test them, and tie each version to an evaluation run.

---

Previous: [Phase 1 — Prompt Design](01-prompt-design.md) · Next: [Phase 3 — Testing & Evaluation](03-testing-and-evaluation.md)
