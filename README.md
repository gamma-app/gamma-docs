---
description: >-
  Build with the Gamma API — generate presentations, documents, websites, and
  social posts programmatically.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Gamma Developer Documentation

{% columns %}
{% column valign="middle" %}
One API call. Polished presentations, documents, websites, and social posts — branded, exported, and shared.

<a href="https://gamma.app/settings/api-keys" class="button primary">Get your API key</a><a href="overview/generate-api-parameters-explained.md" class="button secondary">API reference</a>
{% endcolumn %}

{% column %}
<figure><img src=".gitbook/assets/landscape-developer.png" alt="" width="375"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

## Quickstart

Authenticate with your API key via the `X-API-KEY` header. API access requires a Pro, Ultra, Teams, or Business plan.

{% tabs %}
{% tab title="cURL" %}
```bash
# 1. Create a generation
RESPONSE=$(curl -s -X POST https://public-api.gamma.app/v1.0/generations \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: $GAMMA_API_KEY" \
  -d '{
    "inputText": "Q3 product launch strategy",
    "textMode": "generate",
    "format": "presentation",
    "numCards": 10,
    "exportAs": "pdf"
  }')

GENERATION_ID=$(echo $RESPONSE | jq -r '.generationId')

# 2. Poll until complete (every 5 seconds)
while true; do
  STATUS=$(curl -s https://public-api.gamma.app/v1.0/generations/$GENERATION_ID \
    -H "X-API-KEY: $GAMMA_API_KEY")

  echo $STATUS | jq '.status'

  if echo $STATUS | jq -e '.status == "completed"' > /dev/null; then
    echo $STATUS | jq '{gammaUrl, exportUrl}'
    break
  fi
  sleep 5
done
```
{% endtab %}

{% tab title="Python" %}
```python
import requests, os, time

API_KEY = os.environ["GAMMA_API_KEY"]
BASE = "https://public-api.gamma.app/v1.0"
HEADERS = {"X-API-KEY": API_KEY, "Content-Type": "application/json"}

# 1. Create a generation
response = requests.post(f"{BASE}/generations", headers=HEADERS, json={
    "inputText": "Q3 product launch strategy",
    "textMode": "generate",
    "format": "presentation",
    "numCards": 10,
    "exportAs": "pdf",
})
response.raise_for_status()
generation_id = response.json()["generationId"]

# 2. Poll until complete (every 5 seconds)
for _ in range(60):
    status = requests.get(f"{BASE}/generations/{generation_id}", headers=HEADERS).json()
    if status["status"] == "completed":
        print(f"View: {status['gammaUrl']}")
        print(f"PDF:  {status['exportUrl']}")
        break
    if status["status"] == "failed":
        print(f"Error: {status['error']['message']}")
        break
    time.sleep(5)
```
{% endtab %}

{% tab title="JavaScript" %}
```javascript
const API_KEY = process.env.GAMMA_API_KEY;
const BASE = "https://public-api.gamma.app/v1.0";
const headers = { "X-API-KEY": API_KEY, "Content-Type": "application/json" };

// 1. Create a generation
const createRes = await fetch(`${BASE}/generations`, {
  method: "POST",
  headers,
  body: JSON.stringify({
    inputText: "Q3 product launch strategy",
    textMode: "generate",
    format: "presentation",
    numCards: 10,
    exportAs: "pdf",
  }),
});
const { generationId } = await createRes.json();

// 2. Poll until complete (every 5 seconds)
for (let i = 0; i < 60; i++) {
  const pollRes = await fetch(`${BASE}/generations/${generationId}`, { headers });
  const data = await pollRes.json();

  if (data.status === "completed") {
    console.log(`View: ${data.gammaUrl}`);
    console.log(`PDF:  ${data.exportUrl}`);
    break;
  }
  if (data.status === "failed") {
    console.error(data.error?.message);
    break;
  }
  await new Promise((r) => setTimeout(r, 5000));
}
```
{% endtab %}
{% endtabs %}

Completed response:

```json
{
  "generationId": "abc123xyz",
  "status": "completed",
  "gammaUrl": "https://gamma.app/docs/abc123",
  "exportUrl": "https://gamma.app/export/abc123.pdf",
  "credits": { "deducted": 15, "remaining": 485 }
}
```

{% hint style="info" %}
Getting a 401? Gamma uses `X-API-KEY` as a custom header — not `Authorization: Bearer`. See [Error codes](errors-and-warnings/error-codes.md) for other common issues.
{% endhint %}

### Next steps

Browse the sidebar for the full API surface, or jump to:

* [All generation parameters](overview/generate-api-parameters-explained.md) — format, themes, images, headers/footers, sharing
* [Template-based generation](overview/create-from-template-api-parameters-explained.md) — design once, generate variations
* [Connectors and Integrations](overview/connectors-and-integrations.md) — Claude, Zapier, Make, n8n
