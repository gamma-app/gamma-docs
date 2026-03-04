# Gamma Cloudflare Infrastructure Landscape

Surveyed 2026-02-25 from the monorepo at `/packages/`.

## Existing Workers

All Workers share Cloudflare account ID `e6d6f2d9231ff6524b204bf07c9d2dc7`.

| Worker | Package | Domain | Role |
|---|---|---|---|
| app-worker | `packages/app-worker/` | gamma.app, staging.gamma.app | Traffic router (marketing vs app vs microsites) |
| public-api-proxy | `packages/public-api-proxy/` | api.gamma.app, public-api.gamma.app | Public API proxy |
| auth-worker | `packages/auth-worker/` | Auth endpoints | Auth proxy |
| image-worker | `packages/image-worker/` | Image CDN | R2 image proxy (staging/prod buckets, webp, avif) |
| embed-proxy | `packages/embed-proxy/` | Embed endpoints | Embed proxy |
| assets | `packages/assets/` | Asset CDN | Static assets with KV namespaces |
| e2e | `packages/e2e/` | Staging | E2E debug tooling |

## Deployment pattern

- **CI/CD**: GitHub Actions with `cloudflare/wrangler-action@2.0.0`
- **Secret**: `CF_API_TOKEN` (shared across workflows)
- **Branch mapping**: `main` → staging, `prod` → production
- **Config**: Each Worker has its own `wrangler.toml` + GitHub Actions workflow
- **Wrangler version**: Workflow pins `3.106.0`, package.json uses `^4.23.0`

## What's in the repo vs dashboard

| Config | Location |
|---|---|
| Worker code + wrangler.toml | Monorepo (`packages/*/`) |
| Custom domains / DNS | Cloudflare dashboard (not in repo) |
| Routes / zone config | Cloudflare dashboard (not in repo) |
| WAF / rate limiting / DDoS | Cloudflare dashboard or separate security repo |
| SSL certificates | Managed by Cloudflare |
| Terraform | AWS only (`terraform/`, `infra/terraform/`). No CF Terraform. |

## Key observations

- No `route`, `routes`, or `zone_id` in any `wrangler.toml` — all use `workers_dev = true`
- No references to `developers.gamma.app` or docs-related domains anywhere in the monorepo
- Security policies are not version-controlled in the monorepo
- The `public-api-proxy` Worker handles the `public-api.gamma.app` domain used by the API docs
