---
description: Gamma MCP powers Gamma Connectors and integrations in popular AI tools.
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

# Set up the MCP server

Gamma MCP is a hosted server that lets AI tools create new gammas and read existing Gamma presentations or documents on your behalf. Integrations like the Gamma connectors in Claude and ChatGPT are powered by this server.

### Quick reference

- Works with any AI tool that supports the Model Context Protocol.
- Available on all Gamma plans. Generations charge credits.
- Four capabilities: generate content, read existing gammas, browse themes, organize to folders.
- Reading requires view access to the Gamma in the connected workspace.
- Uses OAuth with Dynamic Client Registration for custom integrations.
- See [MCP tools reference](mcp-tools-reference.md) for full parameter tables and authentication details.

### Capabilities

**Generate content** -- create presentations, documents, webpages, or social posts with control over text density, tone, audience, language, images, themes, layout, headers/footers, export format, and sharing permissions.

**Read existing gammas** -- retrieve the full content of a presentation or document when you provide a Gamma file ID or URL. This tool is read-only and cannot modify the Gamma.

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

Connected apps request permission to create gammas, read gammas, list folders, and list themes in the selected workspace.

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

You can create new content with the same generation controls as the Generate API, browse themes, browse folders, and read existing Gamma presentations or documents with `read_gamma`. See the [MCP tools reference](mcp-tools-reference.md) for the full tool list and parameter details.
</details>

<details>
<summary>Where can I learn more about MCP?</summary>

Visit the [Model Context Protocol website](https://modelcontextprotocol.io/) for technical details.
</details>

### Related

- [MCP tools reference](mcp-tools-reference.md) for authentication, parameter tables, and error handling
- [Connect integrations](connectors-and-integrations.md) for platform-specific setup instructions
- [Generate from text](generate-api-parameters-explained.md) for the full parameter reference
- [Access and pricing](access-and-pricing.md) for credit costs and plan details
