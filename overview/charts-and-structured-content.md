---
description: >-
  How to get the best chart, table, and structured visual results from the
  Gamma API.
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

# Add charts and structured content

The Gamma API can generate charts, tables, and infographics as part of your output. Generation is non-deterministic — results may vary across runs, even with identical inputs. There are no API parameters to directly control chart type, styling, or data formatting, but you can steer the output through your prompts.

### Quick reference

- Charts are prompted through `inputText` and `additionalInstructions`, not through dedicated API parameters.
- Provide explicit data values and chart type for best results.
- Use the Create from Template API for consistent chart layouts across repeated generations.
- Output varies between runs -- test a few generations to calibrate your prompts.

### How to prompt for charts

You influence chart output through `inputText` and `additionalInstructions`. The more specific you are, the better the results.

{% tabs %}
{% tab title="Vague (less predictable)" %}
```json
{
  "inputText": "Revenue data for 2024",
  "additionalInstructions": "Include a chart"
}
```
{% endtab %}

{% tab title="Specific (more predictable)" %}
```json
{
  "inputText": "Revenue by quarter:\nQ1: $1.2M\nQ2: $1.5M\nQ3: $1.8M\nQ4: $2.1M",
  "additionalInstructions": "Display this data as a bar chart with quarters on the x-axis and revenue on the y-axis"
}
```
{% endtab %}
{% endtabs %}

### Tips for better results

* **Specify the chart type.** "Bar chart comparing X and Y" produces more predictable output than "include a chart."
* **Provide structured data.** Explicit values (tables, bullet points with numbers) give the AI clear data to work with.
* **Use `additionalInstructions`** to reinforce preferences: "Use bar charts for comparisons, pie charts for proportions."
* **Keep data labels unambiguous.** Labels that resemble numeric values (e.g. `$100` as a category name) may be interpreted as data.
* **Test a few runs.** Since output varies, run a few generations to see the range and refine your prompts accordingly.

### Using templates for more consistent output

If you need predictable chart layouts, the [Create from Template API](create-from-template-api-parameters-explained.md) is a better fit. Design a gamma in the app with the exact chart types and layouts you want, then use the API to generate new content into that structure.


### Tables and infographics

The same prompting principles apply:

* Provide structured data (rows, columns, key-value pairs) in your input for best table results
* Infographics such as timelines and process flows can be prompted for, but the AI determines the final layout
* Your theme controls styling for all structured content

### Related

- [Generate from text](generate-api-parameters-explained.md) for `inputText` and `additionalInstructions` usage
- [Generate from template](create-from-template-api-parameters-explained.md) for consistent chart layouts
- [Image URL best practices](image-url-best-practices.md) if you want to include your own chart images
