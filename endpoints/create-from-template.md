---
description: Generate content from an existing Gamma template with variable substitution.
---

# POST /generations/from-template

Start an asynchronous generation from an existing Gamma template. Use this when you want to keep a fixed layout and swap in new content.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/generations/from-template" method="post" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="info" %}
For template workflow guidance, see [Generate from template](../overview/create-from-template-api-parameters-explained.md).
{% endhint %}

## Related

- [Generate from template](../overview/create-from-template-api-parameters-explained.md) for workflow and parameter guidance
- [GET /generations/{id}](get-generation-status.md) for the polling step after creation
