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
| textMode missing from required in openapi.yaml | FIXED (added to required array) |
| Export URL lifetime undocumented | FIXED (added ~1 week across all pages) |

### Issues found, intentional by design

| Issue | Reason |
| --- | --- |
| 22 image models in spec but not in docs | Intentional: deprecated models (flux-1-*, playground-3, imagen-3-pro) removed from docs; video models removed per Deeni feedback; spec retains them for backward compatibility |
| Rate limits not documented | Intentional per product decision |
| "API Reference tab" referenced in guides | Works on published GitBook site (separate section tab); only confusing in isolated doc reading |

### Items needing eng/product input

| Item | Question |
| --- | --- |
| Card limits for Teams/Business | Only Pro (60) and Ultra (75) documented. What about Teams/Business? |
| Credit cost specifics | "1-5 credits/card" is vague. What drives the variation? |

---

## Phase 2: LLM digestibility (Claude)

Fed all 18 published pages (105K chars, 2,770 lines) to Claude as a fresh reader. Ran 15 standardized test questions across 4 categories.

### TASK 1: Comprehension

#### Q1: What header do I need for authentication?

**Answer:** `X-API-KEY` containing your API key. Also `Content-Type: application/json` for POST requests. Notably, Gamma does **not** use `Authorization: Bearer` -- the docs explicitly warn about this as a common 401 cause.

| Header | Value | Required |
|---|---|---|
| `X-API-KEY` | Your API key | Yes |
| `Content-Type` | `application/json` | Yes |

**Confidence:** HIGH. Stated consistently across multiple pages (README, overview, error codes).

#### Q2: What are the required fields for POST /generations?

**Answer:** Two required fields:
- `inputText` -- the content/topic to generate from (1 to ~400,000 characters)
- `textMode` -- one of `generate`, `condense`, or `preserve`

For the separate `POST /generations/from-template` endpoint, the required fields are different: `gammaId` + `prompt`.

**Confidence:** HIGH. Both the overview comparison table and the parameter-by-parameter page mark these as `(required)`.

#### Q3: What image models are available at the basic tier (cheapest credits)?

**Answer:** The docs label the cheapest tier "Free (All Plans)" with these models:

| Model | String | Credits/Image |
|---|---|---|
| Flux 2 Fast | `flux-2-klein` | 2 |
| Flux Kontext Fast | `flux-kontext-fast` | 2 |
| Imagen 3 Fast | `imagen-3-flash` | 2 |
| Luma Photon Flash | `luma-photon-flash-1` | 2 |
| Qwen Image Fast | `qwen-image-fast` | 3 |
| Ideogram 3 Turbo | `ideogram-v3-turbo` | 10 |

The four cheapest at 2 credits/image are Flux 2 Fast, Flux Kontext Fast, Imagen 3 Fast, and Luma Photon Flash.

**Confidence:** HIGH. The image model page has explicit tables.

**Note:** There is a terminology mismatch -- the pricing page uses "Basic models: 2 credits/image" while the image model page uses "Free (All Plans)" as the tier name. These appear to be the same tier but use different labels.

#### Q4: How do I generate a presentation in French?

**Answer:** Set `textOptions.language` to `"fr"`. Example:

```json
{
  "inputText": "Le changement climatique",
  "textMode": "generate",
  "format": "presentation",
  "textOptions": {
    "language": "fr"
  }
}
```

The language parameter works regardless of the language of `inputText` -- you can write input in English and get French output.

**Confidence:** HIGH. The output language page lists `fr` for French explicitly, and the parameter docs explain the behavior clearly.

#### Q5: What's the difference between `generate` and `preserve` text modes?

