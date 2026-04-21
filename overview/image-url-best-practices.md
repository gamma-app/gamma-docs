---
description: >-
  How to include your own images in API-generated gammas, and how to avoid
  common issues with broken or missing images.
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

# Optimize image URLs

You can include your own images in API-generated gammas by placing image URLs directly in your `inputText` (Generate API) or `prompt` (Create from Template API). The technical requirements and common pitfalls are below.

### Quick reference

- URLs must be HTTPS, end with a recognized image extension, and be publicly accessible.
- Set `imageOptions.source` to `noImages` if you want only your provided images.
- Gamma fetches and re-hosts images during generation, so URLs only need to be live at generation time.
- Test URLs in an incognito window -- if you can see the image without logging in, Gamma can access it.

### How it works

When Gamma encounters an image URL in your input, it:

1. Detects the URL based on format (see requirements below)
2. Fetches the image from your URL during generation
3. Re-hosts the image on Gamma's CDN

If the fetch fails for any reason, the image is silently skipped — you won't get an error, but the image won't appear in the output.

### URL requirements

For Gamma to detect and use your image URLs, they must meet **all** of the following:

| **Requirement** | **Details** |
| --- | --- |
| HTTPS only | URLs must start with `https://`. HTTP URLs are ignored. |
| Recognized image extension | Must end with one of: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.heic`, `.heif`, `.avif` |
| Publicly accessible | No authentication headers, login walls, or IP restrictions. Gamma's servers must be able to fetch the URL directly. |

{% hint style="warning" %}
**Query parameters are fine.** URLs like `https://cdn.example.com/photo.jpg?width=800&quality=90` will work — Gamma matches the extension before any `?` query string.
{% endhint %}

#### What won't work

| URL type | Why it fails |
| --- | --- |
| `http://example.com/photo.jpg` | Not HTTPS |
| `https://example.com/image` | No recognized extension |
| `https://example.com/document.pdf` | Not an image extension |
| `https://internal.corp.net/photo.jpg` | Not publicly accessible |
| `<img src="https://example.com/photo.jpg">` | HTML tags — use the raw URL instead |
| `![alt](https://example.com/photo.jpg)` | Already-wrapped markdown is skipped by the preprocessor |

### Placement in your input

Image URLs can appear **inline with your text or on their own line** — both work. Gamma scans for any whitespace-separated URL matching the requirements above.

{% code title="Inline with text" %}
```
"inputText": "Our headquarters https://cdn.example.com/office.jpg is located in San Francisco."
```
{% endcode %}

{% code title="On its own line" %}
```
"inputText": "Our headquarters\nhttps://cdn.example.com/office.jpg\nis located in San Francisco."
```
{% endcode %}

{% code title="Multiple images" %}
```
"inputText": "Product lineup:\nhttps://cdn.example.com/product-a.jpg\nhttps://cdn.example.com/product-b.png\nhttps://cdn.example.com/product-c.webp"
```
{% endcode %}

### Use `noImages` to prevent extra images

If you want **only** your provided images (no AI-generated or stock images added by Gamma), set `imageOptions.source` to `noImages`:

```json
{
  "inputText": "...",
  "textMode": "preserve",
  "imageOptions": {
    "source": "noImages"
  }
}
```

Without this, Gamma may add additional images from the selected source alongside yours.

### Hosting recommendations

Since Gamma fetches and re-hosts your images during generation, the URLs only need to be accessible at generation time. However, using reliable hosting avoids intermittent failures.

| URL type | Recommended | Notes |
| --- | --- | --- |
| Public CDN (Cloudflare, CloudFront, Fastly) | ✅ Yes | Permanent, fast, reliable |
| Direct image hosting (Imgur, Unsplash) | ✅ Yes | Generally permanent |
| S3/GCS signed URL (7+ day expiry) | ✅ Yes | Works if expiration is long enough |
| S3/GCS signed URL (< 24 hours) | ❌ No | May expire before Gamma fetches it |
| Google Drive / Dropbox share links | ⚠️ Maybe | Can break if permissions change; not a direct image URL |
| URLs behind CDN hotlink protection | ❌ No | Gamma's servers will be blocked |
| Localhost / private network IPs | ❌ No | Not accessible to Gamma's servers |

{% hint style="success" %}
**Quick test:** Open your image URL in an incognito browser window. If you can see the image without logging in, Gamma can access it too.
{% endhint %}

### Troubleshooting

#### Images appear during generation but disappear on refresh

Your URLs were accessible when Gamma first rendered the content, but the re-hosting step failed — usually because of hotlink protection, rate limiting, or signed URLs that expired between the initial render and the background upload. Use permanent, publicly accessible URLs.

#### Images don't appear at all

Check that your URLs meet all three requirements (HTTPS, recognized extension, publicly accessible). Also check that you're not wrapping them in HTML `<img>` tags or markdown image syntax — use raw URLs only.

#### Some images work, others don't

Each URL is fetched independently. A mix of working and broken images usually means some URLs have access restrictions or don't end with a recognized extension. Test each URL individually in an incognito window.

### Related

- [Generate from text](generate-api-parameters-explained.md) for where image URLs fit in `inputText`
- [Generate from template](create-from-template-api-parameters-explained.md) for using image URLs in the `prompt` field
- [Poll for results](async-patterns-and-polling.md) for the generation workflow after submitting your request
