---
description: List all themes available in your workspace, including custom themes.
---

# GET /themes

List the themes available in the authenticated workspace. Use the returned `id` values as `themeId` in generation requests.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/themes" method="get" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="info" %}
For guidance on when to fetch theme IDs and how to use them in requests, see [Use themes and folders](../overview/list-themes-and-list-folders-apis-explained.md).
{% endhint %}

## Related

- [Use themes and folders](../overview/list-themes-and-list-folders-apis-explained.md) for workflow guidance
- [POST /generations](create-generation.md) if you want to apply a returned `themeId`
