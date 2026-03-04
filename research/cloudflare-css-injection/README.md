# Cloudflare CSS Injection for GitBook Docs

## Summary

Investigation into using a Cloudflare Worker with HTMLRewriter to inject custom CSS animations into the GitBook-hosted API docs site. The goal: subtle, whimsical transitions (hover lifts on cards, page fade-ins, animated underlines) that match Gamma's brand.

## Verdict (stealth-surgeon assessment)

**Not recommended as a quick win.** This is a new infrastructure system, not a surgical change.

| Criterion | Assessment |
|---|---|
| Minimal diff | FAIL — new Worker, new deployment pipeline, new DNS, new CI/CD |
| Local over global | FAIL — touches Cloudflare dashboard, DNS, GitBook proxy layer |
| Respect ownership | RISK — security repo and CF dashboard owned by others |
| No side-effects | RISK — new proxy layer in front of docs site |

## Key risks

1. **Separate security infrastructure**: Gamma's Cloudflare WAF/rate limiting/DDoS config is managed in the dashboard or a separate repo, not the monorepo. A new Worker could bypass or conflict with existing security policies.
2. **Dashboard-managed DNS**: No Terraform or IaC for Cloudflare DNS. Domain changes are unversioned dashboard operations.
3. **Proxy-in-front-of-proxy**: User → CF Worker → GitBook CDN → GitBook origin. Could cause cache invalidation issues, break GitBook's built-in search/AI features.
4. **CSP header conflicts**: GitBook may set Content-Security-Policy headers that block inline `<style>` tags.
5. **Fragile CSS selectors**: GitBook can change HTML structure anytime without notice.
6. **Graceful degradation**: If selectors break, animations disappear silently — nothing crashes, the site just looks "normal."

## Recommendation

1. **Now**: Use GitBook's built-in customization (Gradient theme, brand colors, fonts, rounded corners, semantic colors). Gets 80% of visual polish with 0% risk.
2. **Later**: If a Worker is added for `developers.gamma.app` (custom domain setup), CSS injection can be layered on top with minimal incremental effort.
3. **Before proceeding**: Get buy-in from whoever owns the Cloudflare account and security policies.

## Files in this folder

- `gamma-cloudflare-landscape.md` — Inventory of existing Workers and deployment patterns
- `htmlrewriter-docs.md` — Cloudflare HTMLRewriter API reference and CSS injection examples
- `gitbook-subdirectory-setup.md` — GitBook Ultimate + Cloudflare Worker proxy setup
- `custom-domain-steps.md` — Standalone steps for `developers.gamma.app` via CNAME
