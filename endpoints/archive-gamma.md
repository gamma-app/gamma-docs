---
description: Archive a Gamma document. Idempotent -- archiving an already archived Gamma succeeds.
---

# POST /gammas/{gammaId}/archive

Archive a Gamma to remove it from the active workspace without deleting it.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/gammas/{gammaId}/archive" method="post" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="warning" %}
**The `gammaId` must be the file ID returned by the API** (e.g. `g_l0mf2jvf1fpmi1v`), not the slug from the web app URL. If you pass the URL slug (the ID at the end of `gamma.app/docs/My-Doc-bc7s74ruzod20f4`), the request returns `403` instead of `404`.
{% endhint %}

### Example

```bash
curl -X POST "https://public-api.gamma.app/v1.0/gammas/$GAMMA_ID/archive" \
  -H "X-API-KEY: $GAMMA_API_KEY"
```

```json
{
  "gammaId": "g_l0mf2jvf1fpmi1v",
  "archived": true
}
```

### Behavior

- **Idempotent.** Archiving an already archived Gamma returns `200` with `"archived": true`.
- **No credits deducted.** This endpoint does not consume credits.
- **Requires edit permission.** The API key owner must have edit access, and the Gamma must belong to the API key's workspace.

### Finding the gammaId

Poll a completed generation to get the ID:

```bash
curl "https://public-api.gamma.app/v1.0/generations/$GENERATION_ID" \
  -H "X-API-KEY: $GAMMA_API_KEY"
```

The `gammaId` value in the response (e.g. `g_l0mf2jvf1fpmi1v`) is what you pass to `/archive`. The `gammaUrl` field contains the web app link, but the slug in that URL is not the same ID.

### Related

- [GET /generations/{id}](get-generation-status.md) to retrieve the `gammaId` from a generation
- [Error codes](../errors-and-warnings/error-codes.md) for the `403` response when using a wrong ID
