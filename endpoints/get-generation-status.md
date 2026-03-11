---
description: Poll this endpoint until status is completed or failed.
---

# GET /generations/{id}

Use this endpoint to poll an existing generation until it reaches `completed` or `failed`. This is where you receive `gammaUrl`, `exportUrl`, and credit usage.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/generations/{id}" method="get" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="info" %}
For usage patterns, see [Poll for results](../overview/async-patterns-and-polling.md).
{% endhint %}

## Related

- [Poll for results](../overview/async-patterns-and-polling.md) for complete polling implementations
- [POST /generations](create-generation.md) if you need to start a new generation first