**Answer:**
- **`generate`**: Gamma uses `inputText` as a starting point and **rewrites and expands** the content. Best for brief topic descriptions you want elaborated on. Supports `textOptions.tone`, `textOptions.audience`, and `textOptions.amount`.
- **`preserve`**: Gamma **retains the exact text** from `inputText`, only structuring it where sensible (e.g., adding headings). `textOptions.tone`, `textOptions.audience`, and `textOptions.amount` are **ignored** (you'll get a warning). You can add `additionalInstructions` to request zero modifications.

There's also `condense`, which **summarizes** long input text to fit the desired content length.

**Confidence:** HIGH. Well-documented in the parameters page, and the warnings page provides concrete examples of `preserve` ignoring text options.

---

### TASK 2: Code generation

#### Q6: Python script -- generate 10-slide climate change presentation, download PDF, with polling

```python
import requests
import time
import os
import sys

API_KEY = os.environ.get("GAMMA_API_KEY")
if not API_KEY:
    print("Set GAMMA_API_KEY environment variable")
    sys.exit(1)

BASE_URL = "https://public-api.gamma.app"
HEADERS = {
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json",
}

def generate_and_download():
    payload = {
        "inputText": "Climate change: causes, effects, and solutions",
        "textMode": "generate",
        "format": "presentation",
        "numCards": 10,
        "exportAs": "pdf",
        "textOptions": {
            "amount": "medium",
            "tone": "professional, data-driven",
            "audience": "general public",
        },
        "imageOptions": {
            "source": "aiGenerated",
            "style": "photorealistic, environmental photography",
        },
    }

    response = requests.post(
        f"{BASE_URL}/v1.0/generations",
        headers=HEADERS,
        json=payload,
    )
    response.raise_for_status()
    data = response.json()
    generation_id = data["generationId"]
    print(f"Generation started: {generation_id}")

    if "warnings" in data:
        print(f"Warnings: {data['warnings']}")

    max_attempts = 60
    poll_interval = 5

    for attempt in range(1, max_attempts + 1):
        time.sleep(poll_interval)

        status_resp = requests.get(
            f"{BASE_URL}/v1.0/generations/{generation_id}",
            headers={"X-API-KEY": API_KEY},
        )

        if status_resp.status_code == 429:
            retry_after = int(status_resp.headers.get("Retry-After", 10))
            print(f"Rate limited, waiting {retry_after}s...")
            time.sleep(retry_after)
            continue

        status_resp.raise_for_status()
        result = status_resp.json()
        status = result.get("status")
        print(f"Poll {attempt}/{max_attempts}: {status}")

        if status == "completed":
            gamma_url = result.get("gammaUrl")
            export_url = result.get("exportUrl")
            credits = result.get("credits", {})
            print(f"View at: {gamma_url}")
            print(f"Credits used: {credits.get('deducted')}, remaining: {credits.get('remaining')}")

            if export_url:
                pdf_resp = requests.get(export_url)
                pdf_resp.raise_for_status()
                filename = "climate_change_presentation.pdf"
                with open(filename, "wb") as f:
                    f.write(pdf_resp.content)
                print(f"Downloaded: {filename} ({len(pdf_resp.content)} bytes)")
            return result

        elif status == "failed":
            error = result.get("error", "Unknown error")
            raise RuntimeError(f"Generation failed: {error}")

    raise TimeoutError(f"Generation did not complete after {max_attempts * poll_interval}s")


if __name__ == "__main__":
    generate_and_download()
```

**Confidence:** HIGH. Based directly on the documented polling pattern, response schema, and parameter examples.

#### Q7: cURL command with a specific theme ID

```bash
curl -X POST https://public-api.gamma.app/v1.0/generations \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: $GAMMA_API_KEY" \
  -d '{
    "inputText": "Quarterly business review for Q4 2025",
    "textMode": "generate",
    "format": "presentation",
    "numCards": 12,
    "themeId": "abc123def456ghi",
    "exportAs": "pptx"
  }'
```

To find a valid theme ID first:

```bash
curl https://public-api.gamma.app/v1.0/themes \
  -H "X-API-KEY: $GAMMA_API_KEY"
```

**Confidence:** HIGH.

#### Q8: JavaScript polling with error handling

```javascript
const API_KEY = process.env.GAMMA_API_KEY;
const BASE_URL = "https://public-api.gamma.app";

async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function generateAndWait(payload, { maxAttempts = 60, pollInterval = 5000 } = {}) {
  const startResponse = await fetch(`${BASE_URL}/v1.0/generations`, {
    method: "POST",
    headers: {
      "X-API-KEY": API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!startResponse.ok) {
    const errorBody = await startResponse.text();
    throw new Error(`Failed to start generation (${startResponse.status}): ${errorBody}`);
  }

  const { generationId, warnings } = await startResponse.json();
  console.log(`Generation started: ${generationId}`);
  if (warnings) console.warn(`Warnings: ${warnings}`);

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    await sleep(pollInterval);

    const statusResponse = await fetch(
      `${BASE_URL}/v1.0/generations/${generationId}`,
      { headers: { "X-API-KEY": API_KEY } }
    );

    if (statusResponse.status === 429) {
      const retryAfter = parseInt(statusResponse.headers.get("Retry-After") || "10", 10);
      console.warn(`Rate limited. Retrying in ${retryAfter}s...`);
      await sleep(retryAfter * 1000);
      continue;
    }

    if (!statusResponse.ok) {
      throw new Error(`Poll failed (${statusResponse.status}): ${await statusResponse.text()}`);
    }

    const result = await statusResponse.json();
    console.log(`Poll ${attempt}/${maxAttempts}: ${result.status}`);

    if (result.status === "completed") {
      return result;
    }
    if (result.status === "failed") {
      throw new Error(`Generation failed: ${JSON.stringify(result.error)}`);
    }
  }

  throw new Error(`Generation timed out after ${maxAttempts * pollInterval / 1000}s`);
}

// Usage
const result = await generateAndWait({
  inputText: "5 strategies for remote team productivity",
  textMode: "generate",
  format: "presentation",
  numCards: 8,
  exportAs: "pdf",
});

console.log(`View: ${result.gammaUrl}`);
console.log(`Download: ${result.exportUrl}`);
console.log(`Credits: ${result.credits?.deducted} used, ${result.credits?.remaining} remaining`);
```

**Confidence:** HIGH.

---

### TASK 3: Edge cases

#### Q9: Can I export to both PDF and PPTX in one request?

**Answer:** No. The docs explicitly state: *"One export format per request. You can export to PDF, PPTX, or PNG, but not multiple formats in a single API call. If you need multiple formats, make separate generation requests or export additional formats manually from the Gamma app."*

This warning appears on both the Generate API and Create from Template pages.

**Confidence:** HIGH.

#### Q10: What happens if I set `cardSplit` to `inputTextBreaks` but my text has no `\n---\n`?

**Answer:** You get **1 card**. The docs include an explicit scenario table:

| inputText has `\n---\n`? | cardSplit | numCards | Output |
|---|---|---|---|
| No | `inputTextBreaks` | 9 | **1 card** |

When `cardSplit` is `inputTextBreaks`, Gamma looks only for `\n---\n` breaks and ignores `numCards`. No breaks = no splits = one card containing all content.

**Confidence:** HIGH. The table makes this unambiguous.

#### Q11: Can Free plan users use the API?

**Answer:** It depends on what you mean by "the API":
- **API keys (direct REST calls, Zapier, Make, n8n):** No. Requires Pro, Ultra, Teams, or Business plan.
- **Connectors (ChatGPT, Claude, Superhuman Go, Atlassian Rovo):** Yes, available on **all plans including Free**. No API key needed. Credits are still charged.
- **MCP server:** Available on all plans.

**Confidence:** HIGH. Stated on the access-and-pricing page and the connectors page.

#### Q12: What's the maximum number of cards I can create?

**Answer:**
- **Pro plan:** 1-60 cards
- **Ultra plan:** 1-75 cards

The docs don't specify limits for Plus, Teams, or Business plans individually.

**Confidence:** MEDIUM. The numbers are stated clearly for Pro and Ultra, but there's no mention of what Teams or Business get. The overview quick-reference says "1-75 depending on plan" as the range.

---

### TASK 4: Confusion detection

#### Q13: Unclear, contradictory, or confusing parts

1. **"Basic/Advanced/Premium/Ultra" vs. plan-based model tiers.** The pricing page describes credit costs as "Basic models: 2 credits/image. Advanced models: 7-20. Premium models: 20-70. Ultra models: 30-125." But the image models page organizes models by **plan tier** (Free, Plus, Pro, Ultra). These are two different classification axes and there's no mapping between them. A reader doesn't know which plan-tier models correspond to "basic" vs "premium" pricing labels.

2. **The `POST /gammas/{gammaId}/archive` endpoint is referenced but never documented.** It appears in the "API scope and limits" page's capabilities table, but there's no parameter reference, response schema, or dedicated page for it. It's also missing from the README's endpoint table.

3. **"API Reference tab" is referenced repeatedly but not included.** Multiple pages say "For the exact request body, field types, and response schema, use the API Reference tab." This combined doc doesn't include that tab, so the exact JSON schema (required vs. optional fields, field types, enums) is never formally specified.

4. **The "Nano Banana 2" section in image models is a model family, not a plan tier.** Every other section header is a plan name (Free, Plus, Pro, Ultra), but "Nano Banana 2" breaks the pattern. It's unclear which plan is required to access these models.

5. **Card credit costs are vague.** The pricing page says "1-5 credits/card" and that costs "vary depending on the AI model used for text generation," but never specifies the actual mapping. Template-based generations "may cost slightly more" -- how much more is undefined.

6. **`emailOptions` JSON examples have unclosed braces.** Both the Generate and Template pages show `sharingOptions.emailOptions` examples with missing closing braces, which could trip up developers copying examples.

**Confidence:** HIGH -- these are real gaps, not misreadings.

#### Q14: Undocumented or inconsistently described parameters

1. **`POST /gammas/{gammaId}/archive`** -- mentioned once in a table, never documented anywhere.

2. **`User / Get Me` operation** -- the n8n integration section mentions a "Get Me" operation that returns "authenticated user and workspace info." This implies a `/me` or `/user` endpoint exists, but it's not in the endpoint table or documented anywhere.

3. **The `textMode` field** -- the parameter page marks it `(required)`, but the overview comparison table says the required fields for POST /generations are "`inputText` + `textMode`" while for POST /generations/from-template they are "`prompt` + `gammaId`". The template endpoint page doesn't mention `textMode` at all, which is consistent. No issues here, but worth noting for template users who might wonder.

4. **Rate limit specifics** -- the docs mention 429 errors and `Retry-After` headers but never state the actual rate limits (requests per minute, concurrent generation limits, etc.).

5. **`exportUrl` expiration** -- described as "temporary signed URLs" with advice to "download promptly," but no concrete expiration window is given (1 hour? 24 hours? 7 days?).

**Confidence:** HIGH.

#### Q15: Top 3 things I'd want clarified before building an integration

1. **Concrete rate limits.** The docs say to use 5-second polling intervals and mention 429 errors, but never state the actual limits. For a production integration, I need to know: How many generations can I start per minute? How many concurrent generations? Is there a per-IP or per-key limit? Without this, capacity planning is guesswork.

2. **The `POST /gammas/{gammaId}/archive` endpoint.** It's the only write endpoint besides generation, and it's referenced as the workaround for "updating content after generation." But there's no documentation on its request body, response format, error codes, or whether it's idempotent. I can't safely use it.

3. **Export URL lifetime and retry behavior.** The docs say export URLs are "temporary" but never specify how long they last. If my download fails, can I re-poll `GET /generations/{id}` to get a fresh URL, or is the export URL fixed at generation time? This matters for reliability in automated pipelines.

**Confidence:** HIGH. These are genuine blockers for production-grade integrations.

---

### Results summary

| Task | Questions | Fully Answered | Partially Answered | Unanswerable |
|---|---|---|---|---|
| Comprehension (Q1-Q5) | 5 | 5 | 0 | 0 |
| Code Generation (Q6-Q8) | 3 | 3 | 0 | 0 |
| Edge Cases (Q9-Q12) | 4 | 3 | 1 (Q12 - missing Teams/Business limits) | 0 |
| Confusion Detection (Q13-Q15) | 3 | 3 | 0 | 0 |

**Overall assessment:** The documentation is well-structured and covers the happy path thoroughly. The parameter-by-parameter guide, polling examples in three languages, and the warnings page are particularly strong. The main gaps are operational details (rate limits, export URL lifetimes, credit cost specifics) and the undocumented archive endpoint. The repeated references to an "API Reference tab" that isn't present in this combined document create a reliance on external content for the exact JSON schema.

---

## Resolutions applied after testing

| Finding | Resolution |
| --- | --- |
| Q6 emailOptions unclosed braces (Q13.6) | FIXED in commit ca612d0 |
| Q13.4 Nano Banana 2 section header | FIXED -- added "(Pro Plan)" in commit ca612d0 |
| Q14.1 Archive endpoint referenced | FIXED -- removed references in commit ca612d0 |
| Q14.2 /me endpoint leaking | Already excluded via @ApiExcludeEndpoint in PR #17131 (pending merge) |
| Q14.5 Export URL expiration | FIXED -- documented as ~1 week in commit e120f7d |
| Q2 textMode required | FIXED -- added to required in openapi.yaml in commit e120f7d |
| Q14.4 Rate limits | Intentionally not documented per product decision |

### ChatGPT test

Requires manual login. Browser automation could not authenticate. Same 15 questions are ready to run manually by pasting the concatenated docs from `/tmp/gamma-docs-combined.md` into a fresh ChatGPT conversation.
