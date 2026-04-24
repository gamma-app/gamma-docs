---
description: >-
  When creating AI generated images in your gamma, you can specify which model
  to use.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Image models

### Quick reference

- Set `imageOptions.source` to `aiGenerated` when using any of the model strings below.
- If `imageOptions.model` is omitted, Gamma selects a model automatically.
- Higher-tier, HD, and video models usually take longer to complete, so longer polling windows may be helpful.
- All models below are available to API users (Pro plan and above). Models are grouped by credit cost.
- See [Access and Pricing](../overview/access-and-pricing.md) for plan and credit details.

### Standard models

| Model Name | String | Credits/Image |
| --- | --- | --- |
| Flux 2 Fast | `flux-2-klein` | 2 |
| Flux Kontext Fast | `flux-kontext-fast` | 2 |
| Imagen 3 Fast | `imagen-3-flash` | 2 |
| Luma Photon Flash | `luma-photon-flash-1` | 2 |
| GPT Image 2 Mini | `gpt-image-2-mini` | 5 |
| Flux 2 Pro | `flux-2-pro` | 8 |
| Ideogram 3 Turbo | `ideogram-v3-turbo` | 10 |
| Imagen 4 Fast | `imagen-4-fast` | 10 |
| Luma Photon | `luma-photon-1` | 10 |
| Recraft V4 | `recraft-v4` | 12 |
| Leonardo Phoenix | `leonardo-phoenix` | 15 |

### Advanced models

| Model Name | String | Credits/Image |
| --- | --- | --- |
| Flux 2 Flex | `flux-2-flex` | 20 |
| Flux 2 Max | `flux-2-max` | 20 |
| Flux Kontext Pro | `flux-kontext-pro` | 20 |
| Ideogram 3 | `ideogram-v3` | 20 |
| Imagen 4 | `imagen-4-pro` | 20 |
| Recraft V3 | `recraft-v3` | 20 |
| Nano Banana Pro (Gemini 3 Pro) | `gemini-3-pro-image` | 20 |
| Nano Banana Flash (Gemini 2.5 Flash) | `gemini-2.5-flash-image` | 20 |
| GPT Image | `gpt-image-1-medium` | 30 |
| GPT Image 2 | `gpt-image-2` | 20 |
| Dall-E 3 | `dall-e-3` | 33 |

### Premium models

| Model Name | String | Credits/Image |
| --- | --- | --- |
| Nano Banana 2 Mini | `gemini-3.1-flash-image-mini` | 34 |
| Recraft V3 Vector | `recraft-v3-svg` | 40 |
| Recraft V4 Vector | `recraft-v4-svg` | 40 |
| Ideogram 3 Quality | `ideogram-v3-quality` | 45 |
| Nano Banana 2 | `gemini-3.1-flash-image` | 50 |
| Nano Banana Pro HD (Gemini 3 Pro HD) | `gemini-3-pro-image-hd` | 70 |
| Nano Banana 2 HD | `gemini-3.1-flash-image-hd` | 75 |

### Ultra models

| Model Name | String | Credits/Image |
| --- | --- | --- |
| Imagen 4 Ultra | `imagen-4-ultra` | 30 |
| GPT Image Detailed | `gpt-image-1-high` | 120 |
| GPT Image 2 HD | `gpt-image-2-hd` | 115 |
| Recraft V4 Pro | `recraft-v4-pro` | 125 |

### Output dimensions

Quality tiers (`low` / `medium` / `high`) affect detail and cost — not pixel count. Aspect ratio is the only parameter that changes output dimensions.

| Provider | Model(s) | 1:1 | 16:9 | 9:16 | Max side |
| --- | --- | --- | --- | --- | --- |
| OpenAI | `gpt-image-2-mini`, `gpt-image-2`, `gpt-image-2-hd` | 1024×1024 | 1536×1024 | 1024×1536 | 1536 px |
| OpenAI | `gpt-image-1-medium`, `gpt-image-1-high` | 1024×1024 | 1536×1024 | 1024×1536 | 1536 px |
| OpenAI | `gpt-image-1-mini-low`, `gpt-image-1-mini-medium`, `gpt-image-1-mini-high` | 1024×1024 | 1536×1024 | 1024×1536 | 1536 px |
| Google | `imagen-3-flash`, `imagen-4-pro`, `imagen-4-ultra` | 1024×1024 | 1408×768 | 768×1344 | 1408 px |
| Ideogram | `ideogram-v3`, `ideogram-v3-turbo`, `ideogram-v3-quality` | 1024×1024 | 1280×768 | 768×1344 | 1344 px |
| Flux | `flux-1-quick` | 1024×1024 | 1376×768 | 768×1376 | 1376 px |
| Flux | `flux-2-pro`, `flux-2-flex`, `flux-2-max`, `flux-kontext-fast`, `flux-kontext-pro` | 1440×1440 | 1920×1088 | 1088×1920 | 1920 px |
| Leonardo | `leonardo-phoenix` | 1024×1024 | 1376×768 | 768×1376 | 1376 px |
| Recraft | `recraft-v3`, `recraft-v3-svg` | 1024×1024 | 1820×1024 | 1024×1820 | 1820 px |
| Luma | `luma-photon-1`, `luma-photon-flash-1` | 1536×1536 | 2048×1152 | 1152×2048 | 2048 px |
| Gemini | `gemini-3.1-flash-image-mini`, `gemini-3.1-flash-image`, `gemini-3.1-flash-image-hd` | 1024×1024 | 1920×1080 | 1080×1920 | 1920 px |
| Gemini | `gemini-3-pro-image` | 2048×2048 | 2752×1536 | 1536×2752 | 2752 px |
| Gemini | `gemini-3-pro-image-hd` | 2048×2048 | 3840×2160 | 2160×3840 | 3840 px |
| Gemini | `gemini-2.5-flash-image` | 1024×1024 | 1920×1080 | 1080×1920 | 1920 px |

{% hint style="info" %}
OpenAI models output 3:2 / 2:3 when 16:9 / 9:16 is requested. Other providers match the requested ratio exactly.
{% endhint %}

### Related

- [Generate from text](../overview/generate-api-parameters-explained.md) for `imageOptions` guidance
- [Poll for results](../overview/async-patterns-and-polling.md) if you need longer polling windows for slower models
- [Access and Pricing](../overview/access-and-pricing.md) for plan and credit details
