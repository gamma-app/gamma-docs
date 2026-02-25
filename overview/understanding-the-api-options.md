---
description: Overview of the different API offerings and when to use each.
---

# Understanding the API options

{% hint style="warning" %}
**The Create from Template API is currently in beta.**

Functionality, rate limits, and pricing are subject to change.
{% endhint %}

There are two ways to create gammas using our APIs: generate from scratch ([Generate API](generate-api-parameters-explained.md)) and create based on an existing template ([Create from Template API](create-from-template-api-parameters-explained.md)).

| Callouts               | Generate API                                                                                                                                                                                                                  | Create from Template API                                                                                                                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When to use            | <ul><li>Create a net new gamma (without an existing template).</li><li>Users have maximum flexibility to specify parameters.</li><li>Gamma uses full range of tools within defined parameters to create the output.</li></ul> | <ul><li>Create a new gamma based on an existing gamma template.</li><li>Allows users to define a good template with the Gamma app.</li><li>Gamma adapts new content to the existing template.</li></ul> |
| Important distinctions | <ul><li>Has many parameters to provide users maximum flexibility.</li><li>Use <code>inputText</code> to pass in text content and image URLs. Use other parameters to pass in more guidance.</li></ul>                         | <ul><li>Requires an existing gamma template and its gammaId.</li><li>Use <code>prompt</code> to pass in text content, image URLs, as well as instructions for how to use this content.</li></ul>        |

Additionally, you can use GET Themes and GET Folders APIs to retrieve all available options for themes and folders.
