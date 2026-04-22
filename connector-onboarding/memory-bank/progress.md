# Progress

## What works

- Three-file onboarding pattern is mechanical and stable across ~25 live connectors
- Batch PR model validated twice (#18530, #18885), covering 20 connectors across 2 PRs
- TypeScript safety net catches most missing-logo bugs at `yarn workspace server build` time
- Skill-driven execution keeps the approval gate honest (Byron's approval verified in the sheet)
- PR catalog here separates real onboardings from the ~4 infra-adjacent PRs that touched the same files

## What's left to build

1. Automate S3 logo upload (Matt flagged interest; no owner)
2. Post-merge Terraform apply handoff — Slack ping or GitHub Action, whichever is simpler
3. Admin UI for redirect URI management (Matt's long-term direction)
4. Periodic sheet reconciliation — flag approved-but-not-live connectors older than N days
5. Possibly: surface `oauthClientType` on APM spans so live monitoring doesn't require Snowflake (separate discussion in `#api` earlier this month)

## Current status

Steady-state. Two batches shipped in the last ~3 weeks with ~10 connectors each. The process has settled into "review sheet, draft batch PR, merge, Terraform apply." No open questions on the three-file pattern itself.

This memory bank is first-pass — created to stop re-deriving context each session. Will refine after the next real onboarding uses it.

## Known issues

- **`git log --follow` noise.** Session checkpoints and unmerged branches appear when tracking `oauth-client-type.ts` history. Filter to `main`. Documented in `pr-catalog.md`.
- **Terraform apply is a silent requirement.** Merging the PR does not deploy the allowlist change. No automation yet.
- **S3 logo upload is a silent requirement.** Must happen before the PR merges, or the consent page shows `null` for the logo.
- **No live monitoring by connector.** Can filter Snowflake by `oauthClientType` for historical analysis; APM is workspace-scoped. Span tag proposal is in flight.

## Evolution of project decisions

- **2025-12-ish → 2026-01**: First connectors (Atlassian, Glean, ChatGPT, Claude) added as one-offs; `oauth-client-type.ts` didn't exist yet. Resolver logo mapping was the only shared surface.
- **2026-01-12 (#15679)**: `oauth-client-type.ts` introduced — formalizes the typed client classification. Glean suffix match pattern born here.
- **2026-02-10 (#16599)**: ChatGPT multi-host support added; establishes the pattern for connectors with multiple callback hostnames.
- **2026-03-ish (#18376)**: Redirect URI allowlist migrates from AWS Parameter Store to Terraform `prod.tfvars`. Biggest process shift of the year — turns allowlist changes into normal PR review but introduces Terraform apply as a new manual step.
- **2026-03-30 (#18530)**: First batch PR. One PR covering 10 connectors. Shifts the onboarding cadence from one-off-per-PR to weekly-ish batches.
- **2026-04-17 (#18885)**: Second batch confirms the batch model is working; includes a URI correction for Peripheral.
