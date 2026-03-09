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

One API call. Polished presentations, documents, websites, and social posts — branded, exported, and shared.

<a href="https://gamma.app/settings/api-keys" class="button primary">Get your API key</a><a href="overview/understanding-the-api-options.md" class="button secondary">API overview</a>

## Authentication

All requests require an API key in the `X-API-KEY` header. Generate a key from [Account Settings > API Keys](https://gamma.app/settings/api-keys).

| Header | Value | Required |
| --- | --- | --- |
| `X-API-KEY` | Your API key | Yes |
| `Content-Type` | `application/json` | Yes |

API key access requires a Pro, Ultra, Teams, or Business plan. [ChatGPT and Claude connectors](overview/connectors-and-integrations.md) work on all plans and do not require an API key.

## Quickstart

### 1. Start a generation

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

{% code title="Response" %}
```json
{
  "generationId": "abc123xyz"
}
```
{% endcode %}

### 2. Poll for the result

Poll `GET /v1.0/generations/{generationId}` every 5 seconds until `status` is `completed` or `failed`. Full polling examples in [Async Patterns and Polling](overview/async-patterns-and-polling.md).

{% code title="Response (completed)" %}
```json
{
  "generationId": "abc123xyz",
  "status": "completed",
  "gammaUrl": "https://gamma.app/docs/abc123",
  "exportUrl": "https://gamma.app/export/abc123.pdf",
  "credits": {
    "deducted": 15,
    "remaining": 485
  }
}
```
{% endcode %}

### 3. Use your Gamma

Your presentation is live at `gammaUrl`. If you specified `exportAs`, the file is ready at `exportUrl`.

{% hint style="info" %}
Getting a 401? Gamma uses `X-API-KEY` as a custom header — not `Authorization: Bearer`. See [Error codes](errors-and-warnings/error-codes.md) for other common issues.
{% endhint %}

## Endpoints

| Endpoint | Method | Description |
| --- | --- | --- |
| [/generations](endpoints/create-generation.md) | POST | Generate from text |
| [/generations/{id}](endpoints/get-generation-status.md) | GET | Poll generation status |
| [/generations/from-template](endpoints/create-from-template.md) | POST | Generate from template |
| [/themes](endpoints/list-themes.md) | GET | List workspace themes |
| [/folders](endpoints/list-folders.md) | GET | List workspace folders |
| [/gammas/{gammaId}/archive](endpoints/archive-gamma.md) | POST | Archive a Gamma |

{% hint style="success" %}
**Building an AI integration?** The [Gamma MCP Server](overview/gamma-mcp-server.md) lets AI tools create gammas on behalf of users via OAuth with Dynamic Client Registration.
{% endhint %}

## What's new

{% updates format="full" %}
{% update date="2026-03-06" %}
## Gamma is live on ChatGPT and Claude

Create presentations, documents, and social posts directly from [ChatGPT](overview/connectors-and-integrations.md) and [Claude](overview/connectors-and-integrations.md) — just connect Gamma and start prompting.

{% endupdate %}

{% update date="2026-02-27" %}
## Create from Template GA and new image models

Create from Template is now generally available. Plus new image models including Recraft v4, Gemini 3.1 Flash, and Flux 2.

[Full changelog →](overview/changelog.md)

{% endupdate %}
{% endupdates %}

## Next steps

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Generate from text</strong></td><td>Control format, themes, images, headers/footers, and sharing.</td><td><a href="overview/generate-api-parameters-explained.md">Generate from text</a></td></tr><tr><td><strong>Generate from a template</strong></td><td>Design a template once, then generate variations programmatically.</td><td><a href="overview/create-from-template-api-parameters-explained.md">Generate from template</a></td></tr><tr><td><strong>Connectors and Integrations</strong></td><td>ChatGPT, Claude, Zapier, Make, and n8n — no API key needed for connectors.</td><td><a href="overview/connectors-and-integrations.md">Connectors</a></td></tr><tr><td><strong>Gamma MCP Server</strong></td><td>Let AI tools create gammas on behalf of users via OAuth.</td><td><a href="overview/gamma-mcp-server.md">MCP Server</a></td></tr></tbody></table>
