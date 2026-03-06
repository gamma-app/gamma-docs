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
<figure><img src=".gitbook/assets/landscape-developer-clouds.png" alt="" width="375"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

## Quickstart

Authenticate with your API key via the `X-API-KEY` header. API access requires a Pro, Ultra, Teams, or Business plan.

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

```json
{ "generationId": "abc123xyz" }
```

Poll `GET /v1.0/generations/{generationId}` every 5 seconds until `status` is `completed` or `failed`. Full polling examples in [Async Patterns and Polling](overview/async-patterns-and-polling.md).

```json
{
  "status": "completed",
  "gammaUrl": "https://gamma.app/docs/abc123",
  "exportUrl": "https://gamma.app/export/abc123.pdf",
  "credits": { "deducted": 15, "remaining": 485 }
}
```

{% columns %}
{% column valign="middle" %}
Your presentation is live at `gammaUrl` and the PDF is ready at `exportUrl`.
{% endcolumn %}

{% column %}
<div data-with-frame="true"><figure><img src=".gitbook/assets/example-campaign-report.png" alt="Example API-generated presentation"><figcaption></figcaption></figure></div>
{% endcolumn %}
{% endcolumns %}

{% hint style="info" %}
Getting a 401? Gamma uses `X-API-KEY` as a custom header — not `Authorization: Bearer`. See [Error codes](errors-and-warnings/error-codes.md) for other common issues.
{% endhint %}

### Next steps

* [All generation parameters](overview/generate-api-parameters-explained.md) — format, themes, images, headers/footers, sharing
* [Template-based generation](overview/create-from-template-api-parameters-explained.md) — design once, generate variations
* [Connectors and Integrations](overview/connectors-and-integrations.md) — Claude, Zapier, Make, n8n
* [Contact sales](https://gamma.app/contact-sales) — enterprise plans and custom integrations
