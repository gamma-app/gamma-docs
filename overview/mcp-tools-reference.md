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

| Tool          | Description                                                | Read-only | Destructive | Idempotent |
| ------------- | ---------------------------------------------------------- | --------- | ----------- | ---------- |
| `generate`    | Create presentations, documents, webpages, or social posts | No        | No          | No         |
| `get_themes`  | Browse or search the Gamma theme library                   | Yes       | No          | Yes        |
| `get_folders` | Browse or search your Gamma folders                        | Yes       | No          | Yes        |

## generate

Create a new presentation, document, webpage, or social media post. Ask the user clarifying questions about text mode, length, tone, and audience when needed.

Each call creates new content — the tool is not idempotent.

### Input parameters

<table data-full-width="true"><thead><tr><th width="214.76043701171875">Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead><tbody><tr><td><code>inputText</code></td><td><code>string</code></td><td>Yes</td><td>Content to generate from — a text prompt, outline, or full content</td></tr><tr><td><code>textMode</code></td><td><code>enum</code></td><td>No</td><td>How to handle input text: <code>generate</code> (new content from brief prompt), <code>condense</code> (summarize existing content), <code>preserve</code> (use content as-is)</td></tr><tr><td><code>format</code></td><td><code>enum</code></td><td>No</td><td>Output type: <code>presentation</code>, <code>document</code>, <code>social</code>, <code>webpage</code></td></tr><tr><td><code>numCards</code></td><td><code>int</code></td><td>No</td><td>Number of slides, cards, or pages to generate</td></tr><tr><td><code>themeId</code></td><td><code>string</code></td><td>No</td><td>Theme ID from <code>get_themes</code></td></tr><tr><td><code>folderIds</code></td><td><code>array[string]</code></td><td>No</td><td>Folder IDs from <code>get_folders</code> to organize the content</td></tr><tr><td><code>additionalInstructions</code></td><td><code>string</code></td><td>No</td><td>Extra guidance for the AI generator not covered by other parameters</td></tr><tr><td><code>exportAs</code></td><td><code>enum</code></td><td>No</td><td>Export format: <code>pptx</code> or <code>pdf</code> (only when the user explicitly requests export)</td></tr></tbody></table>

### Text options

Optional `textOptions` object for controlling text generation.

| Parameter  | Type     | Description                                                                   |
| ---------- | -------- | ----------------------------------------------------------------------------- |
| `amount`   | `enum`   | Text density per slide or section: `brief`, `medium`, `detailed`, `extensive` |
| `tone`     | `string` | Writing tone (e.g., `professional`, `casual`)                                 |
| `audience` | `string` | Target audience (e.g., `executives`, `students`)                              |
| `language` | `string` | Language code (e.g., `en`, `es`, `fr`)                                        |

### Image options

Optional `imageOptions` object for controlling image sourcing.

| Parameter | Type     | Description                                                                                                                                             |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `source`  | `enum`   | Image source: `aiGenerated`, `webAllImages`, `webFreeToUse`, `webFreeToUseCommercially`, `pictographic`, `giphy`, `unsplash`, `placeholder`, `noImages` |
| `model`   | `string` | AI image model (only when `source` is `aiGenerated`)                                                                                                    |
| `style`   | `string` | Style for AI images (e.g., `photorealistic`, `illustration`)                                                                                            |

### Card options

Optional `cardOptions` object for layout and header/footer configuration.

| Parameter      | Type     | Description                                                                                         |
| -------------- | -------- | --------------------------------------------------------------------------------------------------- |
| `dimensions`   | `enum`   | Aspect ratio or page size: `16x9`, `4x3`, `fluid`, `letter`, `a4`, `pageless`, `1x1`, `4x5`, `9x16` |
| `headerFooter` | `object` | Header and footer configuration (only use if explicitly requested)                                  |

**Header/footer object**

The `headerFooter` object contains six slot positions and two visibility flags. All properties are optional.

| Parameter           | Type      | Description                            |
| ------------------- | --------- | -------------------------------------- |
| `topLeft`           | `object`  | Top-left header slot                   |
| `topCenter`         | `object`  | Top-center header slot                 |
| `topRight`          | `object`  | Top-right header slot                  |
| `bottomLeft`        | `object`  | Bottom-left footer slot                |
| `bottomCenter`      | `object`  | Bottom-center footer slot              |
| `bottomRight`       | `object`  | Bottom-right footer slot               |
| `hideFromFirstCard` | `boolean` | Hide header/footer from the first card |
| `hideFromLastCard`  | `boolean` | Hide header/footer from the last card  |

**Slot configuration**

Each slot object (`topLeft`, `topCenter`, etc.) accepts:

