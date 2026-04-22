# Tech Context

## Stack

- **Server**: TypeScript + NestJS, `packages/server/` in the `gamma` monorepo (Yarn workspaces)
- **Infrastructure**: Terraform for server config and env vars, applied out of `packages/server/terraform/`
- **Static assets**: AWS S3 bucket `static.gamma.app`, logos under `icons/third_party/`
- **Database**: Prisma on PostgreSQL (stores OAuth clients, sessions, codes) — not touched during onboarding
- **External services**: Notion (process doc), Google Sheets (intake + approval), Slack `#mcp-access-requests` (triage), GitHub (code review)
- **Auth**: Workspace OAuth 2.1 + PKCE with Dynamic Client Registration — implementation owned by platform eng

## Development setup

No per-project setup beyond standard monorepo. From `gamma/` root:

```
# regenerate TypeScript types after editing oauth-client-type.ts
yarn workspace server build

# run server unit tests for the oauth-provider module
yarn workspace server jest packages/server/src/oauth-provider --no-coverage

# validate Terraform syntax before opening a PR
cd packages/server/terraform && terraform validate
```

S3 logo upload via AWS CLI with the `engineer` role:

```
aws s3 cp /path/to/logo.svg s3://static.gamma.app/icons/third_party/{filename} --profile engineer
```

## Constraints

- **Terraform apply requires engineering permission.** You cannot apply from a docs PR context; coordinate with Matt or whichever engineer owns the deploy.
- **S3 logo path is fixed.** `icons/third_party/` under `static.gamma.app`. Not configurable.
- **Empty `oauth_dcr_allowed_redirect_urls` rejects all registrations** (fail-closed). Never drop the array during refactors.
- **Staging is permissive** (`[".*"]`). Don't add staging patterns; it makes no difference.
- **Regex patterns are case-insensitive** at runtime. `^https://grok\\.com$` and `^https://GROK\\.com$` are equivalent.

## Dependencies

- `gh` CLI — for PR operations (view, create, search)
- AWS CLI with a profile that has `engineer` role access to `static.gamma.app` — for S3 uploads
- Terraform — only required for apply; PR drafting doesn't need it locally
- Notion MCP — optional, for fetching Matt's process doc; falls back to the URL if not authed
- Slack MCP — read-only; used for searching `#mcp-access-requests` and coordinating handoffs

## Tool usage patterns

- **PR drafting**: `gh pr create --draft` with a batch-aware body listing every connector in the batch
- **PR auditing**: `git log main --oneline -- packages/server/src/oauth-provider/oauth-client-type.ts` for the real onboarding history (filter to `main` to skip branch noise)
- **Connector discovery**: search the sheet first, then `#mcp-access-requests` for any context that didn't make it into the sheet row
- **Verification**: `yarn workspace server build` catches missing logo entries; `terraform validate` catches malformed regex escape sequences
