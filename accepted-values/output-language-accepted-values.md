---
description: Specify the output language of your gamma.
icon: language
---

# Output language accepted values

You can create gammas in different languages. To specify the output language of your gamma, use the appropriate string in the `textOptions.language` parameter. If nothing is specified in this parameter, Gamma creates your output in `en`, ie English (US).

## Quick reference

- Set `textOptions.language` to one of the keys below.
- Each generation request produces output in a single language.
- If you need multiple language variants, make separate generation requests.

| Language                | Key      |
| ----------------------- | -------- |
| Afrikaans               | `af`     |
| Albanian                | `sq`     |
| Arabic                  | `ar`     |
| Arabic (Saudi Arabia)   | `ar-sa`  |
| Bengali                 | `bn`     |
| Bosnian                 | `bs`     |
| Bulgarian               | `bg`     |
| Catalan                 | `ca`     |
| Croatian                | `hr`     |
| Czech                   | `cs`     |
| Danish                  | `da`     |
| Dutch                   | `nl`     |
| English (India)         | `en-in`  |
| English (UK)            | `en-gb`  |
| English (US)            | `en`     |
| Estonian                | `et`     |
| Finnish                 | `fi`     |
| French                  | `fr`     |
| German                  | `de`     |
| Greek                   | `el`     |
| Gujarati                | `gu`     |
| Hausa                   | `ha`     |
| Hebrew                  | `he`     |
| Hindi                   | `hi`     |
| Hungarian               | `hu`     |
| Icelandic               | `is`     |
| Indonesian              | `id`     |
| Italian                 | `it`     |
| Japanese (です/ます style)  | `ja`     |
| Japanese (だ/である style)  | `ja-da`  |
| Kannada                 | `kn`     |
| Kazakh                  | `kk`     |
| Korean                  | `ko`     |
| Latvian                 | `lv`     |
| Lithuanian              | `lt`     |
| Macedonian              | `mk`     |
| Malay                   | `ms`     |
| Malayalam               | `ml`     |
| Marathi                 | `mr`     |
| Norwegian               | `nb`     |
| Persian                 | `fa`     |
| Polish                  | `pl`     |
| Portuguese (Brazil)     | `pt-br`  |
| Portuguese (Portugal)   | `pt-pt`  |
| Romanian                | `ro`     |
| Russian                 | `ru`     |
| Serbian                 | `sr`     |
| Simplified Chinese      | `zh-cn`  |
| Slovenian               | `sl`     |
| Spanish                 | `es`     |
| Spanish (Latin America) | `es-419` |
| Spanish (Mexico)        | `es-mx`  |
| Spanish (Spain)         | `es-es`  |
| Swahili                 | `sw`     |
| Swedish                 | `sv`     |
| Tagalog                 | `tl`     |
| Tamil                   | `ta`     |
| Telugu                  | `te`     |
| Thai                    | `th`     |
| Traditional Chinese     | `zh-tw`  |
| Turkish                 | `tr`     |
| Ukrainian               | `uk`     |
| Urdu                    | `ur`     |
| Uzbek                   | `uz`     |
| Vietnamese              | `vi`     |
| Welsh                   | `cy`     |
| Yoruba                  | `yo`     |

## Related

- [Generate from text](../overview/generate-api-parameters-explained.md) for where `textOptions.language` fits into the full request
- [Create from template](../overview/create-from-template-api-parameters-explained.md) if you want to reuse a layout in multiple languages
