# GitBook Subdirectory Setup with Cloudflare Worker

Source: https://docs.gitbook.com/publishing-documentation/setting-a-custom-subdirectory/configuring-a-subdirectory-with-cloudflare

Requires: **GitBook Ultimate site plan**

Use this if you want docs at a subdirectory like `gamma.app/docs` rather than a separate domain. If you just want `developers.gamma.app`, see `custom-domain-steps.md` instead.

## Steps

### 1. Configure GitBook

1. In GitBook org, click your docs site name in the sidebar
2. Click **Manage site** or open **Settings** tab
3. Open **Domain and redirects** section
4. Under "Subdirectory", click **Set up a subdirectory**
5. Enter the URL: `gamma.app/docs`
6. Click **Configure**
7. Copy the **proxy URL** from "Additional configuration"

### 2. Create Cloudflare Worker

1. Sign into Cloudflare → **Workers & Pages**
2. Click **Create** → **Hello world** template
3. Rename to `gamma-docs-proxy`
4. Click **Deploy**

### 3. Configure custom domain

1. In Worker **Settings** → **Domains & Routes**
2. Click **+ Add** → **Custom domain**
3. Enter `gamma.app` (NOT `gamma.app/docs`)

**Warning**: This would conflict with the existing `app-worker` that already handles `gamma.app` traffic. See risk analysis in README.md.

### 4. Update Worker code

```javascript
export default {
  fetch(request) {
    const SUBDIRECTORY = '/docs';
    const url = new URL(request.url);
    const target = "<INSERT GITBOOK PROXY URL>" + url.pathname.slice(SUBDIRECTORY.length);
    const proxy = new URL(
      target.endsWith('/') ? target.slice(0, -1) : target
    );
    proxy.search = url.search;
    return fetch(new Request(proxy, request));
  }
};
```

### 5. Add CSS injection (optional)

Wrap the fetch in HTMLRewriter — see `htmlrewriter-docs.md` for the pattern.

## Conflict with existing app-worker

The `app-worker` already routes all `gamma.app` traffic. Adding a second Worker on the same domain for `/docs` would require either:
- Modifying `app-worker` to route `/docs` traffic to GitBook (preferred — keeps routing in one place)
- Using Cloudflare route priority rules (fragile)

This is why the separate `developers.gamma.app` custom domain approach is simpler.
