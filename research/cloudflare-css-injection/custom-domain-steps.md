# Setting Up developers.gamma.app (Custom Domain for GitBook)

No Cloudflare Worker required. This is a CNAME-based custom domain pointing directly to GitBook.

## Prerequisites

- GitBook Premium or Ultimate site plan
- Access to Gamma's DNS provider (Cloudflare dashboard)
- Access to GitBook site settings

## Steps

### 1. Configure in GitBook

1. Open your docs site in GitBook
2. Go to **Settings** → **Domain and redirects**
3. Click **Set up a custom domain**
4. Enter: `developers.gamma.app`
5. GitBook will display the CNAME target (something like `hosting.gitbook.io`)

### 2. Add DNS record in Cloudflare

1. Sign into Cloudflare dashboard
2. Select the `gamma.app` zone
3. Go to **DNS** → **Records**
4. Add a new record:
   - **Type**: CNAME
   - **Name**: `developers`
   - **Target**: the value GitBook provided (e.g., `hosting.gitbook.io`)
   - **Proxy status**: DNS only (gray cloud) — GitBook manages its own SSL
   - **TTL**: Auto

### 3. Wait for propagation

- DNS propagation takes up to 1 hour (usually faster)
- GitBook automatically provisions an SSL certificate once DNS resolves

### 4. Finalize in GitBook

1. Return to GitBook site settings
2. Click **Finalize** or **Verify** on the custom domain setup
3. Confirm the site loads at `https://developers.gamma.app`

## Notes

- **Proxy status**: Must be "DNS only" (gray cloud), not "Proxied" (orange cloud). GitBook needs direct DNS resolution to provision SSL.
- **No Worker needed**: This is a simple CNAME. The Cloudflare Worker approach is only needed if you want subdirectory hosting (e.g., `gamma.app/docs`) or CSS injection.
- **GitBook handles SSL**: Automatic certificate provisioning once DNS resolves.
- **Existing Workers unaffected**: This creates a new subdomain (`developers.gamma.app`) that doesn't conflict with any existing Worker routes on `gamma.app`.

## Future: Adding CSS injection

If you later want to inject custom CSS animations via a Cloudflare Worker:
1. Change the CNAME proxy status from gray cloud to orange cloud
2. Create a Worker that proxies `developers.gamma.app` → GitBook
3. Add HTMLRewriter CSS injection (see `htmlrewriter-docs.md`)

This can be done incrementally without disrupting the existing custom domain setup.
