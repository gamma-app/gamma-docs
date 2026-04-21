---
description: >-
  What the Gamma API covers today and how to work within its current scope.
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

# API scope and limits

The Gamma API focuses on content generation and workspace management. Common use cases that sit outside that scope are covered below with the closest workaround.

### Quick reference

- The API creates gammas but does not edit existing ones.
- Generation is asynchronous: create, then poll until complete.
- Export URLs are temporary -- download files promptly.
- Image URLs can be included in `inputText` but must be publicly accessible.
- Submit feature requests on our [Canny board](https://meetgamma.canny.io).

### What the API covers

| Capability | Endpoint |
| --- | --- |
| Generate a gamma from text | `POST /generations` |
| Generate from an existing template | `POST /generations/from-template` |
| Poll generation status and get results | `GET /generations/{id}` |
| List available themes | `GET /themes` |
| List workspace folders | `GET /folders` |

{% hint style="info" %}
The API focuses on generation — each call produces a new, fully styled gamma. All generation is asynchronous: start a generation with `POST /generations`, then poll for the result with `GET /generations/{id}`. See [Poll for results](async-patterns-and-polling.md) for the full workflow.
{% endhint %}

### Working outside the current scope

#### Updating content after generation

The API creates gammas but does not modify existing ones. To update content, generate a new gamma with the revised input.

#### Waiting for generation to complete

The API uses an asynchronous polling model. After creating a generation, poll `GET /generations/{id}` until the status is `completed` or `failed`. See [Poll for results](async-patterns-and-polling.md) for implementation patterns across platforms.

#### Exporting files

A completed generation includes an `exportUrl` for downloading the output. This URL is signed and expires after approximately one week.

#### Providing your own images

You can include image URLs directly in your `inputText`. Gamma fetches and re-hosts them during generation. See [Image URL best practices](image-url-best-practices.md) for URL requirements and troubleshooting.

#### Generating charts and structured content

Charts, tables, and infographics can be prompted for through your input text. Results vary across runs — for more predictable layouts, use the template-based generation endpoint. See [Charts and structured content](charts-and-structured-content.md).

### Related

- [Generate from text](generate-api-parameters-explained.md) for the full parameter reference
- [Poll for results](async-patterns-and-polling.md) for the polling workflow
- [Image URL best practices](image-url-best-practices.md) for including your own images
- [Get Help](get-help.md) for support channels
