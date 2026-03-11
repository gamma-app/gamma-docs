---
description: Gamma MCP powers Gamma Connectors and integrations in popular AI tools.
---

# Set up the MCP server

Gamma MCP is a hosted server that gives AI tools the ability to create gammas on your behalf. Integrations like the Gamma connectors in Claude and ChatGPT are powered by this server.

### Quick reference

- Works with any AI tool that supports the Model Context Protocol.
- Available on all Gamma plans. Generations charge credits.
- Three capabilities: generate content, browse themes, organize to folders.
- Uses OAuth with Dynamic Client Registration for custom integrations.

### Capabilities

**Generate content** -- create presentations, documents, webpages, or social posts with control over text density, tone, audience, language, images, themes, layout, headers/footers, export format, and sharing permissions.

**Browse themes** -- search Gamma's theme library by name. Each theme includes tone and color keywords to help match your style.

**Organize to folders** -- browse or search your Gamma folders and save generated content to specific locations.

### Getting started

To use a Gamma Connector, you need an AI tool with a Gamma Connector in its library and a Gamma account on any plan. The setup process varies by platform -- see [Connect integrations](connectors-and-integrations.md) for step-by-step instructions.

### Tips for best results

- Be specific about structure: "create a 10-slide marketing strategy covering target audience, channels, budget, and metrics" works better than "make a presentation about marketing."
- Describe your style upfront: "professional and minimal," "colorful and creative," "corporate and clean."
- Specify the format: presentation, document, webpage, or social post.
- Control text density: "keep slides brief with bullet points" or "include detailed explanations."
- Mention folder names if you want content organized: "save to my Marketing folder."
- Request exports when needed: "export as PowerPoint" or "generate a PDF."

### Request custom MCP access

{% hint style="info" %}
**Building your own integration?** The Gamma MCP server uses OAuth with Dynamic Client Registration (DCR). Your platform must support DCR to connect.
{% endhint %}

<a href="https://docs.google.com/forms/d/1y5EJFP8pbl2-0PfTQexcs5vsvWpnPj3Q9bKOaH_4wuE/viewform" class="button primary">Request MCP Access</a>

The form asks for your name, email, company, use case description, OAuth redirect URIs, and a logo for the consent page (SVG, PNG, or JPEG, 256x256 px).

### Troubleshooting

<details>
<summary>Authentication errors</summary>

Your connection to Gamma may have expired. Disconnect and reconnect the Gamma connector in your AI assistant to refresh authentication.
</details>

<details>
<summary>Connection problems</summary>

Make sure you're logged into both your AI assistant and your Gamma account before connecting. If issues persist, check your network connection.
</details>

<details>
<summary>Insufficient credits</summary>

Your account doesn't have enough credits. Purchase more at [Settings > Billing](https://gamma.app/settings/billing) or upgrade your plan.
</details>

<details>
<summary>Invalid parameters</summary>

Your AI assistant will typically retry with corrected values. If the issue persists, try rephrasing your request with simpler options.
</details>

### FAQ

<details>
<summary>Connectors, MCP, and API -- which should I use?</summary>

**No-code users:** Use Gamma connectors in Claude or ChatGPT for conversational creation, or Zapier/Make/n8n for automated workflows.

**Developers:** Use Gamma MCP if you're building a custom AI tool integration that supports MCP. Use the [Gamma API](understanding-the-api-options.md) if you need full programmatic control over requests and responses.
</details>

<details>
<summary>Can I edit a gamma using MCP?</summary>

Not today. Editing is only available in the [Gamma app](https://gamma.app).
</details>

<details>
<summary>What can I request through Gamma MCP?</summary>

The same capabilities as the Generate API. See the [Generate API parameters](generate-api-parameters-explained.md) guide for the full list.
</details>

<details>
<summary>Where can I learn more about MCP?</summary>

Visit the [Model Context Protocol website](https://modelcontextprotocol.io/) for technical details.
</details>

### Related

- [Connect integrations](connectors-and-integrations.md) for platform-specific setup instructions
- [Generate from text](generate-api-parameters-explained.md) for the full parameter reference
- [Access and Pricing](access-and-pricing.md) for credit costs and plan details
