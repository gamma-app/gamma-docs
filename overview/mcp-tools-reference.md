---
description: >-
  Authentication, tools, parameters, and error handling for the Gamma MCP
  server.
layout:
  width: default
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
  metadata:
    visible: true
  tags:
    visible: true
---

# MCP tools reference

Complete reference for the Gamma MCP server's authentication, available tools, input parameters, and error handling.

## Quick reference

* All requests require an OAuth 2.0 Bearer token.
* Three tools: `generate`, `get_themes`, `get_folders`.
* OAuth discovery via RFC 9728 at `/.well-known/oauth-protected-resource`.
* Dynamic Client Registration supported via RFC 7591.
* Errors return `{ "error": "...", "isError": true }`.

## Authentication

The Gamma MCP server uses OAuth 2.0. Every request must include a valid Bearer token.

### Authorization header

Include your token with each request:

```
Authorization: Bearer <your-oauth-token>
```

### OAuth discovery

The server implements [RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728) (OAuth Protected Resource Metadata). Clients retrieve OAuth configuration at:

```
GET /.well-known/oauth-protected-resource
```

### Dynamic client registration

The authorization server supports [RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591) Dynamic Client Registration. Discover the registration endpoint URL from the authorization server metadata obtained via the OAuth discovery endpoint above.

### Authentication errors

A failed authentication returns `401 Unauthorized` with a `WWW-Authenticate` header:

```
WWW-Authenticate: Bearer resource_metadata="https://<server>/.well-known/oauth-protected-resource"
```

Use the `resource_metadata` URI to discover the authorization server and initiate the OAuth flow.

## Tools overview

<table data-full-width="true"><thead><tr><th>Tool</th><th>Description</th><th>Read-only</th><th>Destructive</th><th>Idempotent</th></tr></thead><tbody><tr><td><code>generate</code></td><td>Create presentations, documents, webpages, or social posts</td><td>No</td><td>No</td><td>No</td></tr><tr><td><code>get_themes</code></td><td>Browse or search the Gamma theme library</td><td>Yes</td><td>No</td><td>Yes</td></tr><tr><td><code>get_folders</code></td><td>Browse or search your Gamma folders</td><td>Yes</td><td>No</td><td>Yes</td></tr></tbody></table>

## generate

Create a new presentation, document, webpage, or social media post. Ask the user clarifying questions about text mode, length, tone, and audience when needed.

Each call creates new content — the tool is not idempotent.

### Input parameters

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>inputText</code></td><td><code>string</code></td><td>Yes</td><td>Content to generate from — a text prompt, outline, or full content</td></tr><tr><td><code>textMode</code></td><td><code>enum</code></td><td>No</td><td>How to handle input text: <code>generate</code> (new content from brief prompt), <code>condense</code> (summarize existing content), <code>preserve</code> (use content as-is)</td></tr><tr><td><code>format</code></td><td><code>enum</code></td><td>No</td><td>Output type: <code>presentation</code>, <code>document</code>, <code>social</code>, <code>webpage</code></td></tr><tr><td><code>numCards</code></td><td><code>int</code></td><td>No</td><td>Number of slides, cards, or pages to generate</td></tr><tr><td><code>themeId</code></td><td><code>string</code></td><td>No</td><td>Theme ID from <code>get_themes</code></td></tr><tr><td><code>folderIds</code></td><td><code>array[string]</code></td><td>No</td><td>Folder IDs from <code>get_folders</code> to organize the content</td></tr><tr><td><code>additionalInstructions</code></td><td><code>string</code></td><td>No</td><td>Extra guidance for the AI generator not covered by other parameters</td></tr><tr><td><code>exportAs</code></td><td><code>enum</code></td><td>No</td><td>Export format: <code>pptx</code> or <code>pdf</code> (only when the user explicitly requests export)</td></tr></tbody></table>

### Text options

Optional `textOptions` object for controlling text generation.

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>textOptions.amount</code></td><td><code>enum</code></td><td>No</td><td>Text density per slide or section: <code>brief</code>, <code>medium</code>, <code>detailed</code>, <code>extensive</code></td></tr><tr><td><code>textOptions.tone</code></td><td><code>string</code></td><td>No</td><td>Writing tone (e.g., <code>professional</code>, <code>casual</code>)</td></tr><tr><td><code>textOptions.audience</code></td><td><code>string</code></td><td>No</td><td>Target audience (e.g., <code>executives</code>, <code>students</code>)</td></tr><tr><td><code>textOptions.language</code></td><td><code>string</code></td><td>No</td><td>Language code (e.g., <code>en</code>, <code>es</code>, <code>fr</code>)</td></tr></tbody></table>

