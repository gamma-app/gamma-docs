---
description: Understanding how to work with Gamma’s asynchronous API and poll for results
icon: arrows-rotate
---

# Async Patterns & Polling

Gamma generation is asynchronous. You start a generation, receive a `generationId` immediately, then poll the status endpoint until the result is ready.

## Quick reference

- `POST /v1.0/generations` returns `generationId` only.
- Poll `GET /v1.0/generations/{generationId}` every 5 seconds until `status` is `completed` or `failed`.
- `gammaUrl` and `exportUrl` are only available from the completed status response.
- Export URLs are temporary signed URLs, so download exported files promptly.

## The basic flow

```text
POST /generations      →  Returns { generationId: "abc123" }
Wait ~5 seconds
GET /generations/abc123  →  Returns { status: "pending" }
Wait ~5 seconds  
GET /generations/abc123  →  Returns { status: "completed", gammaUrl: "...", exportUrl: "..." }
```

## What you get back

When status is `completed`, the response includes:

| Field       | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| `gammaUrl`  | Direct link to view/share the presentation in Gamma                 |
| `exportUrl` | Download URL for the exported file (if `exportAs` was specified)    |

## Generation states

| Status      | Meaning              | What to Do                                    |
| ----------- | -------------------- | --------------------------------------------- |
| `pending`   | Still generating     | Keep polling every 5 seconds                  |
| `completed` | Done!                | Stop polling — use `gammaUrl` and export URLs |
| `failed`    | Something went wrong | Stop polling, check the `error` object        |

## Code examples

{% tabs %}
{% tab title="Python" %}
```python
import requests
import time

API_KEY = "sk-gamma-xxxxx"
BASE_URL = "https://public-api.gamma.app"

def generate_and_wait(payload, max_attempts=60, poll_interval=5):
    """Generate a gamma and wait for completion."""
    
    # Step 1: Start generation
    response = requests.post(
        f"{BASE_URL}/v1.0/generations",
        headers={
            "X-API-KEY": API_KEY,
            "Content-Type": "application/json"
        },
        json=payload
    )
    response.raise_for_status()
    generation_id = response.json()["generationId"]
    print(f"Generation started: {generation_id}")
    
    # Step 2: Poll for completion
    for attempt in range(max_attempts):
        time.sleep(poll_interval)
        
        status_response = requests.get(
            f"{BASE_URL}/v1.0/generations/{generation_id}",
            headers={"X-API-KEY": API_KEY}
        )
        status_response.raise_for_status()
        result = status_response.json()
        
        status = result.get("status")
        print(f"Attempt {attempt + 1}: {status}")
        
        if status == "completed":
            return result  # Success! Contains gammaUrl
        elif status == "failed":
            raise Exception(f"Generation failed: {result.get('error')}")
        # status == "pending" - keep polling
    
    raise TimeoutError("Generation timed out")

# Usage
result = generate_and_wait({
    "inputText": "Create a presentation about renewable energy",
    "textMode": "generate",
    "format": "presentation",
    "numCards": 8
})
print(f"Done! View at: {result['gammaUrl']}")
```
{% endtab %}

{% tab title="JavaScript" %}
```javascript
const API_KEY = "sk-gamma-xxxxx";
const BASE_URL = "https://public-api.gamma.app";

async function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function generateAndWait(payload, maxAttempts = 60, pollInterval = 5000) {
  // Step 1: Start generation
  const startResponse = await fetch(`${BASE_URL}/v1.0/generations`, {
    method: "POST",
    headers: {
      "X-API-KEY": API_KEY,
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });
  
  if (!startResponse.ok) {
    throw new Error(`Failed to start: ${await startResponse.text()}`);
  }
  
  const { generationId } = await startResponse.json();
  console.log(`Generation started: ${generationId}`);
  
  // Step 2: Poll for completion
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    await sleep(pollInterval);
    
    const statusResponse = await fetch(
      `${BASE_URL}/v1.0/generations/${generationId}`,
      { headers: { "X-API-KEY": API_KEY } }
    );
    
    const result = await statusResponse.json();
    console.log(`Attempt ${attempt + 1}: ${result.status}`);
    
    if (result.status === "completed") {
      return result; // Success!
    } else if (result.status === "failed") {
      throw new Error(`Generation failed: ${JSON.stringify(result.error)}`);
    }
    // status === "pending" - keep polling
  }
  
  throw new Error("Generation timed out");
}

// Usage
generateAndWait({
  inputText: "Create a presentation about renewable energy",
  textMode: "generate",
  format: "presentation",
  numCards: 8
}).then(result => {
  console.log(`Done! View at: ${result.gammaUrl}`);
});
```
{% endtab %}

{% tab title="cURL" %}
```bash
# Step 1: Start generation
GENERATION_ID=$(curl -s -X POST "https://public-api.gamma.app/v1.0/generations" \
  -H "X-API-KEY: sk-gamma-xxxxx" \
  -H "Content-Type: application/json" \
  -d '{
    "inputText": "Create a presentation about renewable energy",
    "textMode": "generate",
    "format": "presentation",
    "numCards": 8
  }' | jq -r '.generationId')

echo "Generation ID: $GENERATION_ID"

# Step 2: Poll until complete
while true; do
  sleep 5
  RESULT=$(curl -s "https://public-api.gamma.app/v1.0/generations/$GENERATION_ID" \
    -H "X-API-KEY: sk-gamma-xxxxx")
  
  STATUS=$(echo $RESULT | jq -r '.status')
  echo "Status: $STATUS"
  
  if [ "$STATUS" = "completed" ]; then
    echo "Done! URL: $(echo $RESULT | jq -r '.gammaUrl')"
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed: $(echo $RESULT | jq -r '.error')"
    exit 1
  fi
done
```
{% endtab %}
{% endtabs %}

