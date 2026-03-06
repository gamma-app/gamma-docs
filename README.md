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

<a href="https://gamma.app/settings" class="button primary">Get your API key</a><a href="overview/understanding-the-api-options.md" class="button secondary">API overview</a>
{% endcolumn %}

{% column %}
<figure><img src=".gitbook/assets/landscape-developer.png" alt="" width="375"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

### Make your first request

{% tabs %}
{% tab title="cURL" %}
```bash
curl -X POST https://public-api.gamma.app/v1.0/generations \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: your-api-key" \
  -d '{
    "inputText": "Q3 product launch strategy",
    "textMode": "generate",
    "format": "presentation",
    "themeId": "your-theme-id",
    "numCards": 10,
    "exportAs": "pdf"
  }'
```
{% endtab %}

{% tab title="Python" %}
```python
import requests

response = requests.post(
    "https://public-api.gamma.app/v1.0/generations",
    headers={"X-API-KEY": "your-api-key"},
    json={
        "inputText": "Q3 product launch strategy",
        "textMode": "generate",
        "format": "presentation",
        "themeId": "your-theme-id",
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
      "X-API-KEY": "your-api-key",
    },
    body: JSON.stringify({
      inputText: "Q3 product launch strategy",
      textMode: "generate",
      format: "presentation",
      themeId: "your-theme-id",
      numCards: 10,
      exportAs: "pdf",
    }),
  }
);
const { generationId } = await response.json();
```
{% endtab %}
{% endtabs %}

Then poll `GET /v1.0/generations/{generationId}` until `status` is `completed`. See [Async Patterns and Polling](overview/async-patterns-and-polling.md) for full examples.

## Choose how you build

{% columns %}
{% column %}
### <i class="fa-code">:code:</i> Gamma API

Generate from text or templates, apply themes, configure headers/footers, set permissions, and auto-export.

* [Generate API parameters](overview/generate-api-parameters-explained.md)
* [Create from Template](overview/create-from-template-api-parameters-explained.md)
* [Async patterns and polling](overview/async-patterns-and-polling.md)
{% endcolumn %}

{% column %}
### <i class="fa-robot">:robot:</i> Connectors & MCP

Use Gamma from Claude and other AI assistants. Generate content through natural conversation.

* [Connectors and Integrations](overview/connectors-and-integrations.md)
* [Gamma MCP Server](overview/gamma-mcp-server.md)
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
### <i class="fa-wand-magic-sparkles">:wand-magic-sparkles:</i> No-Code Automation

Zapier, Make, and n8n. Trigger generation from forms, CRMs, spreadsheets — no code required.

* [Zapier, Make, and n8n setup](overview/connectors-and-integrations.md)
{% endcolumn %}

{% column %}
### <i class="fa-key">:key:</i> Get Access

Available on Pro, Ultra, Teams, and Business plans.

* [Access and pricing](overview/access-and-pricing.md)
* [Get help](overview/get-help.md)
{% endcolumn %}
{% endcolumns %}
