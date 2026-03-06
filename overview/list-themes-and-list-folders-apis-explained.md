---
description: >-
  How to use the themes and folders endpoints to fetch the IDs you need for
  generation requests.
icon: palette
---

# Use themes and folders

Use these endpoints when you need to look up IDs for a generation request:

* Call `GET /v1.0/themes` when you need a `themeId`
* Call `GET /v1.0/folders` when you need one or more values for `folderIds`

Both endpoints support the same pagination pattern:

* `query` filters by name
* `limit` controls page size, up to 50
* `after` accepts the previous `nextCursor`
* responses include `data`, `hasMore`, and `nextCursor`

{% hint style="info" %}
This page focuses on how to use theme and folder IDs in your workflow. For the exact parameter and response schema for each endpoint, use the `GET /themes` and `GET /folders` pages in the API Reference tab.
{% endhint %}

### List Themes

Returns a paginated list of the themes in the your workspace. This endpoint returns both workspace-specific and global themes in a single response, filterable via the `type` field.

{% code title="GET Themes" %}
```bash
curl -X GET https://public-api.gamma.app/v1.0/themes \
-H "X-API-KEY: sk-gamma-xxxxxxxx"
```
{% endcode %}

#### **Themes response**

Each theme object in the `data` array contains:

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

The `type` field distinguishes between:

* `standard`: Global themes available to all workspaces
* `custom`: Workspace-specific themes

### List Folders

Returns a paginated list of the folders in your workspace.

{% code title="GET Folders" %}
```http
curl -X GET https://public-api.gamma.app/v1.0/folders \
-H "X-API-KEY: sk-gamma-xxxxxxxx"
```
{% endcode %}

#### **Folders response**

Each folder object in the `data` array contains:

{% code title="Sample response" %}
```json
{
  "id": "abc123def456",
  "name": "Business Proposals"
}
```
{% endcode %}

### Pagination Example: Fetch all folders

The example below is for fetching folders but also applies to listing themes.

#### **Get first page of folders**

{% code title="Request 1" %}
```http
GET /v1.0/folders?limit=50
```
{% endcode %}

{% code title="Response 1" %}
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

#### **Get additional folders**

* The `after` parameter accepts a cursor string from a previous response to fetch the next page of results. Cursors are always forward-only—you cannot paginate backward through results.
* When `hasMore` is `false` and `nextCursor` is `null`, you've reached the end of the results.

{% code title="Request 2" %}
```http
GET /v1.0/folders?limit=50&after=abc123def456ghi789
```
{% endcode %}

{% code title="Response 2" %}
```json
{
  "data": [
    { "id": "lmnop1", "name": "Sales" },
    { "id": "qrstuv", "name": "Product" }
  ],
  "hasMore": false,
  "nextCursor": "null"
}
```
{% endcode %}

### Query Example: Search for a theme

The example below shows how to search for a theme by name, and also applies to searching for folders.

#### **Search for themes with "dark" in the name**

{% code title="Request" %}
```http
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
    },
    {
      "id": "123abc456def",
      "name": "Dark Gradient",
      "type": "custom",
      "colorKeywords": ["purple", "black", "navy"],
      "toneKeywords": ["dramatic", "elegant"]
    }
  ],
  "hasMore": false,
  "nextCursor": "null"
}
```
{% endcode %}

The returned `id` can be used in the `themeId` parameter in the Generate and Create from Template APIs.
