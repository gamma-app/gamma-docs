# Docs Style Guide

Use this file to keep GitBook pages visually consistent across the Gamma docs site. Every page in the repo should conform to the rules below. When in doubt, check a representative page of the same type for the current pattern.

## Heading hierarchy

- One `#` per page. This is the page title.
- `##` for major sections.
- `###` only inside an existing `##` section.
- Never use `####` or deeper. Use bold text for sub-labels inside a `###` section.
- Prefer sentence case for all headings.

## Required sections by page type

Every page must include the sections marked "required" for its type. Optional sections can be omitted when they add no value.

### Landing pages

| Order | Section | Required |
| --- | --- | --- |
| 1 | Short hero intro + CTA buttons | yes |
| 2 | `## Quickstart` | yes |
| 3 | `## Endpoints` or equivalent discovery section | yes |
| 4 | `## What's new` | optional |
| 5 | `## Next steps` or `## Resources` | yes |

### Guide pages

| Order | Section | Required |
| --- | --- | --- |
| 1 | Short intro (1-3 sentences) | yes |
| 2 | `## Quick reference` (bullet list of the most important facts) | yes |
| 3 | Main instructional sections under `##` headings | yes |
| 4 | Troubleshooting or caveats | optional |
| 5 | `## Related` (bullet list of 2-4 links) | yes |

### Endpoint reference pages

| Order | Section | Required |
| --- | --- | --- |
| 1 | One-sentence explanation under the `#` title | yes |
| 2 | `{% openapi-operation %}` block | yes |
| 3 | One short guidance `{% hint %}` if needed | optional |
| 4 | `## Related` (bullet list of 2-4 links) | yes |

### Reference data pages

| Order | Section | Required |
| --- | --- | --- |
| 1 | Short intro | yes |
| 2 | `## Quick reference` (bullet list) | yes |
| 3 | Table or list of accepted values | yes |
| 4 | `## Related` (bullet list of 2-4 links) | yes |

## Image sizing

All images must have an explicit `width` attribute. Do not let images render at their native resolution.

| Context | Width | Example |
| --- | --- | --- |
| Hero / decorative image in a column layout | `width="563"` | Homepage hero |
| Instructional screenshot, standalone | `width="563"` | API key settings, billing credits |
| Instructional screenshot in a two-column layout | `width="375"` | Template ID, example outputs |
| Example output with `data-with-frame` in a column | `width="375"` | API Overview example cards |

### Instructional screenshots

- Always include a meaningful `alt` attribute.
- Always include a short caption explaining the takeaway.
- Use `data-with-frame="true"` for product screenshots that show the Gamma UI.
- Do not use `data-with-frame` for code output or JSON examples.

```html
<figure>
  <img src="../.gitbook/assets/example.png"
       alt="Where to find the theme ID in Gamma"
       width="563">
  <figcaption><p>Copy the theme ID from the Gamma app before making the request.</p></figcaption>
</figure>
```

### Decorative / hero images

- No caption needed.
- Empty `alt=""` is acceptable.
- Use only on landing pages.

```html
<figure>
  <img src=".gitbook/assets/hero.png" alt="" width="563">
</figure>
```

## GitBook blocks

### `stepper`

Use for ordered workflows with 3-6 sequential steps where each step is a distinct user action (e.g., connector setup flows).

### `tabs`

Use for language variants (cURL / Python / JavaScript) or platform variants (Claude / ChatGPT / Zapier) of the same task.

Do not stack multiple heading levels immediately around tabs.

### `hint`

| Style | Use for |
| --- | --- |
| `warning` | Constraints that prevent success if ignored |
| `info` | Orientation notes that save the reader time |
| `success` | Proven best practices or recommended patterns |

Do not use `hint` for ordinary examples, filler emphasis, or content that works as plain prose.

### `columns`

Use for side-by-side image comparisons or hero layouts. Always set image widths inside columns explicitly.

## Tables, cards, and surfaced content

- Use markdown tables for compact reference data.
- Use GitBook card tables only for navigation or discovery blocks.
- Do not use card tables for ordinary best-practice bullets.
- End every guide page with a simple `## Related` bullet list.

## Content hierarchy

- Keep the most important user action near the top of the page.
- Put details after the quick reference, not before it.
- Avoid duplicated landing-page content that drifts over time.
- If two pages serve different spaces (e.g., `home/README.md` vs `README.md`), make their roles distinct.

## Editorial tone

- Prefer direct, specific language over promotional language.
- Explain why a user would choose a workflow, not just what the parameter name is.
- Keep examples realistic and concise.
- Use sentence case for headings, not title case.

## Page checklist

Use this checklist before merging any docs change:

- [ ] Page has exactly one `#` heading
- [ ] All sections use `##` or `###` only (no `####`)
- [ ] `## Quick reference` is present (guide and reference pages)
- [ ] `## Related` is present with 2-4 links
- [ ] All images have an explicit `width` attribute
- [ ] All instructional screenshots have meaningful `alt` and a caption
- [ ] No back-to-back `hint` blocks unless one is a true warning
- [ ] Polling interval is consistently 5 seconds across all examples
- [ ] Headings use sentence case
