---
description: >-
  Build with the Gamma API — generate presentations, documents, websites, and
  social posts programmatically.
metaLinks:
  alternates:
    - https://app.gitbook.com/s/2AwfWOGBWBxQmyvHedqW/
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

{% columns %}
{% column valign="middle" %}
One API call. Polished presentations, documents, websites, and social posts — branded, exported, and shared. You bring the content, Gamma handles the rest.

<a href="https://gamma.app/settings" class="button primary">Get your API key</a><a href="https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/understanding-the-api-options" class="button secondary">Read the docs</a>
{% endcolumn %}

{% column %}
{% tabs %}
{% tab title="cURL" %}
{% code title="Generate a presentation" %}
```bash
curl -X POST https://public-api.gamma.app/v1.0/generations \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: your-api-key" \
  -d '{
    "inputText": "Q3 product launch strategy",
    "textMode": "generate",
    "format": "presentation",
    "numCards": 10,
    "exportAs": "pdf"
  }'
```
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code title="Generate a presentation" %}
```python
import requests

response = requests.post(
    "https://public-api.gamma.app/v1.0/generations",
    headers={"X-API-KEY": "your-api-key"},
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
{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code title="Generate a presentation" %}
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
      numCards: 10,
      exportAs: "pdf",
    }),
  }
);
const { generationId } = await response.json();
```
{% endcode %}
{% endtab %}
{% endtabs %}
{% endcolumn %}
{% endcolumns %}

<figure><img src=".gitbook/assets/landscape-developer.png" alt=""><figcaption></figcaption></figure>

## Choose how you build

{% columns %}
{% column %}
### <i class="fa-code">:code:</i> Gamma API

Full programmatic control. Generate from text or templates, apply themes, configure headers/footers, set sharing permissions, and auto-export — all in one request.

* [Generate API parameters](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/generate-api-parameters-explained)
* [Create from Template](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/create-from-template-api-parameters-explained)
* [Async patterns and polling](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/async-patterns-and-polling)
{% endcolumn %}

{% column %}
### <i class="fa-robot">:robot:</i> Connectors & MCP

Use Gamma from AI assistants. The Claude Connector and Gamma MCP Server let you generate content through natural conversation.

* [Connectors and Integrations](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/connectors-and-integrations)
* [Gamma MCP Server](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/gamma-mcp-server)
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
### <i class="fa-wand-magic-sparkles">:wand-magic-sparkles:</i> No-Code Automation

Connect Gamma to Zapier, Make, or n8n. Trigger content generation from forms, CRMs, spreadsheets, and hundreds of other apps — no code required.

* [Zapier, Make, and n8n setup](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/connectors-and-integrations)
{% endcolumn %}

{% column %}
### <i class="fa-key">:key:</i> Get Access

API access is available on Pro, Ultra, Teams, and Business plans. Generate your API key and start building.

* [Access and pricing](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/access-and-pricing)
* [Get help](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/get-help)
{% endcolumn %}
{% endcolumns %}

## What you can build

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4><i class="fa-bolt">:bolt:</i> Generate from text</h4></td><td>Send text, get a polished gamma. Control format, tone, audience, card count, and language.</td><td><a href="https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/generate-api-parameters-explained">Generate API parameters</a></td></tr><tr><td><h4><i class="fa-layer-group">:layer-group:</i> Generate from template</h4></td><td>Design a template in the app, then generate new content into the same layout via API.</td><td><a href="https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/create-from-template-api-parameters-explained">Create from Template</a></td></tr><tr><td><h4><i class="fa-palette">:palette:</i> Apply brand themes</h4></td><td>List workspace themes and lock every generation to your brand colors, fonts, and logo.</td><td><a href="https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/list-themes-and-list-folders-apis-explained">Themes and Folders APIs</a></td></tr><tr><td><h4><i class="fa-file-export">:file-export:</i> Export to PDF, PPTX, PNG</h4></td><td>Auto-export on generation complete. Download the file from the export URL in the status response.</td><td><a href="https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/async-patterns-and-polling">Async patterns and polling</a></td></tr><tr><td><h4><i class="fa-table-columns">:table-columns:</i> Custom headers & footers</h4></td><td>Place logos, page numbers, and text in 6 positions per card. Use your theme logo or a custom image URL.</td><td><a href="https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/header-and-footer-formatting">Header and footer formatting</a></td></tr><tr><td><h4><i class="fa-share-nodes">:share-nodes:</i> Set sharing & permissions</h4></td><td>Control workspace access, external link permissions, and email directly to recipients — all in the same API call.</td><td><a href="https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/generate-api-parameters-explained">Generate API parameters</a></td></tr></tbody></table>

## What's new

{% updates format="full" %}
{% update date="2025-02-18" %}
## Claude Connector

Create gammas directly from Claude conversations. The Gamma Connector is available in Claude's connector library — connect your account and generate presentations, documents, and more through natural language.

[Set up the Claude Connector →](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/connectors-and-integrations)
{% endupdate %}

{% update date="2025-02-10" %}
## Gamma MCP Server

Gamma MCP gives AI tools the ability to create gammas on your behalf. It powers the Claude Connector and is available for custom integrations via OAuth with Dynamic Client Registration.

[Learn about Gamma MCP →](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/gamma-mcp-server)
{% endupdate %}

{% update date="2025-01-15" %}
## n8n Native Node

The official Gamma node for n8n is live. Generate content, list themes and folders, and poll for results — all with a native node instead of raw HTTP requests.

[See the n8n integration →](https://app.gitbook.com/s/upsTVd2JbSOFZRBjfqED/overview/connectors-and-integrations)
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