### Image options

Optional `imageOptions` object for controlling image sourcing.

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>imageOptions.source</code></td><td><code>enum</code></td><td>No</td><td>Image source: <code>aiGenerated</code>, <code>webAllImages</code>, <code>webFreeToUse</code>, <code>webFreeToUseCommercially</code>, <code>pictographic</code>, <code>giphy</code>, <code>unsplash</code>, <code>placeholder</code>, <code>noImages</code></td></tr><tr><td><code>imageOptions.model</code></td><td><code>string</code></td><td>No</td><td>AI image model. Use only when <code>source</code> is <code>aiGenerated</code>.</td></tr><tr><td><code>imageOptions.style</code></td><td><code>string</code></td><td>No</td><td>AI image style, for example <code>photorealistic</code> or <code>illustration</code></td></tr></tbody></table>

### Card options

Optional `cardOptions` object for layout and header/footer configuration.

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>cardOptions.dimensions</code></td><td><code>enum</code></td><td>No</td><td>Aspect ratio or page size: <code>16x9</code>, <code>4x3</code>, <code>fluid</code>, <code>letter</code>, <code>a4</code>, <code>pageless</code>, <code>1x1</code>, <code>4x5</code>, <code>9x16</code></td></tr><tr><td><code>cardOptions.headerFooter</code></td><td><code>object</code></td><td>No</td><td>Header and footer configuration. Use only when explicitly requested.</td></tr></tbody></table>

**Header/footer object**

The `headerFooter` object contains six slot positions and two visibility flags.

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>headerFooter.topLeft</code></td><td><code>object</code></td><td>No</td><td>Top-left header slot</td></tr><tr><td><code>headerFooter.topCenter</code></td><td><code>object</code></td><td>No</td><td>Top-center header slot</td></tr><tr><td><code>headerFooter.topRight</code></td><td><code>object</code></td><td>No</td><td>Top-right header slot</td></tr><tr><td><code>headerFooter.bottomLeft</code></td><td><code>object</code></td><td>No</td><td>Bottom-left footer slot</td></tr><tr><td><code>headerFooter.bottomCenter</code></td><td><code>object</code></td><td>No</td><td>Bottom-center footer slot</td></tr><tr><td><code>headerFooter.bottomRight</code></td><td><code>object</code></td><td>No</td><td>Bottom-right footer slot</td></tr><tr><td><code>headerFooter.hideFromFirstCard</code></td><td><code>boolean</code></td><td>No</td><td>Hide header or footer on the first card</td></tr><tr><td><code>headerFooter.hideFromLastCard</code></td><td><code>boolean</code></td><td>No</td><td>Hide header or footer on the last card</td></tr></tbody></table>

**Slot configuration**

Each slot object (`topLeft`, `topCenter`, etc.) accepts:

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>type</code></td><td><code>enum</code></td><td>Yes</td><td>Content type: <code>cardNumber</code>, <code>image</code>, or <code>text</code></td></tr><tr><td><code>source</code></td><td><code>enum</code></td><td>No</td><td>Image source. Required when <code>type</code> is <code>image</code>: <code>themeLogo</code> or <code>custom</code>.</td></tr><tr><td><code>src</code></td><td><code>string</code></td><td>No</td><td>Image URL. Required when <code>type</code> is <code>image</code> and <code>source</code> is <code>custom</code>.</td></tr><tr><td><code>value</code></td><td><code>string</code></td><td>No</td><td>Text content. Required when <code>type</code> is <code>text</code>.</td></tr><tr><td><code>size</code></td><td><code>enum</code></td><td>No</td><td>Image size: <code>sm</code>, <code>md</code>, <code>lg</code>, or <code>xl</code></td></tr></tbody></table>

### Sharing options

Optional `sharingOptions` object for controlling access after generation.

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>sharingOptions.workspaceAccess</code></td><td><code>enum</code></td><td>No</td><td>Workspace member access: <code>edit</code>, <code>comment</code>, <code>view</code>, <code>noAccess</code>, or <code>fullAccess</code></td></tr><tr><td><code>sharingOptions.externalAccess</code></td><td><code>enum</code></td><td>No</td><td>External user access: <code>edit</code>, <code>comment</code>, <code>view</code>, or <code>noAccess</code></td></tr><tr><td><code>sharingOptions.emailOptions</code></td><td><code>object</code></td><td>No</td><td>Share by email with specific recipients</td></tr><tr><td><code>sharingOptions.emailOptions.recipients</code></td><td><code>array[string]</code></td><td>Yes</td><td>Email addresses to share with</td></tr><tr><td><code>sharingOptions.emailOptions.access</code></td><td><code>enum</code></td><td>Yes</td><td>Recipient access: <code>edit</code>, <code>comment</code>, <code>view</code>, or <code>fullAccess</code></td></tr></tbody></table>

