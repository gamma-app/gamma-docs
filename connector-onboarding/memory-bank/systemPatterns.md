# System Patterns

## Architecture

Onboarding is a small footprint in the OAuth provider stack. Three files in the `gamma` server repo, one S3 upload, one Terraform apply. Everything else — consent page rendering, session storage, token issuance — already exists and doesn't change per connector.

```
Connector request (sheet)
   │
   ├── Byron approves → eligible for next batch
   │
   ▼
Batch PR drafted (gamma repo)
   ├── oauth-client-type.ts        (union + hostname maps)
   ├── oauth-provider.resolver.ts  (logo URL map)
   └── prod.tfvars                 (DCR allowlist patterns)
   │
   ├── S3 logo upload (manual, separate)
   │
   ▼
Merge → Terraform apply → connector live
   │
   ▼
(Optional) generation-details.guard.ts PR for App Host
```

## Key technical decisions

- **Allowlist lives in Terraform, not Parameter Store** (#18376). Enables normal code review but means deployment requires `terraform apply` in addition to PR merge.
- **Batch PR model over one-off PRs** (#18530 onwards). Single PR per week-ish, covers multiple approved connectors. Simpler review, lower overhead.
- **App Host is a separate opt-in decision.** `generation-details.guard.ts` only changes with explicit engineering sign-off — not default onboarding scope.
- **TypeScript safety as the net.** `CLIENT_TYPE_TO_LOGO_URL: Record<OAuthClientType, string | null>` means adding a union member without a logo entry fails the build. Don't work around the type system.
- **Staging allows everything.** `staging.tfvars` is `[".*"]`; no per-connector staging changes.

## Design patterns in use

- **`HOSTNAME_TO_CLIENT_TYPE` — exact hostname match.** Most connectors. E.g., `grok.com → grok`, `coda.io → superhuman`, `chatgpt.com → chatgpt`.
- **`HOSTNAME_SUFFIX_TO_CLIENT_TYPE` — suffix match for tenant subdomains.** Used only by Glean today: `-be.glean.com → glean`. If a new connector has tenant-parameterized callback hosts, this is the pattern.
- **`CLIENT_TYPE_TO_LOGO_URL` — full coverage of the union.** TypeScript enforces every member has an entry (even if `null`).
- **Regex patterns in `oauth_dcr_allowed_redirect_urls`.** Case-insensitive, validated at registration time. Escape dots with `\\.`. Anchor with `^...$` when possible.

## Component relationships

- `oauth-provider.utils.ts` → `validateRedirectUris()` enforces the allowlist against patterns from `prod.tfvars`
- `oauth-provider.resolver.ts` → `getOAuthConsentData()` serves logo + client name to the consent page; calls `getOAuthClientType()` to resolve the type from redirect URI
- `oauth-provider.controller.ts` handles `/oauth/register`, `/oauth/authorize`, `/oauth/callback`, `/oauth/token` — not touched during onboarding
- `config/oauth-provider.config.ts` loads `OAUTH_DCR_ALLOWED_REDIRECT_URLS` at boot from the env var populated by Terraform

## Critical implementation paths

- Adding a connector → `packages/server/src/oauth-provider/oauth-client-type.ts` edit is the single highest-signal change
- Connector logo rendering → `packages/server/src/oauth-provider/oauth-provider.resolver.ts::CLIENT_TYPE_TO_LOGO_URL` + S3 upload to `static.gamma.app/icons/third_party/`
- DCR validation → `packages/server/terraform/prod.tfvars::oauth_dcr_allowed_redirect_urls` + Terraform apply
