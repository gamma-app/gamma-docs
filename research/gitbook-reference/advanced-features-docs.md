Here is the combined markdown from all scraped GitBook pages:

---

## Page: https://gitbook.com/docs/creating-content/blocks/openapi

**Note:** This URL returned 404. The OpenAPI docs live under `api-references/openapi`. Content from those pages is included below.

---

## Page: https://gitbook.com/docs/api-references/openapi

Manually writing REST API documentation can be time-consuming. GitBook simplifies this by letting you import OpenAPI documents that describe your API’s structure and behavior.

The OpenAPI Specification (OAS) is a framework for documenting REST APIs. Written in JSON or YAML, it describes endpoints, parameters, schemas, and authentication schemes.

Once imported into GitBook, these documents become interactive, testable API blocks that show your API methods, whether the spec is provided as a file or loaded from a URL.

GitBook supports [Swagger 2.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md) or [OpenAPI 3.0](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md) compliant files.

### Add a new pet to the store.

post /api/v3/pet

Add a new pet to the store.

**Required scopes**

This endpoint requires the following scopes:

- `write:pets`: modify pets in your account
- `read:pets`: read your pets

**Authorizations**

petstore_auth — OAuth2 implicit

Authorization URL: https://petstore3.swagger.io/oauth/authorize

**Body**

application/json — application/json, application/xml, application/x-www-form-urlencoded

- id — integer · int64 — Optional — Example: `10`
- name — string — Required — Example: `doggie`
- category — object — Optional
- photoUrls — string[] — Required
- tags — object[] — Optional
- status — string · enum — Optional — pet status in the store — Possible values: `available`, `pending`, `sold`

**Responses**

- 200 — Successful operation
- 400 — Invalid input
- 422 — Validation exception
- default — Unexpected error

### Test it (powered by Scalar)

GitBook’s OpenAPI block supports a “test it” feature so users can try API methods with data and parameters filled in from the editor.

