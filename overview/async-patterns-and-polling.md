---
description: Understanding how to work with Gamma’s asynchronous API and poll for results
---

# Async Patterns & Polling

{% hint style="info" %}
**Why is polling needed?**

Gamma generates content using AI, which can take 30 seconds to several minutes depending on complexity. Rather than keeping your connection open (which would timeout), Gamma uses an **async pattern**: you submit a request, get an ID back immediately, then check back periodically until it’s done.
{% endhint %}

{% hint style="warning" %}
**Polling is how you get your URLs**

The initial `POST /generations` request **`only returns a generationId`** — it does NOT return the presentation URL or export files. You MUST poll the status endpoint to receive:

* `gammaUrl` - The URL to view/share your presentation
* `pdfUrl` / `pptxUrl` - Export file URLs (if you requested exports)
{% endhint %}

## The Basic Flow

```
POST /generations      →  Returns { generationId: "abc123" }
Wait ~5 seconds
GET /generations/abc123  →  Returns { status: "pending" }
Wait ~5 seconds  
GET /generations/abc123  →  Returns { status: "completed", gammaUrl: "...", pdfUrl: "..." }
```

## What You Get Back

When status is `completed`, the response includes:

| Field      | Description                                                                      |
| ---------- | -------------------------------------------------------------------------------- |
| `gammaUrl` | Direct link to view/share the presentation in Gamma                              |
| `pdfUrl`   | Download link for PDF export (if `exportOptions.formats` included `pdf`)         |
| `pptxUrl`  | Download link for PowerPoint export (if `exportOptions.formats` included `pptx`) |

{% hint style="success" %}
Export URLs are **temporary signed URLs** that expire after some time. If you need to store the files, download them promptly after generation completes.
{% endhint %}

## Generation States

| Status      | Meaning              | What to Do                                    |
| ----------- | -------------------- | --------------------------------------------- |
| `pending`   | Still generating     | Keep polling every 5 seconds                  |
| `completed` | Done!                | Stop polling — use `gammaUrl` and export URLs |
| `failed`    | Something went wrong | Stop polling, check the `error` object        |

## Code Examples

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

{% hint style="success" %}
Zapier's "Delay for" action pauses your Zap for a specified time (minimum 1 minute). For most Gamma generations, a single 60-second delay followed by a status check works well.
{% endhint %}

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

{% hint style="info" %}
n8n's Wait node offloads execution data to the database during longer waits, so your workflow won't timeout even for complex generations.
{% endhint %}

### Best Practices

<details>

<summary>Use 5-second polling intervals</summary>

Polling more frequently than every 5 seconds won’t make generation faster and may hit rate limits. 5 seconds is the sweet spot.

</details>

<details>

<summary>Set a maximum timeout</summary>

Most generations complete within 2-3 minutes. Set a maximum of 5 minutes (60 attempts × 5 seconds) to avoid infinite loops.

</details>

<details>

<summary>Handle all three states</summary>

Always check for `pending`, `completed`, AND `failed`. Don’t assume success - check the actual status value.

</details>

<details>

<summary>Use exponential backoff for retries</summary>

If you get rate limited (429), wait longer before retrying. Double your wait time with each retry: 5s → 10s → 20s → 40s.

</details>

## Common Issues

{% hint style="warning" %}
**"My generation is stuck on pending forever"**

Generations typically complete in 1-3 minutes. If you're waiting longer than 5 minutes:

* Check that you're polling the correct `generationId`
* Verify your API key has sufficient credits
* Try generating with fewer cards (`numCards`) to test
{% endhint %}

{% hint style="warning" %}
**"I'm getting rate limited"**

If you receive a 429 error:

* You're polling too frequently (use 5+ second intervals)
* You've exceeded 50 generations/hour - wait and retry
* Check the `Retry-After` header for guidance
{% endhint %}

## Related

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h2><i class="fa-circle-exclamation">:circle-exclamation:</i></h2></td><td><strong>Error Codes</strong></td><td>Full list of error codes and troubleshooting tips</td><td><a href="https://app.gitbook.com/s/IrzC0mooWT36AKgnkerQ/errors-and-warnings/error-codes">Error codes</a></td></tr><tr><td><h2><i class="fa-rocket">:rocket:</i></h2></td><td><strong>Getting started</strong></td><td>Quick start guide with your first API request</td><td><a href="../">..</a></td></tr></tbody></table>
