# Docs Style Guide

Use this file to keep GitBook pages visually consistent across the Gamma docs site.

## Core rules

- Use one `#` heading per page.
- Use `##` for major sections.
- Use `###` only inside an existing `##` section.
- Prefer sentence case for headings.
- Keep intros short: 1-3 sentences that explain what the page is for.

## Page templates

### Landing pages

Recommended order:

1. Short hero intro
2. Primary CTA
3. `## Quickstart`
4. `## What you can do` or equivalent discovery section
5. `## What's new`
6. `## Next steps` or `## Resources`

### Guide pages

Recommended order:

1. Short intro
2. `## Quick reference`
3. Main instructional sections
4. Troubleshooting or caveats if needed
5. `## Related`

### Endpoint reference pages

Recommended order:

1. One-sentence explanation under the H1
2. OpenAPI block
3. One short guidance hint if needed
4. `## Related`

### Reference data pages

Recommended order:

1. Short intro
2. `## Quick reference`
3. Table or list of accepted values
4. `## Related`

## GitBook blocks

### Use `stepper` for

- Ordered workflows with 3-6 sequential steps
- Setup instructions where each step is a user action

### Use `tabs` for

- Language variants of the same example
- Platform variants of the same task

Do not stack multiple heading levels immediately around tabs unless they clarify the workflow.

### Use `hint` for

- True warnings that prevent success
- Short orientation notes that save users time

Avoid using `hint` blocks for ordinary examples or filler emphasis. If plain prose works, use plain prose.

## Images

Treat images as one of two types only.

### Decorative or hero images

- Use for landing pages only
- No caption
- Empty `alt` is acceptable if the image is purely decorative
- Keep a consistent fixed width across similar hero sections

### Instructional screenshots

- Always include meaningful `alt`
- Always include a short caption that explains the takeaway
- Use the same framing treatment for the same screenshot type

Preferred pattern:

```html
<div data-with-frame="true">
  <figure>
    <img src="../.gitbook/assets/example.png" alt="Where to find the theme ID in Gamma">
    <figcaption><p>Copy the theme ID from the Gamma app before making the request.</p></figcaption>
  </figure>
</div>
```

## Tables, cards, and surfaced content

- Use markdown tables for compact reference data.
- Use cards only for navigation or discovery.
- Do not use card tables for ordinary best-practice bullets.
- End substantial guides with a simple `## Related` list unless a stronger card treatment is clearly helpful.

## Content hierarchy

- Keep the most important user action near the top of the page.
- Put details after the quick reference, not before it.
- Avoid duplicated landing-page content that drifts over time.
- If two pages serve different spaces, make their roles distinct instead of lightly rephrasing the same sections.

## Editorial tone

- Prefer direct, specific language over promotional language.
- Explain why a user would choose a workflow, not just what the parameter name is.
- Keep examples realistic and concise.
