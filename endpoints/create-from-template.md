---
description: Adapt, remix, or transform an existing Gamma. The template's structure is preserved by default and changes only when your prompt asks.
---

# POST /generations/from-template

Start an asynchronous generation by adapting an existing Gamma — swap content, retarget for a new audience, transform the subject, replace images, or restructure cards. The template's structure is preserved by default; it only changes when your prompt explicitly asks.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/generations/from-template" method="post" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="info" %}
For template workflow guidance, see [Generate from template](../overview/create-from-template-api-parameters-explained.md).
{% endhint %}

## Related

- [Generate from template](../overview/create-from-template-api-parameters-explained.md) for workflow and parameter guidance
- [GET /generations/{id}](get-generation-status.md) for the polling step after creation
