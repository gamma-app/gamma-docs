---
description: Understanding how to work with Gamma’s asynchronous API and poll for results
---

# Poll for results

Gamma generation is asynchronous. You start a generation, receive a `generationId` immediately, then poll the status endpoint until the result is ready.

### Quick reference

- `POST /v1.0/generations` returns `generationId` only.
- Poll `GET /v1.0/generations/{generationId}` every 5 seconds until `status` is `completed` or `failed`.
- `gammaUrl` and `exportUrl` are only available from the completed status response.
- Export URLs are temporary signed URLs, so download exported files promptly.

### The basic flow

```text
POST /generations      →  Returns { generationId: "abc123" }
Wait ~5 seconds
GET /generations/abc123  →  Returns { status: "pending" }
Wait ~5 seconds  
GET /generations/abc123  →  Returns { status: "completed", gammaUrl: "...", exportUrl: "..." }
```

### What you get back

When status is `completed`, the response includes:

| Field       | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| `gammaUrl`  | Direct link to view/share the presentation in Gamma                 |
| `exportUrl` | Download URL for the exported file (if `exportAs` was specified)    |

### Generation states

| Status      | Meaning              | What to Do                                    |
| ----------- | -------------------- | --------------------------------------------- |
| `pending`   | Still generating     | Keep polling every 5 seconds                  |
| `completed` | Done!                | Stop polling — use `gammaUrl` and export URLs |
| `failed`    | Something went wrong | Stop polling, check the `error` object        |

### Code examples

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

### Using automation platforms

Popular automation platforms have built-in ways to handle delays and polling:

#### Zapier

Use the **Delay** action between your HTTP Request steps:

1. **HTTP Request** (POST) → Start generation, get `generationId`
2. **Delay for** → Wait 30-60 seconds
3. **HTTP Request** (GET) → Check status with the `generationId`
4. Use **Paths** or **Filter** to check if `status` equals `completed`
5. If still pending, use **Looping by Zapier** to repeat steps 2-4

Zapier's "Delay for" action pauses your Zap for a specified time (minimum 1 minute). For most Gamma generations, a single 60-second delay followed by a status check works well.

#### Make (formerly Integromat)

Use the **Sleep** module or a polling pattern:

1. **HTTP** module → POST to start generation
2. **Sleep** module → Wait 30 seconds
3. **HTTP** module → GET to check status
4. **Router** with filter → Check if `status` is `completed`
5. Use **Repeater** + **Sleep** for polling loop

#### n8n

Use the **Wait** node with time interval:

1. **HTTP Request** node → POST to start generation
2. **Wait** node → Set to "After Time Interval" (30-60 seconds)
3. **HTTP Request** node → GET to check status
4. **IF** node → Check `status === "completed"`
5. Loop back to Wait node if still pending

n8n's Wait node offloads execution data to the database during longer waits, so your workflow won't timeout even for complex generations.

### Best practices

- Use 5-second polling intervals. Polling more frequently will not speed up the generation and may increase the chance of rate limiting.
- Set a maximum timeout. Most generations complete within 2-3 minutes, so a 5-minute ceiling is a good default for automation.
- Handle all three states: `pending`, `completed`, and `failed`.
- Use exponential backoff if you receive a 429 response.

### Common issues

#### `status` stays `pending` for too long

Generations typically complete in 1-3 minutes. If you are waiting longer than 5 minutes:

- Check that you're polling the correct `generationId`
- Verify your API key has sufficient credits
- Try generating with fewer cards (`numCards`) to test

#### You receive a 429 rate-limit response

If you receive a 429 error:

- Use 5+ second polling intervals
- Check the `Retry-After` header for guidance
- If you're using Zapier, Make, or n8n, the rate limit may be on the platform side rather than Gamma's

### Related

- [Error codes](../errors-and-warnings/error-codes.md) for the full list of API errors and troubleshooting guidance
- [Generate from text](generate-api-parameters-explained.md) for parameter-level guidance on `POST /v1.0/generations`
- [Charts and structured content](charts-and-structured-content.md) for prompting charts and infographics
- [Image URL best practices](image-url-best-practices.md) for including your own images
- [API Overview](understanding-the-api-options.md) for a broader workflow comparison
