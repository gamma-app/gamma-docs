---
description: List all folders the authenticated user is a member of.
icon: folder
---

# GET /folders

List the folders the authenticated user can access. Use the returned `id` values in `folderIds` when you want generated output stored in a specific folder.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/folders" method="get" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="info" %}
For guidance on when to fetch folder IDs and how to use them in requests, see [Use themes and folders](../overview/list-themes-and-list-folders-apis-explained.md).
{% endhint %}

## Related

- [Use themes and folders](../overview/list-themes-and-list-folders-apis-explained.md) for workflow guidance
- [POST /generations](create-generation.md) if you want to place output into one or more folders
