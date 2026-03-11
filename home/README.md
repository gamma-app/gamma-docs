---
description: >-
  Build with the Gamma API — generate presentations, documents, websites, and
  social posts programmatically.
layout:
  width: wide
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: false
  outline:
    visible: false
  pagination:
    visible: false
---

# Gamma Developer Documentation

One API call. Polished presentations, documents, websites, and social posts — branded, exported, and shared.

<a href="https://gamma.app/settings" class="button primary">Get your API key</a><a href="../overview/understanding-the-api-options.md" class="button secondary">Read the docs</a>

## Quickstart

### 1. Start a generation

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

Response:

```json
{
  "generationId": "abc123xyz"
}
```

### 2. Poll for the result

Generation is async. Use the `generationId` from step 1 to poll until `status` is `completed` or `failed`.

{% tabs %}
{% tab title="cURL" %}
```bash
curl https://public-api.gamma.app/v1.0/generations/YOUR_GENERATION_ID \
  -H "X-API-KEY: your-api-key"
```
{% endtab %}

{% tab title="Python" %}
```python
import time

while True:
    status = requests.get(
        f"https://public-api.gamma.app/v1.0/generations/{generation_id}",
        headers={"X-API-KEY": "your-api-key"},
    ).json()
    if status["status"] in ("completed", "failed"):
        break
    time.sleep(5)
```
{% endtab %}

{% tab title="JavaScript" %}
```javascript
let status;
do {
  await new Promise((r) => setTimeout(r, 5000));
  const res = await fetch(
    `https://public-api.gamma.app/v1.0/generations/${generationId}`,
    { headers: { "X-API-KEY": "your-api-key" } }
  );
  status = await res.json();
} while (status.status !== "completed" && status.status !== "failed");
```
{% endtab %}
{% endtabs %}

Response when complete:

```json
{
  "generationId": "abc123xyz",
  "status": "completed",
  "gammaUrl": "https://gamma.app/docs/abc123",
  "exportUrl": "https://gamma.app/export/abc123.pdf",
  "credits": {
    "deducted": 10,
    "remaining": 490
  }
}
```

### 3. Use your Gamma

Open `gammaUrl` to view it, or download `exportUrl` for the PDF, PPTX, or PNG.

{% columns %}
{% column valign="middle" %}
## Choose how you build

Gamma API gives you full control over content generation — format, theme, layout, images, export, and sharing. Or skip the code entirely with connectors and no-code platforms.
{% endcolumn %}

{% column %}
<figure><img src=".gitbook/assets/landscape-developer.png" alt="" width="375"></figure>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
### <i class="fa-code">:code:</i> Gamma API

Generate from text or templates, apply themes, configure headers/footers, set permissions, and auto-export.

* [Generate API parameters](../overview/generate-api-parameters-explained.md)
* [Create from Template](../overview/create-from-template-api-parameters-explained.md)
* [Async patterns and polling](../overview/async-patterns-and-polling.md)
{% endcolumn %}

{% column %}
### <i class="fa-robot">:robot:</i> Connectors & MCP

Use Gamma from Claude and other AI assistants. Generate content through natural conversation.

* [Connect integrations](../overview/connectors-and-integrations.md)
* [MCP server](../overview/gamma-mcp-server.md)
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
### <i class="fa-wand-magic-sparkles">:wand-magic-sparkles:</i> No-Code Automation

Zapier, Make, and n8n. Trigger generation from forms, CRMs, spreadsheets — no code required.

* [Zapier, Make, and n8n setup](../overview/connectors-and-integrations.md)
{% endcolumn %}

{% column %}
### <i class="fa-key">:key:</i> Get Access

Available on Pro, Ultra, Teams, and Business plans.

* [Access and pricing](../overview/access-and-pricing.md)
* [Get help](../overview/get-help.md)
{% endcolumn %}
{% endcolumns %}

## What you can build

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4><i class="fa-bolt">:bolt:</i> Generate from text</h4></td><td>Control format, tone, audience, card count, and language.</td><td><a href="../overview/generate-api-parameters-explained.md">Generate API parameters</a></td></tr><tr><td><h4><i class="fa-layer-group">:layer-group:</i> Generate from template</h4></td><td>Design a template in the app, generate new content into the same layout.</td><td><a href="../overview/create-from-template-api-parameters-explained.md">Create from Template</a></td></tr><tr><td><h4><i class="fa-palette">:palette:</i> Apply brand themes</h4></td><td>Lock every generation to your brand colors, fonts, and logo.</td><td><a href="../overview/list-themes-and-list-folders-apis-explained.md">Themes and Folders APIs</a></td></tr><tr><td><h4><i class="fa-file-export">:file-export:</i> Export to PDF, PPTX, PNG</h4></td><td>Auto-export on completion. Download from the export URL.</td><td><a href="../overview/async-patterns-and-polling.md">Async patterns and polling</a></td></tr><tr><td><h4><i class="fa-table-columns">:table-columns:</i> Custom headers & footers</h4></td><td>Logos, page numbers, and text in 6 positions per card.</td><td><a href="../overview/header-and-footer-formatting.md">Header and footer formatting</a></td></tr><tr><td><h4><i class="fa-share-nodes">:share-nodes:</i> Sharing & permissions</h4></td><td>Workspace access, external links, and email sharing in one call.</td><td><a href="../overview/generate-api-parameters-explained.md">Generate API parameters</a></td></tr></tbody></table>

## What's new

{% updates format="full" %}
{% update date="2025-02-18" %}
## Claude Connector

Create gammas directly from Claude conversations.

[Set up the Claude Connector →](../overview/connectors-and-integrations.md)
{% endupdate %}

{% update date="2025-02-10" %}
## Gamma MCP Server

Give AI tools the ability to create gammas on your behalf via OAuth with Dynamic Client Registration.

[Learn about Gamma MCP →](../overview/gamma-mcp-server.md)
{% endupdate %}

{% update date="2025-01-15" %}
## n8n Native Node

Generate content, list themes and folders, and poll for results with a native Gamma node.

[See the n8n integration →](../overview/connectors-and-integrations.md)
{% endupdate %}
{% endupdates %}

## Resources

{% columns %}
{% column %}
**[API Slack Channel](https://join.slack.com/t/gambassadors/shared_invite/zt-39mcf05ys-419f~BVFyEtsCsDb9Ij3ow)**
Questions, debugging help, and community.
{% endcolumn %}

{% column %}
**[Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSeRHjChH8DS6YC4WS23LlOb1SC1Fw2HvuPFZ3HFM4rYj16oCg/viewform?usp=header)**
Share broader feedback about the API.
{% endcolumn %}
{% endcolumns %}
