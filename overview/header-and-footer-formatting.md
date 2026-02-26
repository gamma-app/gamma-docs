---
description: Detailed guide to customizing headers and footers in Gamma presentations
icon: table-columns
---

# Header & Footer Formatting

Headers and footers let you add consistent branding elements, page numbers, and custom text across all cards in your presentation.

## Quick Reference

| Position       | Description                       |
| -------------- | --------------------------------- |
| `topLeft`      | Top-left corner of every card     |
| `topCenter`    | Top-center of every card          |
| `topRight`     | Top-right corner of every card    |
| `bottomLeft`   | Bottom-left corner of every card  |
| `bottomCenter` | Bottom-center of every card       |
| `bottomRight`  | Bottom-right corner of every card |

| Element Type | Use Case                          |
| ------------ | --------------------------------- |
| `text`       | Company name, copyright, taglines |
| `image`      | Logo from theme or custom URL     |
| `cardNumber` | Slide/page numbers                |

## Basic Structure

The `headerFooter` object goes inside `cardOptions`:

```json
{
  "cardOptions": {
    "headerFooter": {
      "topRight": {
        "type": "...",
        // type-specific properties
      },
      "bottomLeft": {
        "type": "...",
        // type-specific properties
      }
    }
  }
}
```

## Element Types

### Text Elements

Add custom text like company names, copyright notices, or taglines.

```json
{
  "cardOptions": {
    "headerFooter": {
      "bottomRight": {
        "type": "text",
        "value": "© 2025 Acme Corp"
      },
      "topLeft": {
        "type": "text", 
        "value": "Confidential"
      }
    }
  }
}
```

{% hint style="info" %}
The `value` field is **required** for text elements. Keep text short — headers and footers have limited space.
{% endhint %}

### Image Elements (Theme Logo)

Use the logo from your selected theme:

```json
{
  "cardOptions": {
    "headerFooter": {
      "topRight": {
        "type": "image",
        "source": "themeLogo",
        "size": "md"
      }
    }
  }
}
```

| Size | Description                       |
| ---- | --------------------------------- |
| `sm` | Small logo (subtle branding)      |
| `md` | Medium logo (default, balanced)   |
| `lg` | Large logo (prominent)            |
| `xl` | Extra large logo (very prominent) |

### Image Elements (Custom URL)

Use your own logo image:

```json
{
  "cardOptions": {
    "headerFooter": {
      "topRight": {
        "type": "image",
        "source": "custom",
        "src": "https://example.com/your-logo.png",
        "size": "sm"
      }
    }
  }
}
```

{% hint style="warning" %}
When using `source: "custom"`, the \`src\` field is **required** and must be a valid, publicly accessible URL to an image file (PNG, JPG, SVG).
{% endhint %}

### Card Numbers

Add automatic page/slide numbers:

```json
{
  "cardOptions": {
    "headerFooter": {
      "bottomRight": {
        "type": "cardNumber"
      }
    }
  }
}
```

{% hint style="info" %}
Card numbers have no additional configuration — just specify the position and type.
{% endhint %}

## Hiding from First/Last Cards

You often want to hide headers/footers from title cards or closing cards. Add these properties **at the position level**:

```json
{
  "cardOptions": {
    "headerFooter": {
      "topRight": {
        "type": "image",
        "source": "themeLogo",
        "hideFromFirstCard": true,
        "hideFromLastCard": true
      },
      "bottomRight": {
        "type": "cardNumber",
        "hideFromFirstCard": true
      }
    }
  }
}
```

| Property            | Default | Description                                    |
| ------------------- | ------- | ---------------------------------------------- |
| `hideFromFirstCard` | `false` | Set `true` to hide from title/intro card       |
| `hideFromLastCard`  | `false` | Set `true` to hide from closing/thank you card |

### Complete Examples

#### Professional Presentation (Logo + Page Numbers)

```json
{
  "inputText": "Create a quarterly business review for Q4 2024",
  "textMode": "generate",
  "format": "presentation",
  "numCards": 12,
  "cardOptions": {
    "dimensions": "16x9",
    "headerFooter": {
      "topRight": {
        "type": "image",
        "source": "custom",
        "src": "https://example.com/company-logo.png",
        "size": "sm",
        "hideFromFirstCard": true
      },
      "bottomRight": {
        "type": "cardNumber",
        "hideFromFirstCard": true,
        "hideFromLastCard": true
      },
      "bottomLeft": {
        "type": "text",
        "value": "Confidential - Internal Use Only",
        "hideFromFirstCard": true
      }
    }
  }
}
```

#### Social Media Carousel (Minimal Branding)

```json
{
  "inputText": "5 tips for better productivity",
  "textMode": "generate",
  "format": "social",
  "numCards": 6,
  "cardOptions": {
    "dimensions": "1x1",
    "headerFooter": {
      "bottomCenter": {
        "type": "text",
        "value": "@yourhandle"
      }
    }
  }
}
```

#### Document with Theme Logo

```json
{
  "inputText": "Technical specification for Project X",
  "textMode": "generate",
  "format": "document",
  "numCards": 8,
  "cardOptions": {
    "dimensions": "letter",
    "headerFooter": {
      "topLeft": {
        "type": "image",
        "source": "themeLogo",
        "size": "md"
      },
      "topRight": {
        "type": "text",
        "value": "Technical Specification"
      },
      "bottomRight": {
        "type": "cardNumber"
      }
    }
  }
}
```

### Common Mistakes

{% hint style="warning" %}
**Missing \`value\` for text type**

```json
// ❌ Wrong - missing value
{ "type": "text" }

// ✅ Correct
{ "type": "text", "value": "My Text" }
```
{% endhint %}

{% hint style="warning" %}
**Missing `src` for custom images**

```json
// ❌ Wrong - missing src
{ "type": "image", "source": "custom" }

// ✅ Correct  
{ "type": "image", "source": "custom", "src": "https://..." }
```
{% endhint %}

{% hint style="warning" %}
**Boolean values as strings**

```json
// ❌ Wrong - string instead of boolean
{ "hideFromFirstCard": "true" }

// ✅ Correct
{ "hideFromFirstCard": true }
```
{% endhint %}

## Limitations

* **Not available for `webpage` format** — web pages don't have fixed headers/footers
* **Six positions maximum** — you can only use the six defined positions
* **One element per position** — each position can only hold one type of content

## Related

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h2><i class="fa-sliders">:sliders:</i></h2></td><td><strong>Generate API Parameters</strong></td><td>Complete parameter reference</td><td><a href="generate-api-parameters-explained.md">generate-api-parameters-explained.md</a></td></tr><tr><td><h2><i class="fa-image">:image:</i></h2></td><td><strong>Image Model Options</strong></td><td>Available AI image models</td><td><a href="https://app.gitbook.com/s/IrzC0mooWT36AKgnkerQ/accepted-values/image-model-accepted-values">Image model accepted values</a></td></tr></tbody></table>
