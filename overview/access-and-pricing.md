# Access and Pricing

## Access

* API access is available to subscribers on Pro, Ultra, Teams, and Business plans. View [pricing plans here](https://gamma.app/pricing).
* To get started, you can generate an API key through your account settings as shown below.

<div data-with-frame="true"><figure><img src="https://files.readme.io/2192df8ddd3190fe7d98eb06e2f5370d3a8300f2251bb0aa83a63790f3e35c6a-CleanShot_2025-07-28_at_12.43.382x.png" alt=""><figcaption></figcaption></figure></div>

## Usage and pricing

* API billing is conducted using a credit-based system, and higher tier subscribers receive more monthly credits.
* If you run out of credits, you can upgrade to a higher subscription tier, purchase credits ad hoc, or enable auto-recharge (_recommended_) at [https://gamma.app/settings/billing](https://gamma.app/settings/billing)

<div data-with-frame="true"><figure><img src="https://files.readme.io/7088518f8139672d05c42610c1e1a172e600d6f00ec2e6a16c5d0f45f7e46c7a-CleanShot_2025-10-01_at_07.40.082x.png" alt=""><figcaption></figcaption></figure></div>

## How credits work

Credit charges are determined based on several factors and are returned in the GET response.

| Feature         | API parameter        | Credits Charged\*                                                                                                                                         |
| --------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of cards | `numCards`           | 3-4 credits/card                                                                                                                                          |
| AI image model  | `imageOptions.model` | - Basic models: \~2 credits/image - Advanced models: \~10-20 credits/image - Premium models: \~20-40 credits/image - Ultra models: \~40-120 credits/image |

\*Credit charges subject to change.

## **Illustrative scenarios**

* Deck with 10 cards + 5 images generated using a basic image model = \~40-50 credits
* Doc with 20 cards + 15 images generated using a premium image model = \~360-680 credits
* Socials with 30 cards + 30 images generated using an ultra image model = \~1290-3720 credits

To learn more about credits, you can visit our [Help Center](https://help.gamma.app/en/articles/7834324-how-do-ai-credits-work-in-gamma).
