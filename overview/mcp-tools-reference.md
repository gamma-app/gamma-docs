---
description: Authentication, tools, parameters, and error handling for the Gamma MCP server.
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

# MCP tools reference

Complete reference for the Gamma MCP server's authentication, available tools, input parameters, and error handling.

## Quick reference

- All requests require an OAuth 2.0 Bearer token.
- Three tools: `generate`, `get_themes`, `get_folders`.
- OAuth discovery via RFC 9728 at `/.well-known/oauth-protected-resource`.
- Dynamic Client Registration supported via RFC 7591.
- Errors return `{ "error": "...", "isError": true }`.

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

| Tool | Description | Read-only | Destructive | Idempotent |
| --- | --- | --- | --- | --- |
| `generate` | Create presentations, documents, webpages, or social posts | No | No | No |
| `get_themes` | Browse or search the Gamma theme library | Yes | No | Yes |
| `get_folders` | Browse or search your Gamma folders | Yes | No | Yes |

## generate

Create a new presentation, document, webpage, or social media post. Ask the user clarifying questions about text mode, length, tone, and audience when needed.

Each call creates new content — the tool is not idempotent.

### Input parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `inputText` | `string` | Yes | Content to generate from — a text prompt, outline, or full content |
| `textMode` | `enum` | No | How to handle input text: `generate` (new content from brief prompt), `condense` (summarize existing content), `preserve` (use content as-is) |
| `format` | `enum` | No | Output type: `presentation`, `document`, `social`, `webpage` |
| `numCards` | `int` | No | Number of slides, cards, or pages to generate |
| `themeId` | `string` | No | Theme ID from `get_themes` |
| `folderIds` | `array[string]` | No | Folder IDs from `get_folders` to organize the content |
| `additionalInstructions` | `string` | No | Extra guidance for the AI generator not covered by other parameters |
| `exportAs` | `enum` | No | Export format: `pptx` or `pdf` (only when the user explicitly requests export) |

### Text options

Optional `textOptions` object for controlling text generation.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `textOptions.amount` | `enum` | No | Text density per slide or section: `brief`, `medium`, `detailed`, `extensive` |
| `textOptions.tone` | `string` | No | Writing tone (e.g., `professional`, `casual`) |
| `textOptions.audience` | `string` | No | Target audience (e.g., `executives`, `students`) |
| `textOptions.language` | `string` | No | Language code (e.g., `en`, `es`, `fr`) |

### Image options

Optional `imageOptions` object for controlling image sourcing.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `imageOptions.source` | `enum` | No | Image source: `aiGenerated`, `webAllImages`, `webFreeToUse`, `webFreeToUseCommercially`, `pictographic`, `giphy`, `unsplash`, `placeholder`, `noImages` |
| `imageOptions.model` | `string` | No | AI image model (only when `source` is `aiGenerated`) |
| `imageOptions.style` | `string` | No | Style for AI images (e.g., `photorealistic`, `illustration`) |

### Card options

Optional `cardOptions` object for layout and header/footer configuration.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `cardOptions.dimensions` | `enum` | No | Aspect ratio or page size: `16x9`, `4x3`, `fluid`, `letter`, `a4`, `pageless`, `1x1`, `4x5`, `9x16` |
| `cardOptions.headerFooter` | `object` | No | Header and footer configuration (only use if explicitly requested) |

**Header/footer object**

The `headerFooter` object contains six slot positions and two visibility flags.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `headerFooter.topLeft` | `object` | No | Top-left header slot |
| `headerFooter.topCenter` | `object` | No | Top-center header slot |
| `headerFooter.topRight` | `object` | No | Top-right header slot |
| `headerFooter.bottomLeft` | `object` | No | Bottom-left footer slot |
| `headerFooter.bottomCenter` | `object` | No | Bottom-center footer slot |
| `headerFooter.bottomRight` | `object` | No | Bottom-right footer slot |
| `headerFooter.hideFromFirstCard` | `boolean` | No | Hide header/footer from the first card |
| `headerFooter.hideFromLastCard` | `boolean` | No | Hide header/footer from the last card |

