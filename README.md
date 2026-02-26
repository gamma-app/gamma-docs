---
description: >-
  When creating AI generated images in your gamma, you can specify which model
  to use.
icon: image
---

# Image model accepted values

* In the `imageOptions.source` parameter, use `aiGenerated` as the value.
* In the `imageOptions.model` parameter, use one of the strings below.
* Conversely, if you're not sure which image model you'd like to use, you can leave the `imageOptions.model` parameter blank and Gamma will select a model for you.

{% hint style="warning" %}
**Plan Requirements:** Some models require a Gamma Ultra subscription. Models available on all plans are listed first, Ultra-only models are listed separately below.
{% endhint %}

## Available on All Plans

| Model Name                  | String                   | Credits/Image |
| --------------------------- | ------------------------ | ------------- |
| Flux Fast 1.1               | `flux-1-quick`           | 2             |
| Flux Kontext Fast           | `flux-kontext-fast`      | 2             |
| Imagen 3 Fast               | `imagen-3-flash`         | 2             |
| Luma Photon Flash           | `luma-photon-flash-1`    | 2             |
| Flux Pro                    | `flux-1-pro`             | 8             |
| Imagen 3                    | `imagen-3-pro`           | 8             |
| Ideogram 3 Turbo            | `ideogram-v3-turbo`      | 10            |
| Luma Photon                 | `luma-photon-1`          | 10            |
| Leonardo Phoenix            | `leonardo-phoenix`       | 15            |
| Flux Kontext Pro            | `flux-kontext-pro`       | 20            |
| Gemini 2.5 Flash            | `gemini-2.5-flash-image` | 20            |
| Ideogram 3                  | `ideogram-v3`            | 20            |
| Imagen 4                    | `imagen-4-pro`           | 20            |
| Recraft                     | `recraft-v3`             | 20            |
| GPT Image                   | `gpt-image-1-medium`     | 30            |
| Dall E 3                    | `dall-e-3`               | 33            |
| Recraft Vector Illustration | `recraft-v3-svg`         | 40            |

## Ultra Plan Only

| Model Name           | String                | Credits/Image |
| -------------------- | --------------------- | ------------- |
| Flux Ultra           | `flux-1-ultra`        | 30            |
| Imagen 4 Ultra       | `imagen-4-ultra`      | 30            |
| Flux Kontext Max     | `flux-kontext-max`    | 40            |
| Ideogram 3.0 Quality | `ideogram-v3-quality` | 45            |
| GPT Image Detailed   | `gpt-image-1-high`    | 120           |
