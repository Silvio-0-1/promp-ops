# Phase 3 — Prompt Testing & Evaluation

An **eval** is a structured test that measures how well a prompt performs against predefined criteria — before it reaches users.

## Anatomy of an Eval

1. **Task** — the prompt (or workflow) under test. Takes an input, produces an output.
2. **Dataset** — real or synthetic input/expected-output pairs used as the test set.
3. **Scorer** — the logic that grades each output (exact match, semantic similarity, LLM-as-judge, custom code, etc.).

## Common Scoring Strategies

- **Exact match / regex** — for deterministic outputs (classifications, IDs).
- **Embedding similarity** — for free-form text that should be semantically close.
- **LLM-as-judge** — a second LLM grades responses against a rubric.
- **Custom code** — domain-specific checks (valid JSON, schema match, contains required fields).

## Example: Python Eval with Braintrust + Azure OpenAI

A runnable version of this lives in [`examples/python/movie_matcher.py`](../examples/python/movie_matcher.py).

```python
import os
from dotenv import load_dotenv
from braintrust import init_logger, wrap_openai, Eval
from autoevals import ExactMatch
from openai import AzureOpenAI

load_dotenv()

PROJECT_NAME = os.getenv("BRAINTRUST_DEFAULT_PROJECT_NAME", "PromptOps Demo")
logger = init_logger(project=PROJECT_NAME)

azure_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
client = wrap_openai(azure_client)

SYSTEM_PROMPT = (
    "Based on the following description, identify the movie. "
    "Reply with only the exact title (no year, no quotes, no extra words)."
)

def task(movie_description: str) -> str:
    resp = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": movie_description},
        ],
        temperature=0,
    )
    return resp.choices[0].message.content.strip()

Eval(
    PROJECT_NAME,
    experiment_name="Movie matcher (Azure)",
    data=[
        {"input": "A detective investigates a series of murders based on the seven deadly sins.", "expected": "Se7en"},
        {"input": "A thief who steals corporate secrets through dream-sharing tech is tasked with planting an idea.", "expected": "Inception"},
        {"input": "A hacker learns the true nature of reality and fights its controllers.", "expected": "The Matrix"},
        {"input": "A cowboy doll gets jealous of a new spaceman toy.", "expected": "Toy Story"},
        {"input": "An orphan discovers he's a wizard and goes to Hogwarts.", "expected": "Harry Potter and the Sorcerer's Stone"},
    ],
    task=task,
    scores=[ExactMatch()],
)
```

Run it with:

```bash
braintrust eval movie_matcher.py
```

Typical metrics to track per run: **average score**, **per-row score distribution**, **end-to-end latency**, **model latency**, **token usage / cost**.

---

Previous: [Phase 2 — Prompt Versioning](02-prompt-versioning.md) · Next: [Phase 4 — Deployment](04-deployment.md)
