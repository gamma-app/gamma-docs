Here is the concatenated markdown from all 9 pages:

---

## Page: https://gitbook.com/docs/getting-started/git-sync

![A GitBook screenshot showing the Git Sync setup](https://gitbook.com/docs/~gitbook/image?url=https%3A%2F%2F1050631731-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FNkEGS7hzeqa35sMXQZ4X%252Fuploads%252Fo79JqKUo68L5FgJLGdJp%252FGit%2520Sync%25402x.png%3Falt%3Dmedia%26token%3D76a81aba-457d-4821-867d-57ad86fea004&width=768&dpr=3&quality=100&sign=372bdbb6&sv=2)

Set up Git Sync for your GitBook space.

### Overview

Git Sync lets technical teams sync GitHub or GitLab repositories with GitBook and turn Markdown files into docs. You can edit in GitBook’s editor while keeping content in sync with your codebase on GitHub or GitLab.

Git Sync is bi-directional: edits in GitBook and commits on GitHub or GitLab are both synced. Developers can commit from GitHub or GitLab, and technical writers, instructional designers, and product managers can edit, discuss, and give feedback in GitBook.

circle-info

Only [administrators and creators](https://gitbook.com/docs/account-management/member-management/roles) can enable and configure Git Sync.

### skill.md

When working on your docs locally with Git Sync, you can use GitBook's [skill.md file](https://gitbook.com/docs/creating-content/ai-coding-assistants-and-skillmd) to give an AI coding assistant context about GitBook's blocks, features, and best practices.

Last updated 1 month ago

Was this helpful?

---

## Page: https://gitbook.com/docs/getting-started/git-sync/content-configuration

If you want to configure Git Sync further, add a `.gitbook.yaml` file at the root of your repository to tell GitBook how to parse your Git repository.

.gitbook.yaml

Copy

```
root: ./

​structure:
  readme: README.md
  summary: SUMMARY.md​

redirects:
  previous/page: new-folder/page.md
```

### Root

The path for your documentation defaults to the repository root. To use a `./docs` folder:

.gitbook.yaml

Copy

```
root: ./docs/
```

circle-exclamation

**All other options that specify paths are relative to this root folder**. If you set `root` to `./docs/` and `structure.summary` to `./product/SUMMARY.md`, GitBook looks for `./docs/product/SUMMARY.md`.

### ​Structure‌

The structure section has two properties:

- `readme`: The first page of your docs. Default: `./README.md`
- `summary`: The table of contents. Default: `./SUMMARY.md`

Values are paths relative to the `root` option. Example:

.gitbook.yaml

Copy

```
structure:
  readme: ./product/README.md
  summary: ./product/SUMMARY.md
```

circle-exclamation

When Git Sync is enabled, **do not create or modify readme files** in the GitBook UI. Manage the readme only in your GitHub/GitLab repository to avoid conflicts and duplication.

### Summary‌

The `summary` file is a Markdown file (`.md`) with this structure:

./SUMMARY.md

Copy

```
‌# Summary​

## Use headings to create page groups like this one​

* [First page's title](page1/README.md)
    * [Some child page](page1/page1-1.md)
    * [Some other child page](part1/page1-2.md)

* [Second page's title](page2/README.md)
    * [Some child page](page2/page2-1.md)
    * [Some other child page](part2/page2-2.md)

## A second-page group​

* [Another page](another-page.md)
```

Providing a custom summary file is optional. By default, GitBook looks for `SUMMARY.md` in the `root` folder (or at the repository root if not specified).

If you don’t specify a summary and GitBook doesn’t find `SUMMARY.md` at the root of your docs, it will infer the table of contents from the folder structure and Markdown files.

circle-info

The summary Markdown file **mirrors the table of contents** of your GitBook space. Even when no summary file is provided during the initial import, GitBook will create or update it when you change content in the GitBook editor.

You cannot reference the same Markdown file twice in `SUMMARY.md`, because that would put one page at two different URLs.

#### Table of contents (sidebar) titles

To use a different title in the sidebar than on the page, add an optional **page link title** in `SUMMARY.md`.

With Git Sync, the page link title is set on the page link:

./SUMMARY.md

Copy

```
# Summary

* [Page main title](page.md "Page link title")
```

The text in quotes (`"Page link title"`) is used:

- In the table of contents (sidebar)
- In the pagination buttons at the bottom of each page
- In relative links to that page

Page link titles are optional; if you omit them, GitBook uses the page’s standard title everywhere.

### ​Redirects

Redirects are defined in `.gitbook.yaml`. Paths are relative to the `root` option. Example:

.gitbook.yaml

Copy

```
root: ./

redirects:
  help: support.md
```

circle-info

Redirects in a space’s configuration apply only to that space. For most cases, use [site redirects](https://gitbook.com/docs/publishing-documentation/site-redirects), which apply across the whole site.

circle-exclamation

When a file is moved multiple times in Git, the old file is removed and a new one is created. GitBook may not detect folder renames. Add redirects where needed.

Last updated 2 months ago

Was this helpful?

---

## Page: https://gitbook.com/docs/getting-started/git-sync/enabling-github-sync

### Getting started

In the space you want to sync with GitHub, open the [space header](https://gitbook.com/docs/resources/gitbook-ui#space-header) in the top right and select **Configure**. Choose **GitHub Sync** from the provider list.

![A GitBook screenshot showing GitHub Sync configuration options](https://gitbook.com/docs/~gitbook/image?url=https%3A%2F%2F1050631731-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FNkEGS7hzeqa35sMXQZ4X%252Fuploads%252FSmP9bdDqDK0gOpDYdSdj%252FEnabling%2520GitHub%2520Sync%25402x.png%3Falt%3Dmedia%26token%3Da10a9f24-4f69-4b34-a802-64424aac7f76&width=768&dpr=3&quality=100&sign=53baed17&sv=2)

GitHub Sync configuration options.

### Authenticate with GitHub

If you’re setting up GitHub Sync for the first time and haven’t linked a GitHub account, you’ll be prompted to do so. If you’ve already linked it, you may still need to authenticate via GitHub.

circle-exclamation

If you see a **'Potential duplicated accounts'** error, your GitHub account is already linked to another GitBook user.

To identify which accounts are linked, log out and sign in again using “Sign in with GitHub”.

If you know the GitBook account linked to GitHub, log into that account and unlink GitHub (in settings) before signing back in and linking your current account.

See the [troubleshooting page](https://gitbook.com/docs/getting-started/git-sync/troubleshooting#potential-duplicated-accounts-when-signing-in).

### Install the GitBook app to your GitHub account

If you haven’t already, you’ll be prompted to add the [GitBook app](https://github.com/apps/gitbook-com) to your GitHub account.

Follow the GitHub popover and either grant GitBook access to specific repositories or to all repositories.

### Select a repository and branch

Choose the account and repository to sync with your GitBook space.

circle-info

**Can’t see your repository?** Ensure the [GitBook GitHub app](https://github.com/apps/gitbook-com) is installed for the right scope (personal account or org where the repo lives) and that repository access is configured correctly.

After selecting the repository, choose the branch to push commits to and sync from.

### Perform an initial sync

For the first sync, you can choose:

1. **GitBook -> GitHub** — sync your space’s content **to** the selected branch. Use this when starting from an empty repository.
2. **GitHub -> GitBook** — sync your space’s content **from** the selected branch. Use this when you have existing Markdown in the repository.

### Write and commit

When your space was in [live edit](https://gitbook.com/docs/collaboration/live-edits) mode, live edits are now locked so content can be reliably synced when someone merges a [change request](https://gitbook.com/docs/collaboration/change-requests) in GitBook.

- Edits in GitBook: each merged change request becomes a commit on the selected GitHub branch.
- Commits on GitHub: each commit is synced to your GitBook space as a history commit.

circle-exclamation

The GitHub app that powers this integration is not available for GitHub Enterprise Server.

Last updated 10 hours ago

Was this helpful?

---

## Page: https://gitbook.com/docs/getting-started/git-sync/monorepos

GitBook supports monorepos. A monorepo is a repository with more than one logical project (e.g. an iOS client and a web app).

GitBook can sync multiple directories from the same repository to multiple spaces. When enabling Git Sync on a space, you can set a **Project directory**. GitBook uses it to find the `.gitbook.yaml` for the directory to sync with that space.

Example repository structure:

Copy

```
/
  package.json
  packages/
     styleguide/
        .gitbook.yaml
        README.md
        SUMMARY.md
     app/
        README.md
        SUMMARY.md
     api/
        .gitbook.yaml
        README.md
        SUMMARY.md
```

In this example, you can create 3 GitBook spaces with different Project directories:

- `packages/styleguide`
- `packages/app`
- `packages/api`

The **Project directory** in Git Sync is different from the [`root` option](https://gitbook.com/docs/getting-started/git-sync/content-configuration#root) in `.gitbook.yaml`. The Project directory is used to find `.gitbook.yaml`; both are then used to locate the rest of the files. If there is no `.gitbook.yaml` in the Project directory, GitBook uses the default configuration scoped to that directory.

## Updating the Project directory

circle-info

Recommended steps to update the Project directory:

1. Disable the existing Git Sync
2. Move the files in the Git repository to the new Project directory
3. Reconfigure Git Sync with the new Project directory

You might start with a single space syncing to one directory and later move to a monorepo with multiple spaces, or rename the Project directory.

Changing the Project directory on an existing Git Sync can affect content; changes are applied on the next sync (edit in GitBook or new commit in the repository).

#### **If the next operation is an import from the Git repository**

GitBook expects pages and files in the Project directory. If they haven’t been moved there, the sync can result in an empty space.

Recommended: have the next operation be a commit that moves all GitBook-related files (Markdown, README/SUMMARY, assets) into the new Project directory.

#### **If the next operation is an export from GitBook to the Git repository**

GitBook will create or update files in the new Project directory. Previously synced files will be moved there (best effort); this can affect other parts of your system that depend on those paths.

Last updated 3 months ago

Was this helpful?

---

## Page: https://gitbook.com/docs/getting-started/git-sync/troubleshooting

## I have a GitHub sync error

### Be sure to only create readme files in your repo

With Git Sync enabled, do not create readme files in the GitBook UI. Doing so:

- Creates duplicate README files in your repository
- Causes rendering conflicts between GitBook and GitHub
- May break builds and deployment
- Leads to unpredictable file precedence

This applies to files named README.md, readme.md, Readme.md, and README (without extension). Manage the README only in your Git repository.

### Still facing errors?

Check that:

- Your repository has a `README.md` at its root (or at the `root` folder in `.gitbook.yaml`) that was created in the Git repository. This file is required and is used as the docs homepage. See [content configuration](https://gitbook.com/docs/getting-started/git-sync/content-configuration).
- If you use YAML frontmatter in Markdown files, validate it with a [linter](http://www.yamllint.com/).

## ​GitBook is not using my `docs` folder

By default, GitBook uses the repository root. You can specify a different directory in the [content configuration](https://gitbook.com/docs/getting-started/git-sync/content-configuration).

## GitBook is creating new markdown files

When syncing and editing from GitBook with an existing Git repository, GitBook may create new Markdown files instead of reusing existing ones to avoid overwriting files that were already in the repository.

## Redirects aren't working correctly

The YAML file must be correctly formatted for redirects to work. Incorrect indentation or whitespace can break them. [Validating your YAML file](https://www.yamllint.com/) can help.

Do not add leading slashes to redirect paths. For example, redirecting to `./misc/support.md` will not work.

GitBook only looks for redirects when no page exists for a path. If you redirect an old page to a new one, remove the old page for the redirect to apply.

## ​My repository is not listed

### For GitHub repositories

Ensure the GitBook GitHub app is installed for the correct scope (personal account or org) and that it has access to the right repositories.

### For GitLab repositories

Ensure your access token has:

- `api`
- `read_repository`
- `write_repository`

## ​Nothing happens on GitBook after adding a new file to my repository

circle-exclamation

**This section applies when a `SUMMARY.md` file already exists.**

If your repository has no `SUMMARY.md`, GitBook creates one on the first sync. If you’ve edited content in GitBook at least once after enabling Git Sync, GitBook should have created it.

If you add or change a Markdown file in the repository and don’t see updates in GitBook (and the sidebar shows no sync error), the modified file is likely not listed in [your `SUMMARY.md` file](https://gitbook.com/docs/getting-started/git-sync/content-configuration#summary).

This can happen if you created the file manually or if GitBook created it during a Git export.

`SUMMARY.md` mirrors your [table of contents](https://gitbook.com/docs/resources/gitbook-ui#table-of-contents) and is used during the Git → GitBook sync to rebuild the TOC and reconcile updates.

If all files are in `SUMMARY.md` and you still don’t see updates, [contact support](https://gitbook.com/docs/help-center/further-help/how-do-i-contact-support).

## GitHub preview is not showing

If GitHub preview is missing, your Git Sync may have been configured before January 2022. Older setups may not include GitHub Preview.

You should have received a notification to accept updated permissions for read-only access to PRs.

If not, update the integration:

1. Uninstall the GitSync integration from your organization.
2. Reinstall the new version with the updated permissions.

Uninstalling will require reconfiguring the integration on any spaces it was connected to.

## Potential duplicated accounts when signing in

This usually happens when the GitHub account used for sync is already linked to a different GitBook user.

To identify the linked GitBook account:

1. Log out of your current GitBook session (e.g. `name@email.com`)
2. Log out of any GitHub session
3. Go to [the Log in page](https://app.gitbook.com/login)
4. Choose “Sign in with GitHub”
5. Enter your GitHub credentials
6. After logging in, go to [account settings](https://app.gitbook.com/account) and either:
   - Unlink GitHub under “Third-party Login > GitHub” in Personal settings
   - Delete the account if you don’t need it
7. Log out
8. Log back in with your `name@email.com` GitBook account
9. Set up Git Sync again

Last updated 8 months ago

Was this helpful?

---

## Page: https://gitbook.com/docs/getting-started/git-sync/commits

By default, when exporting content from GitBook to Git, GitBook generates a commit message from the merged change request:

Copy

```
GITBOOK-14: Improve documentation about users management
```

## Autolink `GITBOOK-<num>` in GitHub and GitLab

To turn GitBook change request IDs (e.g. _GITBOOK-123_) into links in commits, use GitHub’s _Autolink references_ feature. See [GitHub instructions](https://help.github.com/en/github/administering-a-repository/configuring-autolinks-to-reference-external-resources).

Use this URL format, where `spaceId` is your space’s URL:

`<https://app.gitbook.com/s/{spaceId}/~/changes/<num>/`

![A GitBook screenshot showing autolink setup](https://gitbook.com/docs/~gitbook/image?url=https%3A%2F%2F1050631731-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FNkEGS7hzeqa35sMXQZ4X%252Fuploads%252FXMOX8gtwZIZGwdSWhSdX%252Fgitsync-autolink%25402x.png%3Falt%3Dmedia%26token%3Dbebbbb78-1a5f-4e90-af21-29803b3d2a7a&width=768&dpr=3&quality=100&sign=d9a10dde&sv=2)

Autolink setup.

## Customize the commit message template

For [monorepos](https://gitbook.com/docs/getting-started/git-sync/monorepos) or specific commit message rules, you can customize the message GitBook uses when pushing to Git.

The template supports these placeholders:

- `{change_request_number}` — numeric ID of the change request
- `{change_request_subject}` — subject of the merged change request, or `No subject` if none

Default template:

Copy

```
GITBOOK-{change_request_number}: {change_request_subject}
```

Last updated 2 months ago

Was this helpful?

---

## Page: https://gitbook.com/docs/creating-content/formatting/markdown

![An image containing the markdown logo](https://gitbook.com/docs/~gitbook/image?url=https%3A%2F%2F1050631731-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FNkEGS7hzeqa35sMXQZ4X%252Fuploads%252FMbo91kXRJGPsIzXxsgpU%252Fmarkdown%25402x.png%3Falt%3Dmedia%26token%3D9d812c93-81df-4bca-a053-baa88d83f572&width=768&dpr=3&quality=100&sign=84ab0b4e&sv=2)

Write Markdown in GitBook.

GitBook’s editor lets you create formatted content with Markdown.

Markdown is a simple markup syntax. GitBook supports it as a keyboard-friendly way to write rich, structured text.

circle-info

Learn more about Markdown at [Common Mark](https://commonmark.org/help/).

### Text formatting

GitBook supports standard inline Markdown formatting:

| Formatting   | Markdown version | Result        |
|-------------|------------------|---------------|
| Bold        | `**bold**`       | **bold**      |
| Italic      | `_italic_`       | _italic_      |
| Strikethrough | `~strikethrough~` | ~~strikethrough~~ |
| Inline code | `` `code` ``     | `code`        |

### Pasting Markdown

When pasting Markdown into the editor, use **Paste and Match Style** (`Shift` + `Cmd` + `V` on Mac or `Shift` + `Ctrl` + `V` on Windows).

Using normal Paste for content from another editor or the web may insert it as a code block instead of formatted text.

### Titles

- Heading 1: `# A first-level title`
- Heading 2: `## A second-level title`
- Heading 3: `### A third-level title`

### Code blocks

``````⏎``` creates a new code block.

``````py⏎``` creates a code block with Python syntax highlighting.

circle-info

GitBook uses [Prism](https://github.com/PrismJS/prism) for syntax highlighting. Use [Test Drive Prism](https://prismjs.com/test.html#language=markup) to see supported languages. If GitBook and Prism differ, GitBook may be a version or two behind.

### Lists

GitBook detects and creates ordered and unordered lists as you type.

- Start a line with `-` or `*` for an unordered list
- Start a line with `1.` for a numbered list
- Start a line with `- [ ]` for a task list

circle-info

In lists, use `Tab` to indent and `Shift+Tab` to outdent.

### Quotes

Start a line with `>` for a block quote. Selecting a full paragraph and typing `>` wraps it in a block quote.

> This is a block quote.

### Dividers

Type `---` and press `Enter` to create a divider.

* * *

This is an example of a divider.

Last updated 1 month ago

Was this helpful?

---

## Page: https://gitbook.com/docs/creating-content/formatting/inline

![A GitBook screenshot showing inline content options](https://gitbook.com/docs/~gitbook/image?url=https%3A%2F%2F1050631731-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FNkEGS7hzeqa35sMXQZ4X%252Fuploads%252FQcBDNerKxNvi1X3Jnk2R%252F26_01_22_inline-palette%25402x.png%3Falt%3Dmedia%26token%3D08b0298b-627f-4394-addf-dd5b49cf3501&width=768&dpr=3&quality=100&sign=90e027b6&sv=2)

Add inline elements to your content.

The inline palette lets you add extra content to a text block without leaving the keyboard. Press `/` on any text block to open it. The `/` is replaced by the content you insert.

### Annotations

Annotations add context without interrupting the reader. Use them to explain terms, add extra information, etc. Readers hover over the annotated text to see the annotation.

#### Create an annotation

Select the text, then choose **Annotate** in the context menu. Write the annotation and click outside to continue editing.

#### Markdown representation

You can add annotations using [Markdown footnotes](https://www.markdownguide.org/extended-syntax/#footnotes). Footnote markers should come right after the word, not after punctuation.

Copy

```
Here's a simple footnote[^1], and here's a longer one[^bignote].

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.
```

### Images

Inline images sit alongside text.

By default, images use their original size with a max width of 300px. Click the image to open the formatting palette and choose:

1. **Inline size:** Sized to the font — good for icons and badges
2. **Original size:** Inline at original size, max 300px
3. **Convert to block:** Turn the inline image into an [image block](https://gitbook.com/docs/creating-content/blocks/insert-images), full content width

circle-info

[Image blocks](https://gitbook.com/docs/creating-content/blocks/insert-images) support more sizes and captions but are not inline with text.

#### Representation in Markdown

Copy

```
Here is an inline image: <img src=".gitbook/assets/GitBook - Dark.jpg" alt="Dark version of GitBook logo" data-size="line">
```

### Emojis

Add emojis by pressing `/` and choosing from the inline palette, or type `:` and pick from the list. Typing after `:` filters emojis.

#### Representation in Markdown

Copy

```
:house:
:car:
:dog:
```

### Links

You can add:

- [Relative links](https://gitbook.com/docs/creating-content/formatting/inline#relative-links)
- [Absolute links](https://gitbook.com/docs/creating-content/formatting/inline#absolute-links)
- [Email address `mailto` links](https://gitbook.com/docs/creating-content/formatting/inline#email-address-mailto-links)

#### Relative links

Relative links point to [pages](https://gitbook.com/docs/creating-content/content-structure/page) in your space. If the page URL, name, or location changes, the link stays valid.

To add a relative link:

1. Click where you want the link or select text
2. Press `/` and choose Link, use the **Link** button in the context menu, or press **⌘ + K**
3. Type the page title
4. Select the page from the results
5. Press `Enter`

#### Absolute links

Absolute links are external URLs you paste into your content.

To add an absolute link:

1. Click where you want the link or select text
2. Press `/` and choose Link, use the **Link** button, or press **⌘ + K**
3. Paste the URL
4. Press `Enter`

circle-info

**Why don't external links open in a new tab?**

External links open in the same tab. GitBook follows [W3C-recommended behavior](https://www.w3.org/TR/WCAG20-TECHS/G200.html) for [accessibility](https://it.wisc.edu/learn/make-it-accessible/websites-and-web-applications/when-to-open-links-in-a-new-tab/).

#### Email address mailto links

`mailto` links open the default email client with the address filled in.

To add a mailto link:

1. Click where you want the link or select text
2. Press `/` and choose Link, use the **Link** button, or press **⌘ + K**
3. Type or paste `mailto:something@address.com`
4. Press `Enter`

#### Representation in Markdown

Copy

```
[This is a relative link to another page in this space](../content-structure/page.md)
[This is an absolute link](https://www.gitbook.com/blog)
[This is a link](mailto:support@gitbook.com) to our support email address
```

### Math & TeX

You can add inline math formulas (e.g. f(x)=x∗e2piiξx). GitBook uses the [KaTeX](https://katex.org/docs/supported.html) library.

circle-info

You can also add [a block-level math formula](https://gitbook.com/docs/creating-content/blocks/math-and-tex) from the command palette in an empty block.

#### Representation in Markdown

Copy

```
# Math and TeX block

$$f(x) = x * e^{2 pi i \xi x}$$
```

### Buttons

Buttons describe calls to action. They can link to other GitBook pages or external URLs.

Buttons can be primary or secondary.

#### Representation in Markdown

Copy

```
<a href="https://app.gitbook.com" class="button primary">GitBook</a>
```

### Icons

Icons add visual cues. You can use them inline, in cards, or elsewhere. They follow your [customization settings](https://gitbook.com/docs/publishing-documentation/customization/icons-colors-and-themes).

facebookgithubx-twitterinstagram

See [Font Awesome](https://fontawesome.com/) for available icons.

#### Representation in Markdown

Copy

```
<i class="fa-github">:github:</i>
```

### Expressions

Expressions show content from a [variable](https://gitbook.com/docs/creating-content/variables-and-expressions). Insert them from the `/` menu. Click an expression to open the editor and reference or [conditionally format](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator) your variable.

Last updated 11 days ago

Was this helpful?

---

## Page: https://gitbook.com/docs/creating-content/formatting

Format text by selecting it and choosing a format from the context menu, or by using keyboard shortcuts or Markdown syntax.

circle-info

Shortcuts are written for Mac. Use **Control** instead of **⌘ (Command)** on Windows or Linux. See [keyboard shortcuts](https://gitbook.com/docs/resources/keyboard-shortcuts) for all shortcuts.

### Bold

Keyboard shortcut: `⌘` + `B`

Markdown

Copy

```
**Bold**
```

### Italic

Keyboard shortcut: `⌘` + `I`

Markdown

Copy

```
_Italic_
```

### Strikethrough

Keyboard shortcut: `⇧` + `⌘` + `S`

Markdown

Copy

```
~~Strikethrough~~
```

### Code

Keyboard shortcut: `⌘` + `E`

Markdown

Copy

```
`Code`
```

### Link

Keyboard shortcut: `⌘` + `K`

When adding a link, you’ll be prompted for the URL. You can use any URL; for pages or sections in your space, prefer [relative links](https://gitbook.com/docs/creating-content/formatting/inline#relative-links).

This is [a link to an external page](https://www.gitbook.com/).

This is a [link to another page in this space](https://gitbook.com/docs/creating-content/blocks).

This is [a link to a section on this page](https://gitbook.com/docs/creating-content/formatting#code).

This is [a link that starts an email to a specific address](mailto:support@gitbook.com).

### Color and background color

Use the color icon in the context menu to set text or background color.

This text is orange.

This text background is orange.

Last updated 6 months ago

Was this helpful?