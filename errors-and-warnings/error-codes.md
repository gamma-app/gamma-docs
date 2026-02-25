---
description: Detailed descriptions of API error codes.
---

# Error codes

Below are detailed descriptions of error codes returned by the Gamma API.

## Example Error Response

```json
{
  "message": "Invalid API key.",
  "statusCode": 401
}
```

## Error Code Reference

| Status Code | Message                                                   | Description                                                                                                                             |
| ----------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| 400         | Input validation errors                                   | Invalid parameters detected. Check the error details for specific parameter requirements.                                               |
| 401         | Invalid API key                                           | The provided API key is invalid or not associated with a Pro account.                                                                   |
| 403         | Forbidden                                                 | No credits left. Upgrade your plan or refill credits.                                                                                   |
| 404         | Generation ID not found. generationId: xxxxxx             | The specified generation ID could not be located. Check and correct your generation ID.                                                 |
| 422         | Failed to generate text. Check your inputs and try again. | Generation produced an empty output. Review your input parameters and ensure your instructions are clear.                               |
| 429         | Too many requests                                         | Too many requests have been made. Retry after the rate limit period.                                                                    |
| 500         | An error occurred while generating the gamma.             | An unexpected error occurred while generating the gamma. Contact support with the `x-request-id` header for troubleshooting assistance. |
| 502         | Bad gateway                                               | The request could not be processed due to a temporary gateway issue. Try again.                                                         |

## Troubleshooting Tips

<details>

<summary>400 - Input validation errors</summary>

* Check that all required fields are present (`inputText`, `textMode` for v1.0)
* Verify enum values match exactly (e.g., `presentation` not `Presentation`)
* Ensure `inputText` is between 1 and 400,000 characters
* Check that `numCards` is within your plan’s limits

</details>

<details>

<summary>401 - Invalid API key</summary>

* Verify your API key starts with `sk-gamma-`
* Check that the key hasn’t been revoked
* Ensure the header is `X-API-KEY` (case-sensitive)

</details>

<details>

<summary>429 - Rate limit exceeded</summary>

* Wait before retrying (check `Retry-After` header if present)
* Implement exponential backoff in your integration
* Consider upgrading your plan for higher limits

</details>
