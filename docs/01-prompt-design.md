# Phase 1 — Prompt Design

Prompt design is the practice of writing and refining instructions so the model behaves predictably and usefully. A well-designed prompt typically defines a **role**, gives **clear instructions**, supplies **context or examples**, and specifies an **output format**.

Most prompt platforms (e.g., Braintrust, PromptLayer, Langfuse) let you configure prompts as first-class objects with a name, slug, model parameters, system/user messages, response format, and metadata — turning a prompt into a **versioned, reusable component**.

## Templating: Mustache

Mustache is a simple templating syntax that injects runtime variables using `{{variable}}`.

**Example — General Q&A Assistant**

```text
System:
You are a helpful assistant that answers questions based only on the provided context.

User:
Context:
{{context}}

Question:
{{question}}

Instructions:
- Use only the information in the context above.
- If the answer is not in the context, reply: "I don't know based on the provided information."
- Keep your answer concise and factual.
```

**Runtime input (JSON):**

```json
{
  "context": "The Eiffel Tower was completed in 1889 and stands 330 meters tall, including antennas.",
  "question": "How tall is the Eiffel Tower?"
}
```

**Expected output:**

> The Eiffel Tower stands 330 meters tall, including antennas.

## Templating: Nunjucks / Jinja

Nunjucks adds conditional logic, loops, and filters — useful when a single prompt must adapt to multiple input shapes.

**Example — Adaptive Summarizer**

```text
System:
You are an assistant that summarizes text for different audiences.

User:
Text:
{{ text }}

{% if audience == "child" %}
Summarize this in simple language a 10-year-old would understand. Use short sentences.
{% elif audience == "expert" %}
Summarize this for a domain expert. Preserve technical terminology and nuance.
{% else %}
Provide a clear, neutral summary for a general adult reader.
{% endif %}

Instructions:
- Stay faithful to the source text.
- Do not add information that is not present.
```

**Runtime input (JSON):**

```json
{
  "audience": "child",
  "text": "Photosynthesis is the biochemical process by which plants convert light energy, water, and carbon dioxide into glucose and oxygen."
}
```

The same techniques — clear role, explicit constraints, output format, and templating — let you build reusable prompts that can be systematically evaluated in [Phase 3](03-testing-and-evaluation.md).

---

Previous: [Success Criteria](success-criteria.md) · Next: [Phase 2 — Prompt Versioning](02-prompt-versioning.md)
