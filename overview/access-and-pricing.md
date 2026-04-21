---
description: API access requirements, credit-based pricing, and plan details.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: false
  pagination:
    visible: true
---

# Review access and pricing

### Quick reference

- ChatGPT and Claude connectors work on all plans.
- API keys are available on Pro, Ultra, Teams, and Business plans.
- Credit usage is returned in the `credits` field on `GET /v1.0/generations/{generationId}`.
- Auto-recharge is the safest way to prevent failed generations due to exhausted credits.

### Access

#### API keys (Zapier, Make, n8n, direct integration)

API key access is available on Pro, Ultra, Teams, and Business plans. Generate an API key from [Settings > API Keys](https://gamma.app/settings/api-keys). View [pricing plans here](https://gamma.app/pricing).

<figure><img src="../.gitbook/assets/api-key-settings.png" alt="API key settings in Gamma" width="75%"><figcaption><p>Settings > API Keys</p></figcaption></figure>

#### Connectors (ChatGPT, Claude)

Connectors are available on all plans, including Free and Plus. No API key required — connect directly from [ChatGPT or Claude](connectors-and-integrations.md) and authenticate with your Gamma account. Generations via connectors charge credits the same way as API calls.

### Usage and pricing

* API billing uses a credit-based system. Higher tier subscribers receive more monthly credits.
* If you run out of credits, you can upgrade to a higher subscription tier, purchase credits ad hoc, or enable auto-recharge (_recommended_) at [Settings > Billing](https://gamma.app/settings/billing).

<figure><img src="../.gitbook/assets/billing-credits.png" alt="Credit management in Gamma" width="75%"><figcaption><p>Settings > Billing</p></figcaption></figure>

### How credits work

Credit charges are determined based on several factors and are returned in the GET response.

| Feature         | API parameter        | Credits Charged\*                                                                                                                        |
| --------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Number of cards | `numCards`           | 1-3 credits/card (varies by the text generation model Gamma selects internally)                                                          |
| AI image model  | `imageOptions.model` | Standard: 2-15 credits/image. Advanced: 20-33 credits/image. Premium: 34-75 credits/image. Ultra: 30-125 credits/image. |

\* **Credit consumption rates and the actions that consume credits are subject to change.**

Template-based generations (`POST /generations/from-template`) may cost slightly more per card than standard generations.

### How credits are attributed

Each workspace member has their own credit bucket inside the workspace. Credits do not pool across members.

- **REST API:** calls made with a given API key are attributed to the key's owner. Credits deduct from that user's bucket.
- **MCP (Claude, ChatGPT, custom integrations):** each user authenticates individually via OAuth. Credits deduct from the authenticating user's bucket, even when multiple users share a workspace.

Workspace subscription billing aggregates at the workspace level (one invoice). Credit consumption is tracked per user.

### Illustrative scenarios

* Deck with 10 cards + 5 images using a basic image model = \~20-60 credits
* Doc with 20 cards + 15 images using a premium image model = \~320-1070 credits
* Socials with 30 cards + 30 images using an ultra image model = \~930-3900 credits

Both standard generations (`POST /generations`) and template-based generations (`POST /generations/from-template`) consume credits. Credit usage details are returned in the `credits` field of the `GET /generations/{generationId}` response, showing `deducted` and `remaining` values.

To learn more about credits, visit our [Help Center](https://help.gamma.app/en/articles/7834324-how-do-ai-credits-work-in-gamma).

### Related

- [Connect integrations](connectors-and-integrations.md) for setup instructions by platform
- [Poll for results](async-patterns-and-polling.md) for where `credits.deducted` and `credits.remaining` appear in the generation flow
- [Get Help](get-help.md) if you need support with pricing or API access
