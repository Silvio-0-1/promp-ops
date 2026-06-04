# Phase 4 — Prompt Deployment

Once a prompt version passes evaluation, deploy it the way you'd deploy code:

- **Environment promotion** — dev → staging → production.
- **Gradual rollout** — release to a small percentage of traffic first.
- **A/B testing** — run two prompt versions side-by-side and compare metrics.
- **Feature flags** — toggle prompt versions without redeploying the app.
- **CI/CD** — gate deployments behind evaluation thresholds in GitHub Actions or similar.

## Deployment KPIs

- Zero downtime during cutover.
- No regression in eval scores.
- Stable latency (p50, p95, p99).
- Controlled error rate during rollout.
- Measured time-to-rollout and traffic shift percentage.

---

Previous: [Phase 3 — Testing & Evaluation](03-testing-and-evaluation.md) · Next: [Phase 5 — Monitoring & Observability](05-monitoring-and-observability.md)
