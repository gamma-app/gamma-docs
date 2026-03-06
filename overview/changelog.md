---
description: Release history for the Gamma Public API, MCP Server, and integrations.
icon: clock-rotate-left
---

# Changelog

{% updates format="full" %}
{% update date="2026-03-06" %}
## OpenAPI spec and image model metadata

* Published **OpenAPI spec** (`openapi.yaml`) with clean schema names, standalone `ImageModel` enum, and per-model plan/credit metadata
* OpenAPI spec is now auto-generated from the codebase — no manual maintenance required

{% endupdate %}

{% update date="2026-02-27" %}
## Create from Template GA, new models, and more

* **Create from Template** is now generally available — no longer gated by a feature flag
* New `imageOptions.stylePreset` parameter — choose from `photorealistic`, `illustration`, `abstract`, `3D`, `lineArt`, or `custom`
* **Export as PNG** — `exportAs` now accepts `png` in addition to `pptx` and `pdf`
* `GET /v1.0/generations/{id}` now returns `gammaId` (the file ID) for completed generations
* **Card margin images** — `<top-left type="image" src="..." />` supported in head-tag XML for create-from-template
* New image models: `recraft-v4`, `recraft-v4-svg`, `recraft-v4-pro`, `gemini-3.1-flash-image-mini`, `gemini-3.1-flash-image`, `gemini-3.1-flash-image-hd`, `flux-2-max`, `flux-2-klein`

{% endupdate %}

{% update date="2026-01-16" %}
## v0.2 API removed

* v0.2 synchronous endpoints (`POST /v0.2/generations`, `POST /v0.2/generations/sync`) have been disabled
* All integrations must use the v1.0 async flow (`POST /v1.0/generations` + polling)

{% endupdate %}

{% update date="2025-11-05" %}
## Generate API GA, Create from Template, and more

The Generate API moves from beta to v1.0. Existing v0.2 integrations should migrate to the new endpoints.

* **Create from Template** API now in beta — design a template in Gamma, generate new content into the same layout via API
* Generate **webpages** as a new output format
* Define **headers and footers** with text, images, and card numbers in six positions
* Include **image URLs** directly in input text
* Assign generated gammas to **folders** and **share via email**
* New **List Themes** and **List Folders** endpoints
* Official **Make.com** integration
* Removed hard generation limits — contact support if rate-limited

{% endupdate %}

{% update date="2025-10-01" %}
## Higher usage and credit recharges

* Generation cap increased from 50/day to **50/hour**
* Credits can now be purchased on demand or via **auto-recharge**
* API-generated gammas appear in a **separate tab** in the Gamma dashboard

{% endupdate %}

{% update date="2025-09-15" %}
## Credits-based pricing and new models

* Usage cap: **50 generations per user per day**
* **Ultra** tier unlocks more powerful image models and up to **75 cards** per gamma
* Introduction of **credits-based pricing**
* **Zapier** integration available

{% endupdate %}

{% update date="2025-07-28" %}
## Beta release

* `POST /v1.0/generations` and `GET /v1.0/generations/{id}` endpoints launched in beta
* Generate presentations and documents programmatically for the first time

{% endupdate %}

{% update date="2025-02-18" %}
## Claude Connector

Create gammas directly from Claude conversations using the Gamma Connector.

[Set up the Claude Connector →](connectors-and-integrations.md)

{% endupdate %}

{% update date="2025-02-10" %}
## Gamma MCP Server

Give AI tools the ability to create gammas on your behalf via OAuth with Dynamic Client Registration.

[Learn about Gamma MCP →](gamma-mcp-server.md)

{% endupdate %}

{% update date="2025-01-15" %}
## n8n Native Node

Generate content, list themes and folders, and poll for results with a native Gamma node in n8n.

[See the n8n integration →](connectors-and-integrations.md)

{% endupdate %}
{% endupdates %}
