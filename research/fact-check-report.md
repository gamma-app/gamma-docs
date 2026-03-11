# Fact-check and LLM digestibility report

Generated: 2026-03-10

## Phase 1: Spec vs docs fact-check

Ran automated cross-reference of all documentation against `openapi.yaml` (961 lines, 6 endpoints, 15 schemas).

### Issues found and resolved

| Issue | Status |
| --- | --- |
| emailOptions JSON examples had unclosed braces (4 instances) | FIXED |
| Archive endpoint still referenced in API scope page after nav removal | FIXED |
| Nano Banana 2 section broke plan-tier heading pattern | FIXED (added "Pro Plan") |

### Issues found, intentional by design

| Issue | Reason |
| --- | --- |
| 22 image models in spec but not in docs | Intentional: deprecated models (flux-1-*, playground-3, imagen-3-pro) removed from docs; video models removed per Deeni feedback; spec retains them for backward compatibility |
| textMode marked required in docs but optional in spec | Likely server-side validation not reflected in spec; needs eng confirmation |
| "API Reference tab" referenced in guides | Works on published GitBook site (separate section tab); only confusing in isolated doc reading |

### Items needing eng/product input

| Item | Question |
| --- | --- |
| textMode required? | Spec says only inputText required; docs say textMode is also required. Which is correct? |
| Rate limits | Not documented. What are the actual limits? |
| Export URL lifetime | Docs say "temporary" but no timeframe. How long do URLs last? |
| Card limits for Teams/Business | Only Pro (60) and Ultra (75) documented. What about Teams/Business? |

## Phase 2: LLM digestibility (Claude)

Fed all 18 published pages (105K chars) to Claude as a fresh reader. Ran 15 standardized test questions.

### Results summary

| Category | Questions | Pass | Partial | Fail |
| --- | --- | --- | --- | --- |
| Comprehension | 5 | 5 | 0 | 0 |
| Code generation | 3 | 3 | 0 | 0 |
| Edge cases | 4 | 3 | 1 | 0 |
| Confusion detection | 3 | 3 | 0 | 0 |

### What worked well

- Authentication header correctly identified with high confidence
- All code samples (Python, cURL, JavaScript) were functional and included proper polling, error handling, and rate limit awareness
- Edge cases (one export per request, cardSplit behavior, Free plan limitations) correctly understood
- Parameter documentation clear enough to generate accurate code on first read

### Partial answer

- Q12 (max cards): Docs only specify Pro (60) and Ultra (75). Teams/Business limits not mentioned.

### Documentation gaps Claude identified

1. **"Basic/Advanced/Premium/Ultra" pricing labels vs "Free/Plus/Pro/Ultra" plan tiers** -- two different classification axes with no mapping between them in the credit cost table vs the image models page
2. **Rate limits not specified** -- 429 errors mentioned but no actual limits given
3. **Export URL lifetime** -- "temporary" without a timeframe
4. **n8n "Get Me" operation** -- implies a /me or /user endpoint that isn't documented
5. **Card credit costs vague** -- "1-5 credits/card" with no specifics on what drives the variation

### ChatGPT test

Requires manual login. Browser automation could not authenticate. Recommend testing manually by pasting docs into a fresh ChatGPT conversation and running the same 15 questions.

## Overall assessment

The documentation is highly digestible by LLMs. Claude answered 14/15 questions correctly with high confidence and generated working code in all three languages. The main gaps are operational details (rate limits, URL lifetimes, pricing specifics) rather than structural or comprehension issues.
