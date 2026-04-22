# Process — connector onboarding

Synthesis of the current onboarding flow. This is not the canonical process doc — Matt's [Notion page](https://www.notion.so/gamma-app/Onboarding-a-new-connector-327f3594899480b5b2e1e11c57f533db) is — but it captures the deltas since Matt wrote the original and points to the skill that executes the flow.

## Canonical sources

| Source | Purpose |
| --- | --- |
| [Notion: Onboarding a new connector](https://www.notion.so/gamma-app/Onboarding-a-new-connector-327f3594899480b5b2e1e11c57f533db) | Matt's process writeup. Authoritative for process questions. |
| `~/.claude/skills/onboard-connector/SKILL.md` | Executable workflow — steps 0 through 8, with approval gates and batch mode. |
| `~/.claude/skills/onboard-connector/reference.md` | Architecture reference — how client identification works at runtime. |
| [MCP access requests sheet](https://docs.google.com/spreadsheets/d/1S7wuQ1oEGEJhpobMz_6CRWUgsnCjFQoa65YFYjtVuGs/edit?gid=497166213#gid=497166213) | Intake + Byron approval gate. The business decision on whether to onboard a connector lives here. |
| `#mcp-access-requests` Slack channel | Triage + discussion of pending requests. |

## The three-file pattern

Every connector onboarding currently touches some combination of these files. The minimum viable onboarding touches all three.

| File | Role |
| --- | --- |
| `packages/server/src/oauth-provider/oauth-client-type.ts` | Adds the connector to the `OAuthClientType` union + maps its redirect hostnames to that type. |
| `packages/server/src/oauth-provider/oauth-provider.resolver.ts` | Adds the connector's logo URL to `CLIENT_TYPE_TO_LOGO_URL` (served on the OAuth consent page). |
| `packages/server/terraform/prod.tfvars` | Appends the connector's redirect URI patterns to `oauth_dcr_allowed_redirect_urls`. |

TypeScript safety catches most mistakes here: `CLIENT_TYPE_TO_LOGO_URL` is typed as `Record<OAuthClientType, string | null>`, so adding a new union member without a logo entry fails `yarn workspace server build`.

## The optional fourth file — App Host

`packages/server/src/public-api/auth/generation-details.guard.ts` controls whether a connector can render Gamma generation previews inline in their UI (App Host).

**This is a separate engineering decision**, not part of the default onboarding flow. Only ChatGPT, Claude, and Glean have it today. The skill explicitly gates this step — don't add a connector to the guard without an explicit ask.

See [pr-catalog.md](pr-catalog.md) — #15484 (ChatGPT), #15849 (Claude), #16724 (Glean) are the canonical App Host PRs.

## Steps still not automated

Two manual steps remain after the PR is drafted:

1. **S3 logo upload.** The logo must be uploaded to `s3://static.gamma.app/icons/third_party/{filename}` before the PR merges. Uses AWS CLI with the `engineer` role or the AWS console. Matt has flagged interest in automating this.
2. **Terraform apply.** Merging the PR is necessary but not sufficient — the Terraform allowlist change only goes live after someone runs `terraform apply` in the `gamma` server workspace. The onboarding skill explicitly calls this out as a handoff step, but there's currently no post-merge automation to ping eng.

Both are surfaced in the skill's Step 8 (post-merge apply + verification).

## Deltas from Matt's original Notion writeup

Material changes since Matt wrote the canonical process doc:

- **Allowlist moved from Parameter Store to Terraform** ([#18376](https://github.com/gamma-app/gamma/pull/18376), 2026-03 ish). Before: `OAUTH_DCR_ALLOWED_REDIRECT_URLS` was an AWS Systems Manager parameter you had to edit via the console. After: it's a Terraform variable in `prod.tfvars` that flows through a normal PR review. This made onboarding a normal code-review step but introduced the Terraform-apply handoff as a new manual step.
- **Batch PR model** ([#18530](https://github.com/gamma-app/gamma/pull/18530) onwards). Before: one PR per connector. After: weekly-ish batch PRs covering multiple approved connectors. The skill's batch mode implements this.
- **Staging allows everything**: `packages/server/terraform/staging.tfvars` sets `oauth_dcr_allowed_redirect_urls = [".*"]`. No staging changes required per onboarding.

## Approval gate

Before any code change, confirm Byron approved the connector in the sheet. This is non-negotiable — the skill has an explicit approval-gate check, and the batch PR model only includes approved connectors. "Approved in the sheet" means eligible for the next batch; it does **not** mean "merge without running the technical validations."

## Reference PR

[PR #18152 (Grok)](https://github.com/gamma-app/gamma/pull/18152) is the skill's reference example. The worked example in `reference.md` walks through the exact three-file diff for Grok. Use it as the shape check for any single-connector onboarding.

For batch PRs, use [#18530](https://github.com/gamma-app/gamma/pull/18530) or [#18885](https://github.com/gamma-app/gamma/pull/18885) as the shape check.
