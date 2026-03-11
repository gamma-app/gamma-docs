---
description: Understanding warning messages in API responses.
---

# Warnings

In some cases, you may receive warnings in response to a generation request. Warnings are returned if there were conflicting or ignored parameters in your API call.

For example, if you specified `preserve` in `textMode` and at the same time used `brief` in `textOptions.amount`, Gamma would respect the instruction to preserve your text and would ignore the request for the generated text to be brief. For transparency, the API would return a warning informing you that we ignored the `textOptions.amount` parameter.

{% hint style="info" %}
Warnings are informational and do not prevent the generation from completing. Your Gamma will still be created, but some parameters may have been ignored or adjusted.
{% endhint %}

### Quick reference

- Warnings do not stop generation.
- A warning usually means Gamma ignored a conflicting or incompatible parameter.
- The warning string is returned alongside `generationId` in the creation response.

### Common warning scenarios

#### Conflicting format and dimensions

If you specify card dimensions that don't match your chosen format, Gamma will use a valid default.

**Request:**

```json
{
  "format": "presentation",
  "inputText": "Best hikes in the United States",
  "cardOptions": {
    "dimensions": "1x1"
  }
}
```

**Response:**

```json
{
  "generationId": "xxxxxxxxxx",
  "warnings": "cardOptions.dimensions 1x1 is not valid for format presentation. Valid dimensions are: [ 16x9, 4x3, fluid ]. Using default: fluid."
}
```

#### Valid Dimensions by Format

| Format         | Valid Dimensions                    |
| -------------- | ----------------------------------- |
| `presentation` | `16x9`, `4x3`, `fluid`              |
| `document`     | `pageless`, `letter`, `a4`, `fluid` |
| `social`       | `1x1`, `4x5`, `9x16`                |
| `webpage`      | `fluid`                             |

#### Conflicting image source and model

If you specify an image model but the source is not `aiGenerated`, the model will be ignored.

**Request:**

```json
{
  "format": "presentation",
  "inputText": "Best hikes in the United States",
  "imageOptions": {
    "source": "pictographic",
    "model": "flux-1-pro"
  }
}
```

**Response:**

```json
{
  "generationId": "xxxxxxxxxx",
  "warnings": "imageOptions.model and imageOptions.style are ignored when imageOptions.source is not aiGenerated."
}
```

#### textMode preserve with textOptions

When using `textMode: "preserve"`, text generation options like `amount`, `tone`, and `audience` are ignored since your original text is being preserved.

**Request:**

```json
{
  "inputText": "Your detailed content here...",
  "textMode": "preserve",
  "textOptions": {
    "amount": "brief",
    "tone": "casual"
  }
}
```

**Response:**

```json
{
  "generationId": "xxxxxxxxxx",
  "warnings": "textOptions.amount and textOptions.tone are ignored when textMode is preserve."
}
```

### Best practices

- Log and review warnings during development so ignored parameters are easy to spot.
- Match `format` and `cardOptions.dimensions` to avoid unexpected defaults.
- Only specify `imageOptions.model` when `imageOptions.source` is `aiGenerated`.
- Treat `textMode: "preserve"` as higher priority than text-generation settings like `amount`, `tone`, or `audience`.

### Related

- [Error codes](error-codes.md) for fatal API errors
- [Generate from text](../overview/generate-api-parameters-explained.md) for parameter interactions that commonly produce warnings
- [Generate from template](../overview/create-from-template-api-parameters-explained.md) for the template-specific workflow
