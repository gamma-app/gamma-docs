---
description: Generate a presentation, document, website, or social post from text.
---

# POST /generations

Start an asynchronous generation from text. Use this endpoint when Gamma should determine the layout from your input and generation settings.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/generations" method="post" %}
[OpenAPI gamma-public-api-v1](https://openapi.gitbook.com/o/1xFv2gf06r2iQQzarEcy/openapi/gamma-public-api-v1)
{% endopenapi-operation %}

{% hint style="info" %}
For parameter guidance, see [Generate from text](../overview/generate-api-parameters-explained.md).
{% endhint %}

## Inspecting rate limit headers

Every response from the Gamma API includes rate limit headers (`x-ratelimit-remaining-burst`, `x-ratelimit-remaining`, `x-ratelimit-remaining-daily`). When testing with curl, add the `-i` flag to display these headers alongside the response body:

```bash
curl -i -X POST "https://public-api.gamma.app/v1.0/generations" \
  -H "X-API-KEY: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "inputText": "Create a presentation about renewable energy",
    "textMode": "generate"
  }'
```

Without `-i`, curl only shows the JSON body. In Python, JavaScript, or any HTTP client, these headers are accessible on the response object without any special flag.

For a full breakdown of the rate limit headers and how to use them for adaptive polling, see [Rate limit headers and adaptive polling](../overview/async-patterns-and-polling.md#rate-limit-headers-and-adaptive-polling).

## Related

- [Generate from text](../overview/generate-api-parameters-explained.md) for parameter-by-parameter guidance
- [GET /generations/{id}](get-generation-status.md) for the polling step after creation
- [Async patterns and polling](../overview/async-patterns-and-polling.md) for the full polling workflow and rate limit guidance