## Using Automation Platforms

Popular automation platforms have built-in ways to handle delays and polling:

### Zapier

Use the **Delay** action between your HTTP Request steps:

1. **HTTP Request** (POST) → Start generation, get `generationId`
2. **Delay for** → Wait 30-60 seconds
3. **HTTP Request** (GET) → Check status with the `generationId`
4. Use **Paths** or **Filter** to check if `status` equals `completed`
5. If still pending, use **Looping by Zapier** to repeat steps 2-4

Zapier's "Delay for" action pauses your Zap for a specified time (minimum 1 minute). For most Gamma generations, a single 60-second delay followed by a status check works well.

### Make (formerly Integromat)

Use the **Sleep** module or a polling pattern:

1. **HTTP** module → POST to start generation
2. **Sleep** module → Wait 30 seconds
3. **HTTP** module → GET to check status
4. **Router** with filter → Check if `status` is `completed`
5. Use **Repeater** + **Sleep** for polling loop

### n8n

Use the **Wait** node with time interval:

1. **HTTP Request** node → POST to start generation
2. **Wait** node → Set to "After Time Interval" (30-60 seconds)
3. **HTTP Request** node → GET to check status
4. **IF** node → Check `status === "completed"`
5. Loop back to Wait node if still pending

n8n's Wait node offloads execution data to the database during longer waits, so your workflow won't timeout even for complex generations.

## Best practices

- Use 5-second polling intervals. Polling more frequently will not speed up the generation and may increase the chance of rate limiting.
- Set a maximum timeout. Most generations complete within 2-3 minutes, so a 5-minute ceiling is a good default for automation.
- Handle all three states: `pending`, `completed`, and `failed`.
- Use exponential backoff if you receive a 429 response.

## Working with charts and data visualizations

The Generate API can create charts and infographics through prompting, but output varies based on how you structure your request. Here's how to get the most consistent results.

**Include your exact data in the prompt.** Provide your data as a small table or bullet points along with the chart type you want (bar, line, pie), axes labels, and any specific formatting. The more detail you provide, the more reliable the output.

```json
"inputText": "Create a bar chart showing Q3 revenue by region:\n- North America: $4.2M\n- Europe: $2.8M\n- APAC: $1.5M\n\nUse a horizontal bar chart with region labels on the y-axis."
```

**Use templates for repeated chart formats.** If you generate the same type of chart regularly (e.g., weekly sales reports), create a template in the Gamma app with your preferred chart layout and use the [Create from Template API](create-from-template-api-parameters-explained.md). This gives you more control over chart structure than generating from scratch.

**Keep chart instructions explicit.** Specify data types (label vs numeric), chart orientation, and axis formatting directly in your prompt or `additionalInstructions` to reduce ambiguity.

Charts and infographics work best when your prompt includes exact data values and formatting preferences. General instructions like "make a chart" may produce inconsistent layouts.

## Image styling tips

Getting cohesive, high-quality images across your generated content takes a bit of configuration. Here are the key levers.

**Always set `imageOptions.style`.** Even a simple one-word style like `"photorealistic"` or `"minimal illustration"` creates visual consistency across all generated images in a deck. Without it, each image may have a different artistic treatment.

```json
"imageOptions": {
  "source": "aiGenerated",
  "model": "flux-kontext-fast",
  "style": "photorealistic, professional, clean lighting"
}
```

**Choose your model intentionally.** Different models have different speed, quality, and credit tradeoffs:

| Speed | Model | Credits/Image | Notes |
| --- | --- | --- | --- |
| Fastest | `flux-1-quick` | 2 | Best for drafts and high-volume generation |
| Fast | `flux-kontext-fast` | 2 | Good balance of speed and quality |
| High quality | `flux-1-pro` | 8 | Better detail and composition |
| Premium | `imagen-4-pro` | 8 | Strong photorealism |

If no model is specified, Gamma selects one automatically. Explicitly setting a model avoids unexpected defaults.

**Using your own images.** To use only images you provide (no AI-generated ones), set `imageOptions.source` to `"noImages"` and place your image URLs directly in `inputText`. Requirements:

- URLs must be **HTTPS** (not HTTP)
- URLs must end with a recognized extension: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.heic`, `.heif`, or `.avif`
- URLs should be on their own line, clearly standalone
- URLs must be **publicly accessible** (no authentication required)

```json
"inputText": "Quarterly sales highlights\n\nhttps://example.com/assets/q3-chart.png\n\n---\n\nRegional breakdown\n\nhttps://example.com/assets/regions-map.png",
"imageOptions": { "source": "noImages" }
```

A 6-slide deck with AI-generated images typically takes 1-2 minutes. Faster image models can reduce wait times.

## Common issues

### `status` stays `pending` for too long

Generations typically complete in 1-3 minutes. If you are waiting longer than 5 minutes:

- Check that you're polling the correct `generationId`
- Verify your API key has sufficient credits
- Try generating with fewer cards (`numCards`) to test

### You receive a 429 rate-limit response

If you receive a 429 error:

- Use 5+ second polling intervals
- Check the `Retry-After` header for guidance
- If you're using Zapier, Make, or n8n, the rate limit may be on the platform side rather than Gamma's

## Related

- [Error codes](../errors-and-warnings/error-codes.md) for the full list of API errors and troubleshooting guidance
- [Generate from text](generate-api-parameters-explained.md) for parameter-level guidance on `POST /v1.0/generations`
- [API Overview](understanding-the-api-options.md) for a broader workflow comparison
