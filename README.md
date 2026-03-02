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

{% hint style="info" %}
**Polling tip:** Some models — particularly Ultra-tier, HD, and video models — take longer to generate than standard models. If using these via the API, we recommend increasing your polling timeout to 10 minutes with 30-second intervals to avoid premature timeouts.
{% endhint %}

{% hint style="warning" %}
**Plan Requirements:** Some models require a specific Gamma plan (Plus, Pro, or Ultra). Models are grouped by minimum plan tier below.
{% endhint %}

## Free (All Plans)

| Model Name | String | Credits/Image |
| --- | --- | --- |
| Flux 2 Fast | `flux-2-klein` | 2 |
| Flux Kontext Fast | `flux-kontext-fast` | 2 |
| Imagen 3 Fast | `imagen-3-flash` | 2 |
| Luma Photon Flash | `luma-photon-flash-1` | 2 |
| Ideogram 3 Turbo | `ideogram-v3-turbo` | 10 |
| Qwen Image Fast | `qwen-image-fast` | 3 |

## Plus Plan

| Model Name | String | Credits/Image |
| --- | --- | --- |
| Flux 2 Pro | `flux-2-pro` | 8 |
| Imagen 4 Fast | `imagen-4-fast` | 10 |
| Luma Photon | `luma-photon-1` | 10 |
| Recraft V4 | `recraft-v4` | 12 |
| Leonardo Phoenix | `leonardo-phoenix` | 15 |
| Nano Banana Flash (Gemini 2.5 Flash) | `gemini-2.5-flash-image` | 20 |
| Qwen Image | `qwen-image` | 3 |

## Pro Plan

| Model Name | String | Credits/Image |
| --- | --- | --- |
| Flux 2 Flex | `flux-2-flex` | 20 |
| Flux 2 Max | `flux-2-max` | 20 |
| Flux Kontext Pro | `flux-kontext-pro` | 20 |
| Ideogram 3 | `ideogram-v3` | 20 |
| Imagen 4 | `imagen-4-pro` | 20 |
| Recraft V3 | `recraft-v3` | 20 |
| Nano Banana Pro (Gemini 3 Pro) | `gemini-3-pro-image` | 20 |
| GPT Image | `gpt-image-1-medium` | 30 |
| Dall-E 3 | `dall-e-3` | 33 |
| Recraft V3 Vector | `recraft-v3-svg` | 40 |
| Recraft V4 Vector | `recraft-v4-svg` | 40 |

## Nano Banana 2

| Model Name | String | Credits/Image | Resolution |
| --- | --- | --- | --- |
| Nano Banana 2 Mini | `gemini-3.1-flash-image-mini` | 34 | 1K |
| Nano Banana 2 | `gemini-3.1-flash-image` | 50 | 2K |
| Nano Banana 2 HD | `gemini-3.1-flash-image-hd` | 75 | 4K |

## Ultra Plan

| Model Name | String | Credits/Image |
| --- | --- | --- |
| Imagen 4 Ultra | `imagen-4-ultra` | 30 |
| Ideogram 3 Quality | `ideogram-v3-quality` | 45 |
| Nano Banana Pro HD (Gemini 3 Pro HD) | `gemini-3-pro-image-hd` | 70 |
| GPT Image Detailed | `gpt-image-1-high` | 120 |
| Recraft V4 Pro | `recraft-v4-pro` | 125 |

## Video Models (Ultra Plan)

{% hint style="info" %}
Video models may take significantly longer to generate (up to several minutes). If using these via the API, we recommend polling for up to 10 minutes with 30-second intervals.
{% endhint %}

| Model Name | String | Credits/Video |
| --- | --- | --- |
| Leonardo Motion 2 Fast | `leonardo-motion-2-fast` | 98 |
| Luma Ray 2 Flash | `luma-ray-2-flash` | 120 |
| Leonardo Motion 2 | `leonardo-motion-2` | 195 |
| Veo 3.1 Fast | `veo-3.1-fast` | 300 |
| Luma Ray 2 | `luma-ray-2` | 350 |
| Veo 3.1 | `veo-3.1` | 800 |

## Deprecated Models

The following models have been replaced. If you pass these values, Gamma will automatically redirect to the replacement model.

| Deprecated Model | Replacement |
| --- | --- |
| `flux-1-quick` | `flux-2-klein` |
| `flux-1-pro` | `flux-2-pro` |
| `flux-1-ultra` | `flux-2-max` |
| `flux-kontext-max` | `flux-2-flex` |
| `playground-3` | `flux-2-pro` |
| `imagen-3-pro` | `imagen-4-pro` |
