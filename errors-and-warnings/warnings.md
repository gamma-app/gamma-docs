---
description: Understanding warning messages in API responses.
---

# Warnings

In some cases, you may receive warnings in response to a generation request. Warnings are returned if there were conflicting or ignored parameters in your API call.

For example, if you specified `preserve` in `textMode` and at the same time used `brief` in `textOptions.amount`, Gamma would respect the instruction to preserve your text and would ignore the request for the generated text to be brief. For transparency, the API would return a warning informing you that we ignored the `textOptions.amount` parameter.

{% hint style="info" %}
Warnings are informational and do not prevent the generation from completing. Your Gamma will still be created, but some parameters may have been ignored or adjusted.
{% endhint %}

## Common Warning Scenarios

### Conflicting format and dimensions

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

### Valid Dimensions by Format

| Format         | Valid Dimensions                    |
| -------------- | ----------------------------------- |
| `presentation` | `16x9`, `4x3`, `fluid`              |
| `document`     | `pageless`, `letter`, `a4`, `fluid` |
| `social`       | `1x1`, `4x5`, `9x16`                |
| `webpage`      | `fluid`                             |

### Conflicting image source and model

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

### textMode preserve with textOptions

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

## Best Practices

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><h3><i class="fa-bug">:bug:</i></h3></td><td><h4>Check warnings in development</h4></td><td>Always log and review warnings during development to ensure your API calls are configured correctly.</td></tr><tr><td><h3><i class="fa-ruler">:ruler:</i></h3></td><td><h4>Match format to dimensions</h4></td><td>Use dimensions that are valid for your chosen format to avoid unexpected defaults.</td></tr><tr><td><h3><i class="fa-wand-magic-sparkles">:wand-magic-sparkles:</i></h3></td><td><h4>Use aiGenerated for models</h4></td><td>Only specify <code>imageOptions.model</code> when <code>imageOptions.source</code> is set to <code>aiGenerated</code>.</td></tr><tr><td><h3><i class="fa-text">:text:</i></h3></td><td><h4>Understand textMode behavior</h4></td><td><code>preserve</code> keeps your text as-is, <code>condense</code> summarizes, <code>generate</code> creates new content from your prompt.</td></tr></tbody></table>