Powered by [Scalar](https://scalar.com/), users can test API methods directly in the docs.

#### FAQ

**Why isn’t my spec loading?**

**Note:** This applies only to specs added by URL.

If you added your specification via URL, your API must allow cross-origin GET requests from your docs site. In your API’s CORS settings, allow the exact origin where your docs are hosted (e.g. `https://your-site.gitbook.io` or `https://docs.example.com`).

If your endpoint is public and doesn’t use credentials, you can also return: `Access-Control-Allow-Origin: *`

---

## Page: https://gitbook.com/docs/api-references/openapi/add-an-openapi-specification

If you have an OpenAPI spec, you can add it to your organization by uploading the file, linking to a hosted URL, or using the [GitBook CLI](https://gitbook.com/docs/developers/integrations/reference).

### How to add a specification

1. Open the **OpenAPI** section in the sidebar
2. Click **Add specification**
3. Give your specification a name (especially useful if you manage multiple specs)
4. Choose one of:
   - Upload a file (e.g. _openapi.yaml_)
   - Enter a URL to a hosted spec
   - Use the CLI to publish the spec

### Update your specification

You can update your OpenAPI specification at any time via the GitBook UI or the CLI, regardless of how it was first added.

#### In GitBook application

In the OpenAPI panel:

- If your spec is linked to a URL:
  - GitBook checks for updates automatically every 6 hours.
  - To fetch updates immediately, click **Check for updates**.
- If your spec was uploaded as a file:
  - Click **Update** to upload a new version.
- You can switch from a file to a URL source by clicking **Edit** in the breadcrumb actions menu.

#### Using the CLI

Use the same command to update your specification:

```
gitbook openapi publish --spec api-spec-name --organization organization_id <path-or-url>
```

You can also use the CLI to **Check for updates** by running the publish command on the same URL.

See [Integrating with CI/CD](https://gitbook.com/docs/api-references/guides/support-for-ci-cd-with-api-blocks) for automating spec updates.

---

## Page: https://gitbook.com/docs/api-references/openapi/insert-api-reference-in-your-docs

GitBook can automatically generate pages for endpoints in your OpenAPI spec. These pages include OpenAPI operation blocks so you and your visitors can test endpoints and explore them using the spec.

Endpoints added from your spec are updated whenever the spec is updated. See [Update your specification](https://gitbook.com/docs/api-references/openapi/add-an-openapi-specification#update-your-specification).

### Automatically create OpenAPI pages from your spec

After you’ve [added your OpenAPI spec](https://gitbook.com/docs/api-references/openapi/add-an-openapi-specification), you can generate endpoint pages by inserting an **OpenAPI Reference** in the table of contents of a Space.

1. **Generate pages from OpenAPI**  
   In the space where you want endpoint pages, click **Add new...** at the bottom of the space’s [table of contents](https://gitbook.com/docs/resources/gitbook-ui#table-of-contents).  
   Click **OpenAPI Reference**.

2. **Choose your OpenAPI spec**  
   Select your uploaded OpenAPI spec and click **Insert** to add your endpoints to the space. You can optionally add a models page referencing all OpenAPI schemas.

3. **Manage your API operations**  
   GitBook generates pages from your OpenAPI spec and the tags in its definition.  
   See [Structuring your API reference](https://gitbook.com/docs/api-references/guides/structuring-your-api-reference) for organizing operations.

### Add an individual OpenAPI block

You can also add OpenAPI operations or schemas individually to pages.

1. **Add a new OpenAPI block**  
   Open the block selector with **/** and search for OpenAPI.

2. **Choose your OpenAPI spec**  
   Select your uploaded OpenAPI spec and click **Continue** to choose endpoints.

3. **Choose the operations or schemas you want to insert**  
   Pick the operations and schemas and click **Insert**.

---

## Page: https://gitbook.com/docs/creating-content/blocks/math-and-tex

You can use the mathTeX format to include mathematical formulae in your documentation via the [KaTeX](https://katex.org/docs/supported.html) library.

You can also add mathTeX [as inline content](https://gitbook.com/docs/creating-content/formatting/inline#math-and-tex).

### Example of Math & TeX block

$$s = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2}$$

### Representation in Markdown

$$f(x) = x * e^{2 pi i \xi x}$$

```
# Math and TeX block

$$f(x) = x * e^{2 pi i \xi x}$$
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/drawing

You can create a drawing or sketch directly in GitBook using the integrated [Excalidraw](https://excalidraw.com/) editor and add it to your page.

To create a drawing, press `/` on an empty line to open the insert palette and choose **Drawing**. A popover with Excalidraw tools opens; close it when you’re done and the diagram appears on the page.

GitBook stores drawings as special SVG files in the space with the extension `drawing.svg`.

### Example of a drawing block

A diagram drawn in GitBook

### Draw with GitBook AI

This feature is available on [Pro and Enterprise plans](https://www.gitbook.com/pricing).

In a drawing block, you can ask GitBook AI to generate an illustration with a prompt. Type a prompt and click **Generate**, or use one of the suggested prompts.

When GitBook AI finishes the drawing, double-click to open the full drawing palette and edit it.

When editing a drawing, click **Use AI to generate** to open the prompt editor again and generate a new drawing.

### Representation in Markdown

```
<img src="https://example.com/file.svg" alt="Example diagram description" class="gitbook-drawing">
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/synced-blocks

**Note:** This URL returned 404. The equivalent feature is **Reusable content** at `reusable-content`. That content is included below.

---

## Page: https://gitbook.com/docs/creating-content/reusable-content

This feature is available on [Pro and Enterprise plans](https://www.gitbook.com/pricing).

Reusable content lets you sync content across multiple pages and spaces so you can edit all instances of the block at once.

### Fundamentals

Reusable content behaves like other content: you can modify it via change requests, include it in review workflows, and it renders correctly on published sites.

Reusable content can be referenced across multiple spaces but belongs to a single _parent space_.

### The "parent space" concept

The parent space owns the reusable content and is the only place where it can be edited.

Updates appear in all instances, but all changes must come from the parent space—either as a direct edit or through a change request.

Spaces support editorial workflows and security. Because GitBook uses permission-based editing, reusable content can only be changed from its parent space, even when reused across the organization.

### Known limitations

#### Integrations

Blocks from integrations are not supported in reusable content. Integrations are installed per space, and limiting access keeps third-party integrations within the permissions you grant. Referencing reusable content across spaces would break this boundary.

#### Search

Reusable content currently appears in search results only within its parent space. Work is underway to remove this limitation.

### In the app

#### Create reusable content

Select one or more blocks, open the **Actions menu**, choose **Turn into**, then **Reusable content**. You can give the block a name for easier reuse.

Alternatively, select one or more blocks and press **Cmd + C** to open a prompt asking if you want to create reusable content.

#### Insert reusable content

Press `/` on an empty line to open the **Insert palette** and search for your content by name or for “reusable”. Or click the `+` next to any block or empty line.

You can also use the reusable content panel in the pages sidebar to see previously created blocks in the current space.

#### Edit reusable content

Reusable content can be edited like other content: directly if [live edits](https://gitbook.com/docs/collaboration/live-edits) are enabled, or via [a change request](https://gitbook.com/docs/collaboration/change-requests) otherwise. Changes sync everywhere the content is used.

If you edit inside a change request, the content syncs to all instances when the change request is merged.

#### Detach reusable content

Open the **Actions menu** and select **Detach**. Detaching converts the content back to regular blocks.

After detaching, changes to the block(s) no longer sync to other instances, and changes in other instances do not affect the detached block(s). Other instances remain synced.

#### Delete reusable content

Find the reusable content in the page’s table of contents, open the **Actions menu**, and select **Delete**.

Deleting reusable content removes it from all pages where it is used. This cannot be undone.

### Syncing with GitHub & GitLab

Reusable content is supported when syncing to GitHub & GitLab. It is exported to an `includes` folder, with each block as a separate Markdown file.

Other pages reference it using the `includes` directive.

When syncing, the `.gitbook/includes` directory is created in the root of each synced space (which may not be the repository root). If `.gitbook/includes` or its files appear in the table of contents, you may need to hide them manually.

#### Example

If you’re writing on the GitHub side, use a path to the include that is relative to the file containing the reference (not the repository root):

```
{% include "../../.gitbook/includes/reusable-block.md" %}
```

---

## Page: https://gitbook.com/docs/creating-content/variables-and-expressions

Variables let you create reusable text that can be referenced in [expressions](https://gitbook.com/docs/creating-content/formatting/inline#expressions) and [conditions for adaptive content](https://gitbook.com/docs/publishing-documentation/adaptive-content/adapting-your-content#working-with-the-condition-editor).

If you repeat the same name, phrase, or version number in multiple places, you can create a **variable** to keep them in sync and accurate.

Variables can be scoped to a single page or to a single space.

### Create a new variable

Click **Library** in the Table of Contents when editing an open [change request](https://gitbook.com/docs/collaboration/change-requests). Then click **Variables**.

Use the toggle at the top to view and create variables for the current page or for all pages in the current space.

Click **Create a variable** to open a modal where you can set a name and value.

Click **Add variable** to save.

Variable names must start with a letter and can contain letters, numbers, and underscores.

### Use variables in your content

Variables are referenced in [expressions](https://gitbook.com/docs/creating-content/formatting/inline#expressions), which you can insert inline. Double-click an expression to open the expression editor.

Page-scoped variables are under `page.vars`. Space-scoped variables are under `space.vars`.

### Update a variable

You can update a variable at any time within a change request. Changing its value updates every expression that references it. The updated variable goes live when the change request is merged.

---

## Page: https://gitbook.com/docs/creating-content/blocks/page-link

Page link blocks are a good way to create relations between different pages. They stand out because they occupy their own block, unlike hyperlinks in text.

### Example of page link block

The links below point to [blocks](https://gitbook.com/docs/creating-content/blocks) and [inline content](https://gitbook.com/docs/creating-content/formatting/inline):

Blocks → | Inline content →

### Representation in Markdown

```
{% content-ref url="./" %} . {% endcontent-ref %}
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/quote

Quotes are useful when you want to include something from another source.

Start a quote by typing `>` followed by `Space` in an empty paragraph, or use the [insert palette](https://gitbook.com/docs/creating-content/blocks#inserting-a-new-content-block). You can also convert a paragraph to a quote by selecting it and pressing `>`.

### Example of a quote

> "No human ever steps in the same river twice, for it's not the same river and they are not the same human." — _Heraclitus_

### Representation in Markdown

```
> "No human ever steps in the same river twice, for it's not the same river and they are not the same human." — _Heraclitus_
```

---

## Page: https://gitbook.com/docs/creating-content/searching-your-content/gitbook-ai

GitBook AI lets you ask questions or add more context. It reviews your documentation in real time and gives quick, direct answers.

GitBook AI search is available in the GitBook app for internal content and [in published content for that docs site](https://gitbook.com/docs/publishing-documentation/ai-search).

### GitBook AI helps you find answers in the GitBook app

This feature is available on [Pro and Enterprise plans](https://www.gitbook.com/pricing).

You can enable GitBook AI for your organization’s internal content so people can ask questions and get semantic answers about your knowledge base.

In **Organization settings** → **General**, turn on **Enable GitBook AI**.

### Using GitBook AI search

With GitBook AI enabled, open the **Ask or search** menu from the left sidebar and type a question. GitBook AI scans your documentation and summarizes results.

### FAQs

#### How long does it take for GitBook AI to index changes?

After changes (e.g. a merged [change request](https://gitbook.com/docs/collaboration/change-requests)), it can take up to one hour for GitBook to index and reflect them in AI search.

#### How does GitBook AI handle my data?

Content is sent to OpenAI for indexing and processing. OpenAI does not use this content for service improvements (including model training). See how OpenAI handles data [here](https://openai.com/blog/introducing-chatgpt-and-whisper-apis#developer-focus).

#### How do I prevent hallucinations with GitBook AI search?

If answers are incorrect, add explicit content about the topic so the AI has less room to guess.

---

## Page: https://gitbook.com/docs/publishing-documentation/publish-a-docs-site

After writing, editing, or importing content, you can publish it as a docs site. Your docs will be available on the web to your chosen audience.

Content comes from [spaces](https://gitbook.com/docs/creating-content/content-structure/space) in your organization. When you create a new docs site, you can create a new space or link an existing one.

### Create a docs site

Click the **+** icon next to **Docs site** in the sidebar to open the docs site wizard.

Give the site a name, choose a starting point for content, and decide whether to publish now or later.

To use content from an existing space, open that space and click **Share** in the top-right, then choose **Publish as a docs site**.

### Publish a docs site

By default, sites are published publicly. You can change visibility in [site settings](https://gitbook.com/docs/publishing-documentation/site-settings).

**Public** — Publish docs publicly on the web.

**Privately with share links** — Publish docs with private share links.

**Authenticated Access** — Protect published docs behind OAuth sign-in.

### Delete or unpublish a docs site

To delete a docs site, open its dashboard and go to [**Site settings**](https://gitbook.com/docs/publishing-documentation/site-settings#delete-site) in the top-right.

### Site editing permissions

Docs sites inherit editing permissions from the [spaces](https://gitbook.com/docs/creating-content/content-structure/space) linked to them.

You can view permissions from the docs site’s **Overview** page and see which space each permission comes from. To change permissions, open the space and click **Share**.

Users with **Administrator** or **Creator** on any space linked to a docs site have full access to the site and its publishing and customization settings.

Users with **Reviewer**, **Editor**, **Commenter**, or **Reader** on any linked space have read-only access to the site and cannot change settings.

---

## Page: https://gitbook.com/docs/publishing-documentation/site-settings

Some customization features are only available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).

### General

- **Site title** — Change the site name; without a custom logo, this is what visitors see.
- **Insights cookie** — To use [built-in insights](https://gitbook.com/docs/publishing-documentation/insights), the site uses cookies to identify returning visitors. You can disable these cookies, but insights will not work.
- **Unpublish site** — Unpublish the site but keep settings and customizations. You can publish again later.
- **Delete site** — Unpublish and remove the site from the **Docs site** section. Deleting is permanent and cannot be undone. Settings and customizations are lost; content remains in its [space](https://gitbook.com/docs/creating-content/content-structure/space).

### Audience

- **Audience** — Choose who can see published content. See [Publish a docs site](https://gitbook.com/docs/publishing-documentation/publish-a-docs-site).
- **Adaptive content** (Ultimate) — Turn on adaptive content for pages, variants, and sections. [Adaptive content](https://gitbook.com/docs/publishing-documentation/adaptive-content) lets you show or hide content based on visitor permissions. Your visitor token signing key is shown here.

### Domain and URL

- **Custom domain** — Configure a custom domain. See [Set a custom domain](https://gitbook.com/docs/publishing-documentation/custom-domain).
- **GitBook Subdirectory** — Publish content on a subdirectory (e.g. `yourcompany.com/docs`). See [GitBook Subdirectory](https://gitbook.com/docs/publishing-documentation/site-settings#gitbook-subdirectory).

### Redirects

- **Site redirects** — See [Site redirects](https://gitbook.com/docs/publishing-documentation/site-redirects).

### Features

- **PDF export** (Premium & Ultimate) — Let visitors export your GitBook as PDF. See [PDF export](https://gitbook.com/docs/collaboration/pdf-export).
- **Page ratings** (Premium & Ultimate) — Let visitors rate each page (sad, neutral, or happy). View results in [**Insights**](https://gitbook.com/docs/publishing-documentation/insights) → [**Content scores**](https://gitbook.com/docs/publishing-documentation/insights#content-scores).

### AI & MCP

- **Choose the AI experience** (Premium & Ultimate) — Let visitors use AI search or the GitBook assistant. See [AI Search](https://gitbook.com/docs/publishing-documentation/ai-search).
- **Extend it with MCP connectors** (Ultimate) — Configure MCP servers for the AI assistant. See [AI Search](https://gitbook.com/docs/publishing-documentation/ai-search#how-do-i-use-gitbook-ai).

### Structure

- **Site structure** — See [Site structure](https://gitbook.com/docs/publishing-documentation/site-structure).

### Plan

- **Plans** — See [Plans](https://gitbook.com/docs/account-management/plans).

---

## Page: https://gitbook.com/docs/publishing-documentation/site-redirects

This feature is available on [Premium and Ultimate site plans](https://www.gitbook.com/pricing).

Site redirects help when migrating or restructuring documentation to avoid broken links and protect SEO.

Redirects are often used when moving docs from another provider (e.g. to GitBook). Broken links can hurt SEO, so redirects are recommended where needed.

In addition to [automatic redirects created by GitBook](https://gitbook.com/docs/publishing-documentation/site-redirects#about-automatic-redirects), you can create a redirect from any path on your site’s domain.

Redirects can be **Live** or **Draft**. Draft redirects let you prepare and review rules before publishing. Drafts do not affect the live site until enabled.

### Managing redirects on your site

Open your site’s dashboard in GitBook, go to the **Settings** tab, then click **Domain & redirects**.

### Creating redirects

Click **Add redirect** and choose **Manual**.

Enter the **source path** (URL slug to redirect) and the **destination** (section, variant, or page on your site).

Click **Enable redirect** to enable immediately.

To create a redirect without making it live, click **Save as draft**. Draft redirects appear in the **Draft** tab and can be enabled later.

**Wildcard redirects** — Add `*` at the end of the source path, e.g.:

- `/docs/*` — matches everything under `/docs/`
- `/changelog*` — matches paths starting with `/changelog`

When the source path includes a wildcard (`*`), you can enable **Replace wildcard with matched text**:

- **On:** The part matched by `*` is appended to the destination path.  
  Example: source `/docs/*` → destination `/help`  
  `/docs/install` redirects to `/help/install`

- **Off:** All matched URLs redirect to the same fixed destination.  
  Example: source `/docs/*` → destination `/help`  
  `/docs/install` redirects to `/help`

To add another redirect to the same page, toggle **Add another redirect** before clicking **Enable redirect** or **Save as draft**. The modal stays open with the same destination so you can add another source path.

### Editing redirects

Click the **Edit** icon next to a redirect in the list. Update it and click **Enable redirect** to publish.

If the redirect is a draft, you can enable it from the edit modal by clicking **Enable redirect**.

### Enabling draft redirects

Draft redirects appear in the **Draft** tab.

You can publish a draft redirect by:

- Opening it and clicking **Enable redirect** in the edit modal
- Using the toggle in the table

Once enabled, the redirect moves to the **Live** tab and starts routing visitors.

### Import redirects from a CSV

Click **Add redirect** and choose **Upload CSV**.

Upload a CSV with columns `source`, `destination`, and optional `intent`:

- `source` — Path to redirect (e.g. `/docs/site-redirects`)
- `destination` — Page admin URL, external URL, or empty (depending on intent)
- `intent`:
  - `live`, blank, or omitted — create, update, or remove a live redirect
  - `draft` — create, update, or remove a draft redirect
  - `publish` — publish an existing draft to live; `destination` must be empty

Maximum 500 rows per import.

If the CSV has duplicate `source` values, only the first row is processed. The import is an upsert: existing redirects with the same source are updated; new ones are created.

If any rows fail, an error CSV is available from the bottom-right toast with `source`, `destination`, and a short explanation for each error.

#### CSV Examples

| source | destination | intent | Result |
|--------|-------------|--------|--------|
| /docs/site-redirects | https://example.com/page | blank | Create or update a live redirect |
| /docs/site-redirects | https://example.com/page | live | Create or update a live redirect |
| /docs/site-redirects | https://example.com/page | draft | Create or update a draft redirect |
| /docs/site-redirects | empty | blank | Remove the live redirect |
| /docs/site-redirects | empty | live | Remove the live redirect |
| /docs/site-redirects | empty | draft | Remove the draft redirect |
| /docs/site-redirects | empty | publish | Publish the existing draft redirect to live |

### About automatic redirects

When pages are moved or renamed, their canonical URL changes. GitBook automatically creates [HTTP 307](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/307) redirects from the old URL to the new one.

URL resolution order:

1. Site content is resolved to its canonical URL by following automatic redirects.
2. If the URL cannot be resolved, it is checked against [space-level redirects](https://gitbook.com/docs/getting-started/git-sync/content-configuration#redirects) in `.gitbook.yaml`.
3. Finally, it is checked against site-level redirects created via the process above.

---

**Summary:** Two original URLs returned 404: `creating-content/blocks/openapi` and `creating-content/blocks/synced-blocks`. Their content is included from the equivalent pages: `api-references/openapi` (and related OpenAPI pages) and `creating-content/reusable-content`.