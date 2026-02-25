---
description: Gamma MCP powers Gamma Connectors and integrations in popular AI tools.
---

# Gamma MCP Server

## What is Gamma MCP?

Gamma MCP is our hosted server that gives AI tools the ability to create gammas on your behalf. It's designed to work seamlessly with popular AI assistants — for example, Gamma integrations in tools like Claude are powered by our MCP server.

## What can I do with Gamma MCP?

When you connect Gamma MCP, your AI assistant gains access to three core tools:

### 1. Generate content in Gamma

Create new presentations, documents, webpages, or social media posts with extensive customization options:

* **Content formats**: Presentations, documents, webpages, social posts
* **Text control**: Choose text density, tone, audience, and language
* **Image options**: AI-generated images, web images, Pictographic, GIFs, placeholders, or no images
* **Theme selection**: Apply Gamma's theme library to match your desired aesthetic
* **Layout options**: Set aspect ratios (16:9, 4:3, letter, A4, and more), configure headers/footers
* **Organization**: Save to specific folders in your workspace
* **Export**: Generate PowerPoint (PPTX) or PDF versions
* **Sharing**: Set workspace and external access permissions

### 2. Browse themes

Search and select from Gamma's theme library by name. Each theme includes tone and color keywords to help match your desired style (e.g., "professional", "colorful", "minimal", "modern"). You can [create new themes](https://help.gamma.app/en/articles/11029150-can-i-add-my-own-colors-and-fonts-to-gamma) in Gamma to match your brand's look and feel.

### 3. Organize to folders

Browse your Gamma folders or search for specific folders by name and organize your created gammas accordingly.

## Getting started

### Requirements

To use a Gamma Connector, you'll need:

* An AI tool with a Gamma Connector available in its Connectors or Agents library.
* A Gamma account (any plan works, but a paying plan is recommended for best results).

### How to connect

The setup process varies depending on which AI tool you're using. See the [Connectors and Integrations](connectors-and-integrations.md) page for step-by-step instructions for each supported platform.

## Tips for best results

**Be specific about structure and content.** The more detail you provide, the better the output. Instead of "make a presentation about marketing," try "create a 10-slide marketing strategy presentation covering target audience, campaign channels, budget breakdown, and success metrics."

**Describe your desired style.** Mention visual preferences upfront: "professional and minimal," "colorful and creative," "corporate and clean." Gamma has themes to match various aesthetics. You can also create and specify a theme to match your brand.

**Specify the format.** Clarify whether you want a presentation, document, webpage, or social post.

**Control text density.** Tell the AI how much text you want: "keep slides brief with bullet points" or "include detailed explanations in each section." Options range from brief to extensive.

**Organize as you go.** Mention folder names if you want content saved to specific places: "Create this presentation and save it to my Marketing folder."

**Export when needed.** If you need to share outside of Gamma, specify the format: "Export this as a PowerPoint file" or "Generate a PDF version."

## Request custom MCP access

{% hint style="info" %}
**Building your own integration?** If you'd like to connect Gamma MCP to your own platform, you can request access below.

The Gamma MCP server uses OAuth with Dynamic Client Registration (DCR). Your platform must support DCR to connect. If you're unsure, check with your engineering team before submitting.
{% endhint %}

<a href="https://docs.google.com/forms/d/e/1FAIpQLSfYourFormIdHere/viewform" class="button primary">Request MCP Access</a>

The form will ask for:

* Your name, email, and company
* A description of your use case
* Your OAuth redirect URIs (e.g., `https://yourapp.com/oauth/callback`)
* A logo for the OAuth consent page (SVG, PNG, or JPEG — 256x256 px)

## Troubleshooting

<details>
<summary>Authentication errors</summary>

Your connection to Gamma may have expired. Disconnect and reconnect the Gamma connector in your AI assistant to refresh your authentication.
</details>

<details>
<summary>Connection problems</summary>

Make sure you're logged into both your AI assistant and your Gamma account in your browser before connecting. If you continue to have issues, check your network connection.
</details>

<details>
<summary>Insufficient credits</summary>

Your Gamma account doesn't have enough credits to complete the generation. You can purchase more credits in your [Gamma account settings](https://gamma.app/settings/billing) or upgrade to a higher tier.
</details>

<details>
<summary>Invalid parameters</summary>

If your AI assistant reports an error about invalid parameters, it will typically retry automatically with corrected values. If the issue persists, try rephrasing your request with simpler or more standard options.
</details>

## FAQ

<details>
<summary>Connectors, MCP, and API — which should I use?</summary>

**For no-code users:**

* Gamma connectors in AI tools like Claude let you create presentations through natural conversation.
* Automation platforms (Zapier, Make, n8n) let you connect Gamma to other apps and automate workflows — like generating a presentation from new Google Docs or Slack messages.

**For developers and advanced users:**

* **Use Gamma MCP** if you're building a custom integration between Gamma and an AI tool that supports the Model Context Protocol.
* **Use Gamma API** if you're building a custom application, automation, or integration that needs programmatic access to Gamma's content creation capabilities. The API gives you full control over requests, responses, and error handling. Learn more about the [Gamma API](understanding-the-api-options.md).
</details>

<details>
<summary>Can I edit my gamma using the MCP?</summary>

We do not support editing via MCP or API today. You cannot edit gammas directly from a different AI tool. We recommend editing your gamma via the [Gamma application](https://gamma.app).
</details>

<details>
<summary>What requests can I make with Gamma MCP?</summary>

The Gamma MCP capabilities mirror those of our Generate API. You can read about all available parameters in the [Generate API parameters](generate-api-parameters-explained.md) guide.
</details>

<details>
<summary>I want to learn more about Model Context Protocol (MCP).</summary>

Visit the [Model Context Protocol website](https://modelcontextprotocol.io/) for technical details about how MCP servers work.
</details>
