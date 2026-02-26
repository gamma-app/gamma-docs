---
description: Connect Gamma to your favorite AI tools and automation platforms.
---

# Connectors and Integrations

Gamma integrates with popular AI assistants and automation platforms so you can create presentations, documents, webpages, and social posts from the tools you already use.

{% tabs %}
{% tab title="Claude" %}
## Claude Connector

Create gammas directly from Claude conversations using the Gamma Connector.

{% stepper %}
{% step %}
### Open Claude

Go to [Claude](https://claude.ai) (web or desktop app).
{% endstep %}

{% step %}
### Find Connectors

Go to **Settings** → **Connectors**.
{% endstep %}

{% step %}
### Add Gamma

Click **Browse Connectors** and search for "Gamma."
{% endstep %}

{% step %}
### Connect

Click **Connect**, then click **Allow** to grant access to your Gamma account. Choose the right workspace if applicable.
{% endstep %}
{% endstepper %}

Once connected, you can ask Claude to create presentations, documents, and more — all generated in Gamma.

{% hint style="info" %}
**Example prompt:** "Create a 10-slide marketing strategy presentation covering target audience, campaign channels, budget breakdown, and success metrics. Use a professional theme."
{% endhint %}
{% endtab %}

{% tab title="Zapier" %}
## Zapier Integration

Automate Gamma content creation as part of your Zapier workflows.

* **Integration page**: [Gamma on Zapier](https://zapier.com/apps/gamma/integrations)

### What you can do

* Trigger a Gamma generation when a new row is added to Google Sheets
* Create a presentation whenever a deal closes in your CRM
* Generate reports from form submissions

### Getting started

1. In your Zapier workflow, search for **Gamma** in the app directory.
2. Select the Gamma action you want to use (e.g., "Generate a Gamma").
3. Authenticate with your Gamma API key.
4. Map your trigger data to the Gamma generation parameters.

{% hint style="info" %}
Your Gamma API key is required. Generate one from your [account settings](https://gamma.app/settings).
{% endhint %}
{% endtab %}

{% tab title="Make" %}
## Make Integration

Build visual automation workflows that include Gamma content creation.

* **Integration page**: [Gamma on Make](https://www.make.com/en/integrations/gamma-app)

### What you can do

* Generate branded presentations from CRM data
* Create documents from email content or form responses
* Build multi-step workflows combining Gamma with hundreds of other apps

### Getting started

1. In your Make scenario, add a new module and search for **Gamma**.
2. Select the action you want (e.g., "Create a Generation").
3. Connect your Gamma account using your API key.
4. Configure the module with your desired parameters.

{% hint style="info" %}
Your Gamma API key is required. Generate one from your [account settings](https://gamma.app/settings).
{% endhint %}
{% endtab %}

{% tab title="n8n" %}
## n8n Integration

Use Gamma in your self-hosted or cloud n8n automation workflows.

* **Integration page**: [Gamma on n8n](https://n8n.io/integrations/gamma/)

### What you can do

* Automate presentation creation from any of n8n's 400+ integrations
* Pull data from CRMs, databases, and APIs into Gamma-generated content
* Build end-to-end pipelines: data ingestion → content generation → distribution

### Getting started

1. Add an **HTTP Request** node to your n8n workflow.
2. Configure it as a POST request to `https://public-api.gamma.app/v1.0/generations`.
3. Add your API key in the headers: `X-API-KEY: your-api-key`.
4. Set the request body with your generation parameters.
5. Add a second HTTP Request node to poll `GET /v1.0/generations/{id}` for the result.

For a detailed walkthrough, see our [async patterns and polling guide](async-patterns-and-polling.md).

{% hint style="info" %}
Your Gamma API key is required. Generate one from your [account settings](https://gamma.app/settings).
{% endhint %}
{% endtab %}

{% tab title="Other Platforms" %}
## Other Platforms

Gamma's REST API works with any automation platform or custom application that can make HTTP requests.

### Supported platforms include

* **Workato** — Enterprise automation
* **Pipedream** — Developer-first workflows
* **Power Automate** — Microsoft ecosystem automation
* **Custom applications** — Any backend that can call REST APIs

### Getting started

All platforms follow the same pattern:

1. Make a **POST** request to `https://public-api.gamma.app/v1.0/generations` with your content and parameters.
2. Include your API key in the `X-API-KEY` header.
3. **Poll** the status endpoint until generation is complete.
4. Retrieve the Gamma URL and optional export URL from the response.

See the [Generate API parameters guide](generate-api-parameters-explained.md) for the full list of available options.

{% hint style="warning" %}
**Server-side only.** The Gamma API must be called from a backend server, not from browser-side JavaScript.
{% endhint %}
{% endtab %}
{% endtabs %}

## Which integration method is right for you?

| You want to... | Use |
| --- | --- |
| Create gammas through conversation with an AI assistant | [Claude Connector](#claude-connector) |
| Automate Gamma as part of a no-code workflow | [Zapier](#zapier-integration), [Make](#make-integration), or [n8n](#n8n-integration) |
| Build a custom integration with an AI tool via MCP | [Gamma MCP Server](gamma-mcp-server.md) |
| Build a custom app with full programmatic control | [Gamma API](generate-api-parameters-explained.md) |
