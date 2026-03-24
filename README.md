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

<a href="https://gamma.app/settings/api-keys" class="button primary">Get your API key</a><a href="overview/understanding-the-api-options.md" class="button secondary">API overview</a>
{% endcolumn %}

{% column %}
<figure><img src=".gitbook/assets/landscape-developer-clouds.png" alt="" width="300"></figure>
{% endcolumn %}
{% endcolumns %}

## Authentication

All requests require an API key in the `X-API-KEY` header. Generate a key from [Account Settings > API Keys](https://gamma.app/settings/api-keys).

| Header | Value | Required |
| --- | --- | --- |
| `X-API-KEY` | Your API key | Yes |
| `Content-Type` | `application/json` | Yes |

API key access requires a Pro, Ultra, Teams, or Business plan. [Some connectors](overview/connectors-and-integrations.md) work on all plans and do not require an API key.

{% hint style="info" %}
**Machine-readable docs** are available at [developers.gamma.app/llms.txt](https://developers.gamma.app/llms.txt) and [developers.gamma.app/llms-full.txt](https://developers.gamma.app/llms-full.txt). Every page is also available as markdown by appending `.md` to the URL.
{% endhint %}

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

Poll `GET /v1.0/generations/{generationId}` every 5 seconds until `status` is `completed` or `failed`. Full polling examples in [Poll for results](overview/async-patterns-and-polling.md).

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
| [/generations/from-template](endpoints/create-from-template.md) | POST | Generate from template |
| [/generations/{id}](endpoints/get-generation-status.md) | GET | Poll generation status |
| [/themes](endpoints/list-themes.md) | GET | List workspace themes |
| [/folders](endpoints/list-folders.md) | GET | List workspace folders |

{% hint style="success" %}
**Building an AI integration?** The [MCP server](overview/gamma-mcp-server.md) lets AI tools create gammas on behalf of users via OAuth with Dynamic Client Registration.
{% endhint %}

## Next steps

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Generate from text</strong></td><td>Control format, themes, images, headers/footers, and sharing.</td><td><a href="overview/generate-api-parameters-explained.md">Generate from text</a></td></tr><tr><td><strong>Generate from a template</strong></td><td>Design a template once, then generate variations programmatically.</td><td><a href="overview/create-from-template-api-parameters-explained.md">Generate from template</a></td></tr><tr><td><strong>Connect integrations</strong></td><td>Use Gamma with AI assistants and automation platforms — some require no API key.</td><td><a href="overview/connectors-and-integrations.md">Connectors</a></td></tr><tr><td><strong>Set up the MCP server</strong></td><td>Let AI tools create gammas on behalf of users via OAuth.</td><td><a href="overview/gamma-mcp-server.md">MCP Server</a></td></tr></tbody></table>