| Parameter | Type     | Required | Description                                                           |
| --------- | -------- | -------- | --------------------------------------------------------------------- |
| `type`    | `enum`   | Yes      | Content type: `cardNumber`, `image`, `text`                           |
| `source`  | `enum`   | No       | Image source (required when `type` is `image`): `themeLogo`, `custom` |
| `src`     | `string` | No       | Image URL (required when `type` is `image` and `source` is `custom`)  |
| `value`   | `string` | No       | Text content (required when `type` is `text`)                         |
| `size`    | `enum`   | No       | Image size: `sm`, `md`, `lg`, `xl`                                    |

### Sharing options

Optional `sharingOptions` object for controlling access after generation.

| Parameter         | Type     | Description                                                                  |
| ----------------- | -------- | ---------------------------------------------------------------------------- |
| `workspaceAccess` | `enum`   | Workspace member access: `edit`, `comment`, `view`, `noAccess`, `fullAccess` |
| `externalAccess`  | `enum`   | External user access: `edit`, `comment`, `view`, `noAccess`                  |
| `emailOptions`    | `object` | Share via email to specific recipients (see below)                           |

**Email options object**

| Parameter    | Type            | Required | Description                                                     |
| ------------ | --------------- | -------- | --------------------------------------------------------------- |
| `recipients` | `array[string]` | Yes      | Email addresses to share with                                   |
| `access`     | `enum`          | Yes      | Recipient access level: `edit`, `comment`, `view`, `fullAccess` |

### Output

| Field               | Type     | Description                                                      |
| ------------------- | -------- | ---------------------------------------------------------------- |
| `generationId`      | `string` | Unique ID for the generation                                     |
| `status`            | `enum`   | Generation status: `completed` or `failed`                       |
| `gammaUrl`          | `string` | URL to the created content (when `status` is `completed`)        |
| `exportUrl`         | `string` | Download URL for the export file (when `exportAs` was specified) |
| `credits.deducted`  | `int`    | Credits deducted for this generation                             |
| `credits.remaining` | `int`    | Remaining credits after generation                               |
| `error`             | `string` | Error message (when `status` is `failed`)                        |

## get\_themes

Browse or search the Gamma theme library. Use the returned `id` in the `generate` tool's `themeId` parameter.

If the user references a theme by name, search by name. Otherwise, fetch the full list and choose based on tone and color keywords.

### Input parameters

| Parameter | Type     | Description                                                                           |
| --------- | -------- | ------------------------------------------------------------------------------------- |
| `name`    | `string` | Optional. Search themes by name (only when the user references a specific theme name) |

### Output

| Field                    | Type            | Description                           |
| ------------------------ | --------------- | ------------------------------------- |
| `themes`                 | `array[object]` | Array of theme objects                |
| `themes[].id`            | `string`        | Theme ID to pass to `generate`        |
| `themes[].name`          | `string`        | Display name                          |
| `themes[].type`          | `enum`          | `standard` or `custom`                |
| `themes[].colorKeywords` | `array[string]` | Color keywords describing the palette |
| `themes[].toneKeywords`  | `array[string]` | Tone keywords describing the style    |
| `count`                  | `int`           | Total themes returned                 |

## get\_folders

Browse or search your Gamma folders. Use the returned `id` in the `generate` tool's `folderIds` parameter.

### Input parameters

| Parameter | Type     | Description                                                   |
| --------- | -------- | ------------------------------------------------------------- |
| `name`    | `string` | Optional. Search folders by name (omit to return all folders) |

### Output

| Field            | Type            | Description                     |
| ---------------- | --------------- | ------------------------------- |
| `folders`        | `array[object]` | Array of folder objects         |
| `folders[].id`   | `string`        | Folder ID to pass to `generate` |
| `folders[].name` | `string`        | Display name                    |
| `count`          | `int`           | Total folders returned          |

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

| Error                    | Description                                                                                                       |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `401 Unauthorized`       | Missing or invalid OAuth Bearer token — see [Authentication errors](mcp-tools-reference.md#authentication-errors) |
| Invalid parameter values | One or more parameters do not match expected format or values                                                     |
| Rate limit exceeded      | Too many requests in a given time period                                                                          |
| Network connectivity     | Unable to establish connection to the server                                                                      |
| Insufficient credits     | Account does not have enough credits to complete the generation                                                   |

## Related

* [Set up the MCP server](gamma-mcp-server.md) for getting started and troubleshooting
* [Connect integrations](connectors-and-integrations.md) for platform-specific setup
* [Generate from text](generate-api-parameters-explained.md) for the equivalent REST API parameters
* [Access and pricing](access-and-pricing.md) for credit costs and plan details
