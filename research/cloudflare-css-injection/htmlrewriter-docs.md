# Cloudflare HTMLRewriter — CSS Injection Reference

Source: https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/

## What it is

`HTMLRewriter` is a streaming HTML parser built into Cloudflare Workers. It lets you intercept and transform HTML responses at the edge with jQuery-like selectors — no buffering the entire response.

## CSS injection pattern

Target the `<head>` element and append a `<style>` tag:

```javascript
export default {
  async fetch(request) {
    const GITBOOK_ORIGIN = 'https://your-docs.gitbook.io';
    const url = new URL(request.url);
    const originUrl = GITBOOK_ORIGIN + url.pathname + url.search;
    const response = await fetch(originUrl, { headers: request.headers });

    const contentType = response.headers.get('content-type') || '';
    if (!contentType.includes('text/html')) {
      return response;
    }

    const CUSTOM_CSS = `
      /* Subtle hover lift on card blocks */
      [data-testid="card"] {
        transition: transform 0.2s ease, box-shadow 0.2s ease;
      }
      [data-testid="card"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      }

      /* Smooth fade-in on page content */
      main { animation: fadeIn 0.3s ease-in; }
      @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

      /* Animated link underlines */
      a {
        text-decoration: none;
        background-image: linear-gradient(currentColor, currentColor);
        background-size: 0% 1px;
        background-position: 0 100%;
        background-repeat: no-repeat;
        transition: background-size 0.3s ease;
      }
      a:hover { background-size: 100% 1px; }
    `;

    return new HTMLRewriter()
      .on('head', {
        element(el) {
          el.append(`<style>${CUSTOM_CSS}</style>`, { html: true });
        }
      })
      .transform(response);
  }
};
```

## Key API methods

| Method | What it does |
|---|---|
| `.on(selector, handler)` | Attach handler to elements matching CSS selector |
| `element.append(content, { html: true })` | Insert raw HTML before the closing tag |
| `element.prepend(content, { html: true })` | Insert raw HTML after the opening tag |
| `element.setAttribute(name, value)` | Set an attribute |
| `element.getAttribute(name)` | Read an attribute |

## Supported selectors

Standard CSS selectors: `*`, `E`, `E.class`, `E#id`, `E[attr]`, `E[attr="val"]`, `E F` (descendant), `E > F` (child), `:nth-child(n)`, `:first-child`, `:not(s)`.

## Error handling

If a handler throws, parsing halts immediately and the response body errors. The client sees a truncated response. Keep handlers simple and defensive.

## Performance

HTMLRewriter is a streaming parser — it processes HTML as it flows through the Worker without buffering the entire response. Overhead is typically <1ms. Non-HTML responses (images, JS, CSS files) should be passed through without transformation.

## Alternative: external stylesheet

Instead of inline `<style>`, link to a hosted CSS file:

```javascript
element.append(
  '<link rel="stylesheet" href="https://cdn.gamma.app/docs-animations.css">',
  { html: true }
);
```

This avoids CSP issues with inline styles but requires hosting the CSS file separately (e.g., on R2 or a CDN).
