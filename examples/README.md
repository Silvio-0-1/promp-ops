# Examples

Runnable artifacts that accompany the docs.

## Prompts

Plain-text prompt templates you can paste into any LLM playground or prompt registry.

- [`prompts/general-qa.mustache.txt`](prompts/general-qa.mustache.txt) — Mustache template for grounded Q&A.
- [`prompts/adaptive-summarizer.nunjucks.txt`](prompts/adaptive-summarizer.nunjucks.txt) — Nunjucks template that adapts tone by audience.
- [`prompts/support-reply-v3.txt`](prompts/support-reply-v3.txt) — Production-shaped customer-support prompt with guardrails.

## Python

A minimal Braintrust eval against Azure OpenAI.

- [`python/movie_matcher.py`](python/movie_matcher.py)
- [`python/requirements.txt`](python/requirements.txt)
- [`python/.env.example`](python/.env.example) — copy to `.env` and fill in your keys.

### Run

```bash
cd examples/python
pip install -r requirements.txt
cp .env.example .env   # then edit .env with your real values
braintrust eval movie_matcher.py
```