### Output

<table data-full-width="true"><thead><tr><th>Field</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>generationId</code></td><td><code>string</code></td><td>Unique ID for the generation</td></tr><tr><td><code>status</code></td><td><code>enum</code></td><td>Generation status: <code>completed</code> or <code>failed</code></td></tr><tr><td><code>gammaUrl</code></td><td><code>string</code></td><td>Created content URL when <code>status</code> is <code>completed</code></td></tr><tr><td><code>exportUrl</code></td><td><code>string</code></td><td>Export download URL when <code>exportAs</code> was specified</td></tr><tr><td><code>credits.deducted</code></td><td><code>int</code></td><td>Credits deducted for this generation</td></tr><tr><td><code>credits.remaining</code></td><td><code>int</code></td><td>Credits remaining after generation</td></tr><tr><td><code>error</code></td><td><code>string</code></td><td>Error message when <code>status</code> is <code>failed</code></td></tr></tbody></table>

## get\_themes

Browse or search the Gamma theme library. Use the returned `id` in the `generate` tool's `themeId` parameter.

If the user references a theme by name, search by name. Otherwise, fetch the full list and choose based on tone and color keywords.

### Input parameters

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code></td><td><code>string</code></td><td>No</td><td>Search themes by name. Use only when the user references a specific theme.</td></tr></tbody></table>

### Output

<table data-full-width="true"><thead><tr><th>Field</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>themes</code></td><td><code>array[object]</code></td><td>Array of theme objects</td></tr><tr><td><code>themes[].id</code></td><td><code>string</code></td><td>Theme ID to pass to <code>generate</code></td></tr><tr><td><code>themes[].name</code></td><td><code>string</code></td><td>Display name</td></tr><tr><td><code>themes[].type</code></td><td><code>enum</code></td><td><code>standard</code> or <code>custom</code></td></tr><tr><td><code>themes[].colorKeywords</code></td><td><code>array[string]</code></td><td>Color keywords describing the palette</td></tr><tr><td><code>themes[].toneKeywords</code></td><td><code>array[string]</code></td><td>Tone keywords describing the style</td></tr><tr><td><code>count</code></td><td><code>int</code></td><td>Total themes returned</td></tr></tbody></table>

## get\_folders

Browse or search your Gamma folders. Use the returned `id` in the `generate` tool's `folderIds` parameter.

### Input parameters

<table data-full-width="true"><thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>name</code></td><td><code>string</code></td><td>No</td><td>Search folders by name. Omit it to return all folders.</td></tr></tbody></table>

### Output

<table data-full-width="true"><thead><tr><th>Field</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>folders</code></td><td><code>array[object]</code></td><td>Array of folder objects</td></tr><tr><td><code>folders[].id</code></td><td><code>string</code></td><td>Folder ID to pass to <code>generate</code></td></tr><tr><td><code>folders[].name</code></td><td><code>string</code></td><td>Display name</td></tr><tr><td><code>count</code></td><td><code>int</code></td><td>Total folders returned</td></tr></tbody></table>

## Error handling

All tools return errors in a consistent format:

{% code title="Error response" %}
```json
{
  "error": "Error message describing what went wrong",
  "isError": true
}
```
{% endcode %}

<table data-full-width="true"><thead><tr><th>Error</th><th>Description</th></tr></thead><tbody><tr><td><code>401 Unauthorized</code></td><td>Missing or invalid OAuth Bearer token. See [Authentication errors](#authentication-errors).</td></tr><tr><td>Invalid parameter values</td><td>One or more parameters do not match the expected format or values</td></tr><tr><td>Rate limit exceeded</td><td>Too many requests in a given time period</td></tr><tr><td>Network connectivity</td><td>Unable to establish a connection to the server</td></tr><tr><td>Insufficient credits</td><td>Account does not have enough credits to complete the generation</td></tr></tbody></table>

## Related

* [Set up the MCP server](gamma-mcp-server.md) for getting started and troubleshooting
* [Connect integrations](connectors-and-integrations.md) for platform-specific setup
* [Generate from text](generate-api-parameters-explained.md) for the equivalent REST API parameters
* [Access and pricing](access-and-pricing.md) for credit costs and plan details
