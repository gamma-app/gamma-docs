---
description: >-
  Build with the Gamma API — generate presentations, documents, websites, and
  social posts programmatically.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Gamma Developer Documentation

{% columns %}
{% column valign="middle" %}
One API call. Polished presentations, documents, websites, and social posts — branded, exported, and shared.

<a href="https://gamma.app/settings/api-keys" class="button primary">Get your API key</a><a href="overview/generate-api-parameters-explained.md" class="button secondary">API reference</a>
{% endcolumn %}

{% column %}
<figure><img src=".gitbook/assets/landscape-developer.png" alt="" width="375"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

## Quickstart

Authenticate with your API key via the `X-API-KEY` header. API access requires a Pro, Ultra, Teams, or Business plan.

### 1. Create a generation

{% tabs %}
{% tab title="cURL" %}
```bash
curl -X POST https://public-api.gamma.app/v1.0/generations \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: $GAMMA_API_KEY" \
  -d '{
    "inputText": "Q3 product launch strategy",
    "textMode": "generate",
    "format": "presentation",
    "numCards": 10,
    "exportAs": "pdf"
  }'
```
{% endtab %}

{% tab title="Python" %}
```python
import requests, os

response = requests.post(
    "https://public-api.gamma.app/v1.0/generations",
    headers={
        "X-API-KEY": os.environ["GAMMA_API_KEY"],
        "Content-Type": "application/json",
    },
    json={
        "inputText": "Q3 product launch strategy",
        "textMode": "generate",
        "format": "presentation",
        "numCards": 10,
        "exportAs": "pdf",
    },
)
response.raise_for_status()
generation_id = response.json()["generationId"]
```
{% endtab %}

{% tab title="JavaScript" %}
```javascript
const response = await fetch(
  "https://public-api.gamma.app/v1.0/generations",
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": process.env.GAMMA_API_KEY,
    },
    body: JSON.stringify({
      inputText: "Q3 product launch strategy",
      textMode: "generate",
      format: "presentation",
      numCards: 10,
      exportAs: "pdf",
    }),
  }
);
const { generationId } = await response.json();
```
{% endtab %}
{% endtabs %}

Response:

```json
{
  "generationId": "abc123xyz"
}
```

### 2. Poll for results

Poll `GET /v1.0/generations/{generationId}` every 5 seconds until `status` is `completed` or `failed`.

```bash
curl https://public-api.gamma.app/v1.0/generations/abc123xyz \
  -H "X-API-KEY: $GAMMA_API_KEY"
```

Completed response:

```json
{
  "generationId": "abc123xyz",
  "status": "completed",
  "gammaUrl": "https://gamma.app/docs/abc123",
  "exportUrl": "https://gamma.app/export/abc123.pdf",
  "credits": { "deducted": 15, "remaining": 485 }
}
```

That's it — your presentation is live at `gammaUrl` and the PDF is ready at `exportUrl`.

{% hint style="info" %}
Getting a 401? Gamma uses `X-API-KEY` as a custom header — not `Authorization: Bearer`. See [Error codes](errors-and-warnings/error-codes.md) for other common issues.
{% endhint %}

### Next steps

Browse the sidebar for the full API surface, or jump to:

* [All generation parameters](overview/generate-api-parameters-explained.md) — format, themes, images, headers/footers, sharing
* [Template-based generation](overview/create-from-template-api-parameters-explained.md) — design once, generate variations
* [Connectors and Integrations](overview/connectors-and-integrations.md) — Claude, Zapier, Make, n8n
