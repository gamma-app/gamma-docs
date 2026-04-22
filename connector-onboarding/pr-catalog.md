# PR catalog — connector onboardings

Every connector-onboarding PR merged to `main` in the `gamma` monorepo, plus the infra-adjacent PRs that touch the same files but aren't onboardings. Built from `git log --follow` + `gh pr list`, verified against current `main`.

## Onboarding PRs (merged to main)

| PR | Merged (UTC) | Connector(s) / scope | Author | Files touched | Summary |
| --- | --- | --- | --- | --- | --- |
| [#15319](https://github.com/gamma-app/gamma/pull/15319) | 2025-12-16 | Atlassian | Matt Carroll | `oauth-provider.resolver.ts` | Map Atlassian redirect URL hosts to consent-page logo data. |
| [#15379](https://github.com/gamma-app/gamma/pull/15379) | 2025-12-18 | Glean | sarafina98 | `oauth-provider.resolver.ts` | Glean OAuth consent/logo wiring (pre-`oauth-client-type.ts`). |
| [#15679](https://github.com/gamma-app/gamma/pull/15679) | 2026-01-12 | Claude, ChatGPT, Atlassian, Glean (typed classification) | Matt Carroll | `oauth-client-type.ts` **(new)** + `oauth-provider.resolver.ts` + `public-api.guard.ts` + `types.ts` + `public-api.guard.spec.ts` | Introduce `oauth-client-type.ts`, hostname map + `-be.glean.com` suffix rule, resolver + public API guard/types for client-type analytics. |
| [#15484](https://github.com/gamma-app/gamma/pull/15484) | 2026-01-15 | ChatGPT (App Host) | Matt Carroll | `generation-details.guard.ts` + spec + DTO | Allow ChatGPT through `generation-details` guard + widget/generation details flow. |
| [#15756](https://github.com/gamma-app/gamma/pull/15756) | 2026-01-14 | Superhuman | samuli-kekki | `oauth-client-type.ts` + `oauth-provider.resolver.ts` + `ClientLogos.tsx` | Add `superhuman` type, `coda.io` → Superhuman hostname map, client-side logo. |
| [#15849](https://github.com/gamma-app/gamma/pull/15849) | 2026-01-16 | Claude (App Host) | Matt Carroll | `generation-details.guard.ts` + spec | Extend `generation-details.guard` for Claude MCP app. |
| [#16599](https://github.com/gamma-app/gamma/pull/16599) | 2026-02-10 | ChatGPT (multi-host) | samuli-kekki | `oauth-client-type.ts` + many `oauth-provider/*` + `generation-details.guard(.spec)` + `public-api.guard(.spec)` + `oauth-provider.e2e-spec.ts` | Multi-redirect URI support; add `platform.openai.com` → `chatgpt`, `getClientTypeFromUris`, large oauth-provider refactor. |
| [#16724](https://github.com/gamma-app/gamma/pull/16724) | 2026-02-12 | Glean (App Host) | Matt Carroll | `generation-details.guard.ts` + spec | Add Glean to `generation-details` allowed client types. |
| [#18152](https://github.com/gamma-app/gamma/pull/18152) | 2026-03-18 | Grok | Matt Carroll | `oauth-client-type.ts` + `oauth-provider.resolver.ts` | Add `grok`, hosts `grok.com` + `console.x.ai`, resolver logo mapping. No `prod.tfvars` in this PR — Terraform patterns landed with the migration in #18376. |
| [#18530](https://github.com/gamma-app/gamma/pull/18530) | 2026-03-30 | Batch 1: Lantern, Peripheral, Maybe, Ledgers, Needle, Actava, Algora, Rockhood, Code and Theory, Rubica | maxjackson-lab | `oauth-client-type.ts` + `oauth-provider.resolver.ts` + `prod.tfvars` | First batched MCP onboarding PR. Introduces the weekly-batch model. |
| [#18885](https://github.com/gamma-app/gamma/pull/18885) | 2026-04-17 | Batch 2: Veleiro, MissionSquad, SheetXAI, Optimizely, Auglab, DesignGrow, Mimasa, Fireflies, Worklayer, Elvin; Peripheral URI correction | maxjackson-lab | `oauth-client-type.ts` + `oauth-provider.resolver.ts` + `prod.tfvars` | Second batch. Fireflies uses four callback hosts; Peripheral URIs resubmitted. |

## Patterns and variations

These are the shape variations worth knowing before drafting the next onboarding PR.

- **Glean uses suffix matching, not exact hosts.** `HOSTNAME_SUFFIX_TO_CLIENT_TYPE` in `oauth-client-type.ts` matches `-be.glean.com` so tenant subdomains classify as `glean`. DCR allowlist mirrors this with a regex for `[^/]+-be.glean.com` in `prod.tfvars`.
- **Superhuman maps from `coda.io`.** The hostname doesn't match the product name — don't assume the two are correlated.
- **ChatGPT is multi-host and multi-URI.** Both `chatgpt.com` and `platform.openai.com` resolve to `chatgpt`. `prod.tfvars` additionally allows `[^/]+.chatgpt.com` subdomains and `oauth.tools`.
- **Grok was split across two PRs.** #18152 added the TypeScript classification + logo. The Terraform allowlist patterns first appeared with the Parameter Store → Terraform migration in #18376; #18473 later tweaked them for optional trailing slashes.
- **Batch MCP onboardings (#18530, #18885).** One PR adds many `OAuthClientType` literals, resolver/logo entries, and parallel regex lines in `prod.tfvars`. This is now the default workflow for approved connectors.
- **Fireflies uses four callback hosts.** `askfred.*`, `app.fireflies.ai`, `next.fireflies.dev`, etc. Expect this pattern for mature SaaS connectors with staging/dev URIs.
- **Code and Theory maps multiple environment hostnames.** `stagwell-machine.com`, `dev.*`, `stage.*` all map to client type `codetheory`. This is a reasonable pattern to mirror for any connector with explicit env-named callback domains.
- **App Host is a separate opt-in.** ChatGPT, Claude, and Glean each got standalone `generation-details.guard.ts` allowlist PRs (#15484, #15849, #16724). These PRs generally don't modify `oauth-client-type.ts`. Treat App Host as a per-connector engineering decision, not default onboarding behavior.
- **`git log --follow` on `oauth-client-type.ts` surfaces off-main commits.** Session checkpoints and unmerged branches appear. Filter to `main` only when auditing: `git log main --oneline -- packages/server/src/oauth-provider/oauth-client-type.ts`. On `main`, only six commits touch that file — #15679, #15756, #16599, #18152, #18530, #18885.

## Outliers — touched OAuth files but NOT onboardings

Don't confuse these with real onboardings when auditing history.

| PR / commit | Why it's not onboarding |
| --- | --- |
| [#18376](https://github.com/gamma-app/gamma/pull/18376) | Migrated `OAUTH_DCR_ALLOWED_REDIRECT_URLS` from AWS Parameter Store to `oauth_dcr_allowed_redirect_urls` in `prod.tfvars`. Infra, not a connector. |
| [#18473](https://github.com/gamma-app/gamma/pull/18473) | Grok-only regex trailing-slash tweak. `prod.tfvars` only. |
| [#16890](https://github.com/gamma-app/gamma/pull/16890) | Security hardening / whitelist behavior. No `oauth-client-type.ts` change. |
| [#17045](https://github.com/gamma-app/gamma/pull/17045) | Prettier/eslint trailing-comma fix on `oauth-provider.resolver.ts`. |
| #15983, #15695, #15931 | JWT / signup / analytics around client type. Not adding a connector enum/host map. |

## Source files that matter

All onboarding PRs touch some subset of these:

- `packages/server/src/oauth-provider/oauth-client-type.ts` — client-type union + hostname maps
- `packages/server/src/oauth-provider/oauth-provider.resolver.ts` — consent-page logo map
- `packages/server/terraform/prod.tfvars` — DCR redirect URI allowlist (since #18376)
- `packages/server/src/public-api/auth/generation-details.guard.ts` — App Host allowlist (optional, separate decision)
