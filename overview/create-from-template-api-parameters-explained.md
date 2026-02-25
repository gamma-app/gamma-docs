---
description: >-
  What Create from Template API parameters represent and how they affect your
  Gamma creation. Read this before heading to the API Reference page.
---

# Create from Template API parameters explained

The sample API requests below shows all required and optional API parameters, as well as sample responses.

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/generations/from-template" method="post" %}
[OpenAPI gamma-public-api-v1](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/64e5670ce8c5ac46f8236700d6e5e8826c5ae2cc7a1dbfb2c3ebf44c91189ea3.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260225%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260225T011459Z&X-Amz-Expires=172800&X-Amz-Signature=e00c73752081bed71ca024031eba465fb36e3b7e64f1150279167f11522eb2b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

{% openapi-operation spec="gamma-public-api-v1" path="/v1.0/generations/{id}" method="get" %}
[OpenAPI gamma-public-api-v1](https://4401d86825a13bf607936cc3a9f3897a.r2.cloudflarestorage.com/gitbook-x-prod-openapi/raw/64e5670ce8c5ac46f8236700d6e5e8826c5ae2cc7a1dbfb2c3ebf44c91189ea3.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=dce48141f43c0191a2ad043a6888781c%2F20260225%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20260225T011459Z&X-Amz-Expires=172800&X-Amz-Signature=e00c73752081bed71ca024031eba465fb36e3b7e64f1150279167f11522eb2b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
{% endopenapi-operation %}

## Top level parameters

### `gammaId` _(required)_

Identifies the template you want to modify. You can find and copy the gammaId for a template as shown in the screenshots below.

{% columns %}
{% column %}
<figure><img src="https://files.readme.io/9464bbfb332e5c5798be313563bb9e0c91153fbb28bc88d4da79ac7a2faf865b-CleanShot_2025-11-03_at_15.10.362x.png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}

{% column %}
<figure><img src="https://files.readme.io/a5a8861282b3bf86679595b2cf684fce46ac54c0059f9ff19d7dcfd411e8aed7-CleanShot_2025-11-03_at_15.16.562x.png" alt=""><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

### `prompt` _(required)_

Use this parameter to send text content, image URLs, as well as instructions for how to use this content in relation to the template gamma.

#### **Add images to the input**

You can provide URLs for specific images you want to include. Simply insert the URLs into your content where you want each image to appear (see example below). You can also add instructions for how to display the images, eg, "Group the last 10 images into a gallery to showcase them together."

#### **Token limits**

The total token limit is 100,000, which is approximately 400,000 characters, but because part of your input is the gamma template, in practice, the token limit for your prompt becomes shorter. We highly recommend keeping your prompt well below 100,000 tokens and testing out a variety of inputs to get a good sense of what works for your use case.

#### **Other tips**

* Text can be as little as a few words that describe the topic of the content you want to generate.
* You can also input longer text -- pages of messy notes or highly structured, detailed text.
* You may need to apply JSON escaping to your text. Find out more about JSON escaping and [try it out here](https://www.devtoolsdaily.com/json/escape/).

{% code title="Example" %}
```json
"prompt": "Change this pitch deck about deep sea exploration into one about space exploration."
```
{% endcode %}

{% code title="Example" %}
```json
"prompt": "Change this pitch deck about deep sea exploration into one about space exploration. Use this quote and this image in the title card: That's one small step for man, one giant leap for mankind - Neil Armstrong, https://www.global-aero.com/wp-content/uploads/2020/06/ga-iss.jpg"
```
{% endcode %}

### `themeId` _(optional, defaults to workspace default theme)_

Defines which theme from Gamma will be used for the output. Themes determine the look and feel of the gamma, including colors and fonts.

* You can use the [GET Themes](https://app.gitbook.com/s/IrzC0mooWT36AKgnkerQ/endpoints/default#get-v1.0-themes) endpoint to pull a list of themes from your workspace. Or you can copy over the themeId from the app directly.

<div data-with-frame="true"><figure><img src="https://files.readme.io/d01171ca7562e427d8469ee2d0391e54400235ca558d6da8e61cf35e957d8833-CleanShot_2025-11-03_at_14.24.272x.png" alt=""><figcaption></figcaption></figure></div>

{% code title="Example" %}
```json
"themeId": "abc123def456ghi"
```
{% endcode %}

### `folderIds` _(optional)_

Defines which folder(s) your gamma is stored in.

*   You can use the [GET Folders](https://app.gitbook.com/s/IrzC0mooWT36AKgnkerQ/endpoints/default#get-v1.0-folders) endpoint to pull a list of folders. Or you can copy over the folderIds from the app directly.

    <div data-with-frame="true"><figure><img src="https://files.readme.io/eefcb9b3f6404e96978f1a92aed2820c178ed1dbf550873c6e3da0538c466740-CleanShot_2025-11-03_at_14.27.362x.png" alt=""><figcaption></figcaption></figure></div>
* You must be a member of a folder to be able to add gammas to that folder.

```json
"folderIds": ["123abc456def", "456123abcdef"]
```

### `exportAs` _(optional)_

Indicates if you'd like to return the generated gamma as a PDF or PPTX file as well as a Gamma URL.

* Options are `pdf` or `pptx`
* Download the files once generated as the links will become invalid after a period of time.
* If you do not wish to directly export to a PDF or PPTX via the API, you may always do so later via the app.

{% hint style="warning" %}
**One export format per request.** You can export to PDF \*or\* PPTX, but not both in a single API call. If you need both formats, make two separate generation requests or export the second format manually from the Gamma app.
{% endhint %}

{% code title="Example" %}
```json
"exportAs": "pdf"
```
{% endcode %}

### imageOptions

When you create content from a Gamma template, new images automatically match the image source used in the original template. For example if you used Pictographic images to generate your original template, any new images will be sourced from Pictographic.

For templates with AI-generated images, you can override the default AI image settings using the optional parameters below.

{% code title="Example" %}
```json
"imageOptions": {
    "source": "aiGenerated"
  }
```
{% endcode %}

#### `imageOptions.model` _(optional)_

This field is relevant if the `imageOptions.source` chosen is `aiGenerated`. The `imageOptions.model` parameter determines which model is used to generate images.

* You can choose from the models listed [here](https://app.gitbook.com/s/IrzC0mooWT36AKgnkerQ/accepted-values/image-model-accepted-values).
* If no value is specified for this parameter, Gamma automatically selects a model for you.

{% code title="Example" %}
```json
"imageOptions": {
	"model": "flux-1-pro"
  }
```
{% endcode %}

#### `imageOptions.style` _(optional)_

This field is relevant if the `imageOptions.source` chosen is `aiGenerated`. The `imageOptions.style` parameter influences the artistic style of the images generated. While this is an optional field, we highly recommend adding some direction here to create images in a cohesive style.

* You can add one or multiple words to define the visual style of the images you want.
* Adding some direction -- even a simple one word like "photorealistic" -- can create visual consistency among the generated images.
* Character limits: 1-500.

{% code title="Example" %}
```json
"imageOptions": {
	"style": "minimal, black and white, line art"
  }
```
{% endcode %}

### sharingOptions

#### `sharingOptions.workspaceAccess` _(optional, defaults to workspace share settings)_

Determines level of access members in your workspace will have to your generated gamma.

* Options are: `noAccess`, `view`, `comment`, `edit`, `fullAccess`
* `fullAccess`allows members from your workspace to view, comment, edit, and share with others.

```json
"sharingOptions": {
	"workspaceAccess": "comment"
}
```

#### `sharingOptions.externalAccess` _(optional, defaults to workspace share settings)_

Determines level of access members **outside your workspace** will have to your generated gamma.

* Options are: `noAccess`, `view`, `comment`, or `edit`

{% code title="Example" %}
```json
"sharingOptions": {
	"externalAccess": "noAccess"
}
```
{% endcode %}

#### `sharingOptions.emailOptions` _(optional)_

Allows you to share your gamma with specific recipients via their email address.

{% code title="Example" %}
```json
"sharingOptions": {
  "emailOptions": {
    "recipients": ["ceo@example.com", "cto@example.com"]
}
```
{% endcode %}

#### `sharingOptions.emailOptions.access` _(optional)_

Determines level of access those specified in `sharingOptions.emailOptions.recipients` have to your generated gamma. Only workspace members can have `fullAccess`

* Options are: `view`, `comment`, `edit`, or `fullAccess`

{% code title="Example" %}
```json
"sharingOptions": {
  "emailOptions": {
    "access": "comment"
}
```
{% endcode %}
