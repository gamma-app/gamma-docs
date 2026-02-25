---
description: >-
  List API methods support bulk fetching through cursor-based pagination. You
  can list folders with GET /v1.0/folders and list themes with GET /v1.0/themes.
---

# List Themes and List Folders APIs explained

These endpoints share a common structure and accept the same pagination parameters.

#### **All list endpoints accept the following parameters**

| Parameter | Type               | Description                                                                                   |
| --------- | ------------------ | --------------------------------------------------------------------------------------------- |
| `query`   | string (optional)  | Search by name (case-insensitive). Filters results to items matching the search term.         |
| `limit`   | integer (optional) | Number of items to return per page. Maximum: 50.                                              |
| `after`   | string (optional)  | Cursor token for fetching the next page. Use the nextCursor value from the previous response. |

#### **List response format**

| Field        | Type           | Description                                                                                                                            |
| ------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `data`       | array          | Array of folder or theme objects.                                                                                                      |
| `hasMore`    | boolean        | Indicates whether more pages exist. When true, use nextCursor to fetch the next page.                                                  |
| `nextCursor` | string or null | Opaque cursor token for the next page. Pass this value to the `after` parameter in your next request. Returns `null` on the last page. |

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
