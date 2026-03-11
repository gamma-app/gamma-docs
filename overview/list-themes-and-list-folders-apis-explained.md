---
description: >-
  How to use the themes and folders endpoints to fetch the IDs you need for
  generation requests.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Use themes and folders

Use these endpoints when you need to look up IDs for a generation request.

### Quick reference

- Call `GET /v1.0/themes` to get a `themeId`.
- Call `GET /v1.0/folders` to get values for `folderIds`.
- Both endpoints use cursor-based pagination with `query`, `limit`, `after`, `hasMore`, and `nextCursor`.
- Theme objects include `type` (`standard` or `custom`), `colorKeywords`, and `toneKeywords`.

{% hint style="info" %}
This page focuses on how to use theme and folder IDs in your workflow. For the exact parameter and response schema, see the [GET /themes](../endpoints/list-themes.md) and [GET /folders](../endpoints/list-folders.md) endpoint reference pages.
{% endhint %}

### List themes

Returns a paginated list of themes in your workspace, including both workspace-specific and global themes.

{% code title="Request" %}
```bash
curl -X GET https://public-api.gamma.app/v1.0/themes \
-H "X-API-KEY: sk-gamma-xxxxxxxx"
```
{% endcode %}

**Response fields** -- each theme object in the `data` array contains:

{% code title="Sample response" %}
```json
{
  "id": "abcdefghi",
  "name": "Prism",
  "type": "custom",
  "colorKeywords": ["light","blue","pink","purple","pastel","gradient","vibrant"],
  "toneKeywords": ["playful","friendly","creative","inspirational","fun"]
}
```
{% endcode %}

The `type` field distinguishes between `standard` (global themes available to all workspaces) and `custom` (workspace-specific themes).

### List folders

Returns a paginated list of folders in your workspace.

{% code title="Request" %}
```bash
curl -X GET https://public-api.gamma.app/v1.0/folders \
-H "X-API-KEY: sk-gamma-xxxxxxxx"
```
{% endcode %}

**Response fields** -- each folder object in the `data` array contains:

{% code title="Sample response" %}
```json
{
  "id": "abc123def456",
  "name": "Business Proposals"
}
```
{% endcode %}

### Pagination

Both endpoints use the same cursor-based pagination. The example below uses folders, but the pattern is identical for themes.

**First page:**

{% code title="Request" %}
```text
GET /v1.0/folders?limit=50
```
{% endcode %}

{% code title="Response" %}
```json
{
  "data": [
    { "id": "abcdef", "name": "Design" },
    { "id": "xyzabc", "name": "Marketing" }
  ],
  "hasMore": true,
  "nextCursor": "abc123def456ghi789"
}
```
{% endcode %}

**Next page** -- pass the previous `nextCursor` as `after`. When `hasMore` is `false` and `nextCursor` is `null`, you've reached the end.

{% code title="Request" %}
```text
GET /v1.0/folders?limit=50&after=abc123def456ghi789
```
{% endcode %}

{% code title="Response" %}
```json
{
  "data": [
    { "id": "lmnop1", "name": "Sales" },
    { "id": "qrstuv", "name": "Product" }
  ],
  "hasMore": false,
  "nextCursor": null
}
```
{% endcode %}

### Searching by name

Use the `query` parameter to filter results by name. Works on both themes and folders.

{% code title="Request" %}
```text
GET /v1.0/themes?query=dark&limit=50
```
{% endcode %}

{% code title="Response" %}
```json
{
  "data": [
    {
      "id": "abc123def456",
      "name": "Standard Dark",
      "type": "standard",
      "colorKeywords": ["black", "gray", "accent"],
      "toneKeywords": ["sophisticated", "modern"]
    }
  ],
  "hasMore": false,
  "nextCursor": null
}
```
{% endcode %}

The returned `id` can be used as `themeId` in the Generate and Create from Template APIs.

### Related

- [Generate from text](generate-api-parameters-explained.md) for where `themeId` and `folderIds` fit in the request
- [Generate from template](create-from-template-api-parameters-explained.md) for using theme and folder IDs with templates
- [GET /themes](../endpoints/list-themes.md) for the full API reference
- [GET /folders](../endpoints/list-folders.md) for the full API reference
