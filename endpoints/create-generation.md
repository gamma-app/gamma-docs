---
description: Generate a presentation, document, website, or social post from text.
icon: plus
---

# POST /generations

Start an asynchronous generation from text. Use this endpoint when Gamma should determine the layout from your input and generation settings.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/generations" method="post" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="info" %}
For parameter guidance, see [Generate from text](../overview/generate-api-parameters-explained.md).
{% endhint %}

## Related

- [Generate from text](../overview/generate-api-parameters-explained.md) for parameter-by-parameter guidance
- [GET /generations/{id}](get-generation-status.md) for the polling step after creation
