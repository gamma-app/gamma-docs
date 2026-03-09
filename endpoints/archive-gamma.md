---
description: Archive a Gamma document. Idempotent — archiving an already archived Gamma succeeds.
icon: box-archive
---

# POST /gammas/{gammaId}/archive

Archive an existing Gamma document. Use this endpoint when you want to remove a generated Gamma from the active workspace without deleting it.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/gammas/{gammaId}/archive" method="post" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="info" %}
Use the Gamma file ID returned by a completed generation or copied from the app.
{% endhint %}

## Related

- [GET /generations/{id}](get-generation-status.md) if you need to retrieve the `gammaId` from a recent generation
- [API Overview](../overview/understanding-the-api-options.md) for the broader workflow around creating and managing output
