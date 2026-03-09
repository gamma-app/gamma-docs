---
description: Detailed guide to customizing headers and footers in Gamma presentations
icon: table-columns
---

# Header and footer formatting

Headers and footers let you add consistent branding elements, page numbers, and custom text across all cards in your presentation.

## Quick reference

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

## Basic structure

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

## Element types

### Text elements

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

The `value` field is required for text elements. Keep text short because headers and footers have limited space.

### Image elements (theme logo)

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

### Image elements (custom URL)

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

When using `source: "custom"`, the `src` field is required and must be a valid, publicly accessible URL to an image file.

### Card numbers

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

Card numbers have no additional configuration. Just specify the position and type.

## Hiding from first and last cards

You often want to hide headers/footers from title cards or closing cards. Add these properties **at the `headerFooter` level** (they apply to all positions):

```json
{
  "cardOptions": {
    "headerFooter": {
      "topRight": {
        "type": "image",
        "source": "themeLogo"
      },
      "bottomRight": {
        "type": "cardNumber"
      },
      "hideFromFirstCard": true,
      "hideFromLastCard": true
    }
  }
}
```

| Property            | Default | Description                                    |
| ------------------- | ------- | ---------------------------------------------- |
| `hideFromFirstCard` | `false` | Set `true` to hide from title/intro card       |
| `hideFromLastCard`  | `false` | Set `true` to hide from closing/thank you card |

## Complete examples

### Professional presentation (logo and page numbers)

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
        "size": "sm"
      },
      "bottomRight": {
        "type": "cardNumber"
      },
      "bottomLeft": {
        "type": "text",
        "value": "Confidential - Internal Use Only"
      },
      "hideFromFirstCard": true,
      "hideFromLastCard": true
    }
  }
}
```

### Social media carousel (minimal branding)

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

### Document with theme logo

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

## Common mistakes

### Missing `value` for text elements

```json
// ❌ Wrong - missing value
{ "type": "text" }

// ✅ Correct
{ "type": "text", "value": "My Text" }
```

### Missing `src` for custom images

```json
// ❌ Wrong - missing src
{ "type": "image", "source": "custom" }

// ✅ Correct  
{ "type": "image", "source": "custom", "src": "https://..." }
```

### Boolean values as strings

```json
// ❌ Wrong - string instead of boolean
{ "hideFromFirstCard": "true" }

// ✅ Correct
{ "hideFromFirstCard": true }
```

## Limitations

* **Not available for `webpage` format** — web pages don't have fixed headers/footers
* **Six positions maximum** — you can only use the six defined positions
* **One element per position** — each position can only hold one type of content

## Related

* [Generate from text](generate-api-parameters-explained.md) for the full `cardOptions` and `sharingOptions` context
* [Image model accepted values](../accepted-values/image-model-accepted-values.md) if you are pairing branding with AI-generated images
* [API Overview](understanding-the-api-options.md) for the broader generation workflow