**Slot configuration**

Each slot object (`topLeft`, `topCenter`, etc.) accepts:

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `enum` | Yes | Content type: `cardNumber`, `image`, `text` |
| `source` | `enum` | No | Image source (required when `type` is `image`): `themeLogo`, `custom` |
| `src` | `string` | No | Image URL (required when `type` is `image` and `source` is `custom`) |
| `value` | `string` | No | Text content (required when `type` is `text`) |
| `size` | `enum` | No | Image size: `sm`, `md`, `lg`, `xl` |

### Sharing options

Optional `sharingOptions` object for controlling access after generation.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingOptions.workspaceAccess` | `enum` | No | Workspace member access: `edit`, `comment`, `view`, `noAccess`, `fullAccess` |
| `sharingOptions.externalAccess` | `enum` | No | External user access: `edit`, `comment`, `view`, `noAccess` |
| `sharingOptions.emailOptions` | `object` | No | Share via email to specific recipients |
| `sharingOptions.emailOptions.recipients` | `array[string]` | Yes | Email addresses to share with |
| `sharingOptions.emailOptions.access` | `enum` | Yes | Recipient access level: `edit`, `comment`, `view`, `fullAccess` |

### Output

| Field | Type | Description |
| --- | --- | --- |
| `generationId` | `string` | Unique ID for the generation |
| `status` | `enum` | Generation status: `completed` or `failed` |
| `gammaUrl` | `string` | URL to the created content (when `status` is `completed`) |
| `exportUrl` | `string` | Download URL for the export file (when `exportAs` was specified) |
| `credits.deducted` | `int` | Credits deducted for this generation |
| `credits.remaining` | `int` | Remaining credits after generation |
| `error` | `string` | Error message (when `status` is `failed`) |

## get\_themes

Browse or search the Gamma theme library. Use the returned `id` in the `generate` tool's `themeId` parameter.

If the user references a theme by name, search by name. Otherwise, fetch the full list and choose based on tone and color keywords.

### Input parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No | Search themes by name (only when the user references a specific theme name) |

### Output

| Field | Type | Description |
| --- | --- | --- |
| `themes` | `array[object]` | Array of theme objects |
| `themes[].id` | `string` | Theme ID to pass to `generate` |
| `themes[].name` | `string` | Display name |
| `themes[].type` | `enum` | `standard` or `custom` |
| `themes[].colorKeywords` | `array[string]` | Color keywords describing the palette |
| `themes[].toneKeywords` | `array[string]` | Tone keywords describing the style |
| `count` | `int` | Total themes returned |

## get\_folders

Browse or search your Gamma folders. Use the returned `id` in the `generate` tool's `folderIds` parameter.

### Input parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No | Search folders by name (omit to return all folders) |

### Output

| Field | Type | Description |
| --- | --- | --- |
| `folders` | `array[object]` | Array of folder objects |
| `folders[].id` | `string` | Folder ID to pass to `generate` |
| `folders[].name` | `string` | Display name |
| `count` | `int` | Total folders returned |

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

| Error | Description |
| --- | --- |
| `401 Unauthorized` | Missing or invalid OAuth Bearer token — see [Authentication errors](#authentication-errors) |
| Invalid parameter values | One or more parameters do not match expected format or values |
| Rate limit exceeded | Too many requests in a given time period |
| Network connectivity | Unable to establish connection to the server |
| Insufficient credits | Account does not have enough credits to complete the generation |

## Related

- [Set up the MCP server](gamma-mcp-server.md) for getting started and troubleshooting
- [Connect integrations](connectors-and-integrations.md) for platform-specific setup
- [Generate from text](generate-api-parameters-explained.md) for the equivalent REST API parameters
- [Access and pricing](access-and-pricing.md) for credit costs and plan details
