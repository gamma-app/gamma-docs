Here is the concatenated content from all 12 GitBook documentation pages:

---

## Page: https://gitbook.com/docs/creating-content/blocks/heading

Headings help give your documents structure — and using keywords in headings will also help search engines understand that structure, which can help your page rank higher in search results.

GitBook offers three levels of headings. Heading levels 1 (H1) and 2 (H2) will appear in the [page outline](https://gitbook.com/docs/resources/gitbook-ui#page-outline).

### Anchor links

When you add a heading to a page, it creates an anchor link. You can then link directly to these specific sections, to point people to relevant information.

#### Link to an anchor

You can see anchor links in public content, or private content in read-only mode, by hovering over the title and clicking the `#` that appears next to it. This will update the URL in your browser's top bar, so you can copy it to use elsewhere.

If you want to link to a particular anchor from a page within your GitBook space, you can use a [relative link](https://gitbook.com/docs/creating-content/formatting/inline#relative-links), which will update if you change the heading to prevent the link from breaking.

#### Edit an anchor

By default, the anchor link will be identical to the text in your header. If you plan to link to that URL outside of GitBook, changing the header in future will break the anchor link. The link will then take visitors to the top of the page, rather than the anchor location.

To avoid this, you can manually set the anchor link by opening the **Options menu** for the header, then choosing **Edit anchor**. You can then enter the anchor link you wish to use — this will remain the anchor even if you change the header itself.

### Representation in Markdown

GitBook generates SEO optimized pages, meaning page titles in GitBook are automatically represented in markdown as a first level heading:

```
# I'm a page title
```

This means that if you [sync your content with Git](https://gitbook.com/docs/getting-started/git-sync), page headers added through the editor will be represented as one level lower:

```
## My heading 1
### My heading 2
#### My heading 3
```

### Heading examples

## My heading 1

### My heading 2

#### My heading 3

---

## Page: https://gitbook.com/docs/creating-content/blocks/table

You can add tables to better organize your information in a GitBook page.

### Table block options

When you open the Options menu to the left of a table block, you’ll have a number of options to change the appearance and manage the data inside the table:

- **Table/Cards:** Choose to display your data as either a table block or [a cards block](https://gitbook.com/docs/creating-content/blocks/cards). GitBook populates both these blocks using the same data, so you can switch between them depending on the look and design you want.
- **Add column:** Add a new column to the right of your table. You can choose column type using the menu, or just click **Add column** to add a text column.
- **Insert row:** Add a new row to the bottom of your table.
- **Show header:** Hide or show the top title row of your table. Depending on the data you're displaying, you may not need a title row in your table, so you can disable it here.
- **Reset column sizing:** If you've changed the column widths, this will reset them all to be equal again.
- **Visible columns:** Choose which columns are visible and which are hidden. If you have hidden columns in your table, this menu is where you can make them visible again.
- **Full width:** Make your table span the full width of your window. This is great for tables with lots of columns.
- **Delete:** Deletes the table block and all of its content.

### Changing a column type

Depending on the data you want to display, you can set table columns to different data types. These add formatting, embellishments or restrictions to every cell in the column:

- **Text:** A standard text column, with standard formatting support.
- **Number:** A number column, with or without floating digits.
- **Checkbox:** A checkbox on each line that can be checked or unchecked.
- **Select:** You can select data from a list of options that you can define by opening the **Columns options** menu and choosing **Manage options**. This can be single-choice or multiple-choice.
- **Users:** You can add the name and avatar of a member of your organization. This can be single-choice or multiple-choice.
- **Files:** You can reference a file in the space. You can upload new files when populating cells in the column.
- **Rating:** A star rating. You can configure the maximum rating by opening the **Column options** menu and choosing **Max**.

Use the **Column options** menu to change a column's type. When you change a column type, you'll see a prompt asking you to confirm the change, as column data could be deleted or broken by this action.

### Resizing columns

Hover over a column's edge and drag to resize it. A pixel count appears above the cursor to help you set consistent column sizes.

GitBook stores column sizes as a percentage of the overall width, which allows for relative sizing based on the overall width of the table.

### Scrolling tables

Tables that are wider than the editor container will be horizontally scrollable.

### Column options

To reorder columns, click and drag on the drag handle at the top of the column you want to move.

You can add new columns by clicking the **Add column** button that appears when you hover over the right edge of the table.

Inside the **Column options** menu you can also switch automatic sizing on and off, add a new column to the right, hide the column, or delete the column.

### Row options

Hover over the row and click the **Row options** button that appears on the left of it to open the **Row options** menu. You'll see a number of options:

- **Open row:** Open the row in a modal that shows all of its data. Here you can quickly change row types, edit data, and see data in hidden columns.
- **Insert above/below:** Add a new row above or below the currently-selected row.
- **Add column:** Add a new column on the right of the table.
- **Delete row:** Permanently remove all the data in the row from your table.

### Images in tables

When you click into a table cell, you can hit the / key to insert images. Images cannot be added to the header row of a table.

### Representation in Markdown

```
# Table

|   |   |   |
| - | - | - |
|   |   |   |
|   |   |   |
|   |   |   |
```

**Note:** It's not possible to nest tables in GitBook. To ensure documents remain easy to write, reliable to render, and accessible for all users, GitBook keeps tables flat.

---

## Page: https://gitbook.com/docs/creating-content/blocks/insert-images

You can insert images into your page, then choose their size and whether to align them to the left, center, or right. You can also optionally include alt text and/or a caption on your image block.

**Tip:** For accessibility purposes, we recommend setting alt text for your images.

### Example of an image block

Example of an image block with a caption

### Uploading an image

There are two ways to add images to your content:

1. Drag and drop the image from your file management system directly into an empty block on your page.
2. [Add an image block](https://gitbook.com/docs/creating-content/blocks#inserting-a-new-content-block) to your page and use the **Select images** side panel that appears on the right of the window.

If you follow the second process, you can choose to upload a file, select a previously-uploaded file, paste an image URL or add an image from [Unsplash](https://unsplash.com/) using the built-in search.

**Note:** GitBook allows you to upload images up to 100MB per file.

#### Create an image gallery

Adding more than one image to an image block will create a gallery. To do this, open the block's **Options menu** and choose **Add images…** to open the **Select images** side panel again.

To delete an image from a gallery, open the **Edit menu** on the image you want to delete and press the **Delete ⌫** key.

### Adding images for light & dark mode

You can set different images for the light and dark mode versions of your published site. GitBook will automatically display the correct image depending on the mode your visitor is in.

To add an image for dark mode, hover over your image, open the **Edit menu** and click **Replace image**. In the drop-down menu, choose **Add image for Dark mode**. Once you've set this, you can replace either image from this same menu.

**Note:** GitBook doesn't currently support light and dark mode images for certain cases, including page covers or image covers on [cards](https://gitbook.com/docs/creating-content/blocks/cards).

### Light and dark mode images through GitHub/GitLab Sync

You can also add light and dark mode images in Markdown through HTML syntax (`<picture>` and `<source>`).

For block images, use the `<figure>` HTML element with a `<picture>` and `<source>` in it:

```
Text before

<figure>
  <picture>
    <source
      srcset="
        https://user-images.githubusercontent.com/3369400/139447912-e0f43f33-6d9f-45f8-be46-2df5bbc91289.png
      "
      media="(prefers-color-scheme: dark)"
    />
    <img
      src="https://user-images.githubusercontent.com/3369400/139448065-39a229ba-4b06-434b-bc67-616e2ed80c8f.png"
      alt="GitHub logo"
    />
  </picture>
  <figcaption>Caption text</figcaption>
</figure>

Text after
```

For inline images (images that sit inline with text), use the `<picture>` HTML element with a `<source>` in it:

```
Text before the image
<picture
  ><source
    srcset="
      https://user-images.githubusercontent.com/3369400/139447912-e0f43f33-6d9f-45f8-be46-2df5bbc91289.png
    "
    media="(prefers-color-scheme: dark)" />
  <img
    src="https://user-images.githubusercontent.com/3369400/139448065-39a229ba-4b06-434b-bc67-616e2ed80c8f.png"
    alt="The GitHub Logo"
/></picture>
and text after the image
```

**Note:** We don't yet support [GitHub-only syntax](https://github.blog/changelog/2021-11-24-specify-theme-context-for-images-in-markdown/) through `#gh-dark-mode-only` or `#gh-light-mode-only`.

### Resizing

To resize your image, hover over it and open the **Edit menu**. Click the **Size** button to change the size of your image from the available options.

- **Small** – 25% of the image size
- **Medium** – 50% of the image size
- **Large** – 75% of the image size
- **Fit** – Removes all size specifications and displays either at full size or capped at a maximum width of **735 pixels** for larger images.

If your image is wider than the editor, GitBook will limit the image's width to the editor's width instead, and resizing will be based on this limit.

**Note:** When resizing images in an image gallery, the results can differ from resizing an individual image.

You can make image blocks [span the full width of your window](https://gitbook.com/docs/creating-content/blocks#full-width-blocks) by clicking on the **Options menu** next to the block and choosing **Full width**.

### Resizing images through Git Sync

If you want more control over the sizing of your image, you can specify the exact size using Markdown in GitHub or GitLab.

When we export an image, we use the HTML tag `<img/>`. As per the specifications, we can specify the dimensions of the image using the `width` and `height` attributes, which only accept values in pixels or a combination of a number and a `%` sign.

Valid variants for specifying the image dimensions are:

`<img width="100" />` Sets the image to 100 pixels wide  
`<img width="100%" />` Sets the image to full size (although this will be limited by the editor)

### Aligning images

By default, image blocks will show your image at its full size, aligned centrally.

To change the alignment of an image, open the block's **Options menu** and choose the alignment you want. This will only affect images that are narrower than the editor, or images you've [resized](https://gitbook.com/docs/creating-content/blocks/insert-images#resizing).

### Framing images

You can add a frame to image blocks to give your images a consistent look and visually separate them from their surrounding content.

Framed images can have captions, and show a subtle grid behind the caption.

To add a frame to an image, hover over it, open the block's **Options menu** and enable the **With frame** toggle.

**Good to know:** You can only frame single images in a block. Image blocks that contain multiple images and inline images cannot have frames.

### Representation in Markdown

```
//Simple Block
![](https://gitbook.com/images/gitbook.png)

//Block with Caption
![The GitBook Logo](https://gitbook.com/images/gitbook.png)

//Block with Alt text
<figure><img src="https://gitbook.com/images/gitbook.png" alt="The GitBook Logo"></figure>

//Block with Caption and Alt text
<figure><img src="https://gitbook.com/images/gitbook.png" alt="The GitBook Logo"><figcaption><p>GitBook Logo</p></figcaption></figure>

// Block with framed image
<div data-with-frame="true"><img src="https://gitbook.com/images/gitbook.png" alt="The GitBook Logo"></div>

//Block with different image for dark and light mode, with caption
<figure>
  <picture>
    <source srcset="https://user-images.githubusercontent.com/3369400/139447912-e0f43f33-6d9f-45f8-be46-2df5bbc91289.png" media="(prefers-color-scheme: dark)">
    <img src="https://user-images.githubusercontent.com/3369400/139448065-39a229ba-4b06-434b-bc67-616e2ed80c8f.png" alt="GitHub logo">
  </picture>
  <figcaption>Caption text</figcaption>
</figure>
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/hint

Hints, or callouts, are a great way to bring the reader's attention to specific elements in your documentation, such as tips, warnings, and other important information.

There are four different hint styles — you can change the style by opening the block's **Options menu** and selecting the style you want. Each style uses a default icon, but you can customize the icon by clicking on it and choosing another one from [our icons set](https://gitbook.com/docs/creating-content/formatting/inline#icons).

Hint blocks support [inline content](https://gitbook.com/docs/creating-content/formatting/inline) and [formatting](https://gitbook.com/docs/creating-content/formatting), as well some specific block types. To see which block types you can use in a hint, hit `/` on an empty line and check the [insert palette](https://gitbook.com/docs/creating-content/blocks#inserting-a-new-content-block).

### Examples of hint blocks

**Info hints** are great for showing general information, or providing tips and tricks.

**Success hints** are good for showing positive actions or achievements.

**Warning hints** are good for showing important information or non-critical warnings.

**Danger hints** are good for highlighting destructive actions or raising attention to critical information.

This hint block has a custom icon.

To add a heading to your hint, you need to create a heading block as the first block in the hint.

### Representation in Markdown

```
{% hint style="info" %}
**Info hints** are great for showing general information, or providing tips and tricks.
{% endhint %}

{% hint style="success" %}
**Success hints** are good for showing positive actions or achievements.
{% endhint %}

{% hint style="warning" %}
**Warning hints** are good for showing important information or non-critical warnings.
{% endhint %}

{% hint style="danger" %}
**Danger hints** are good for highlighting destructive actions or raising attention to critical information.
{% endhint %}

{% hint style="info" %}
{% hint style="info" icon="books" %}
This hint block has a custom icon.
{% endhint %}

## This is a H2 heading

This is a line

This is an inline ![The Apple computer command icon](...) image

- This is a second line using an unordered list and color
{% endhint %}
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/code-block

You can add code to your GitBook pages using code blocks.

When you add a code block, you can choose to [set the syntax](https://gitbook.com/docs/creating-content/blocks/code-block#set-syntax...), [show line numbers](https://gitbook.com/docs/creating-content/blocks/code-block#with-line-numbers), [show a caption](https://gitbook.com/docs/creating-content/blocks/code-block#with-caption), and [wrap the lines](https://gitbook.com/docs/creating-content/blocks/code-block#wrap-code). It's also easy to [copy the contents of a code block to the clipboard](https://gitbook.com/docs/creating-content/blocks/code-block#copying-the-code), so you can use it elsewhere.

A code block may be useful for:

- Sharing configurations
- Adding code snippets
- Sharing code files
- Showing usage examples of command line utilities
- Showing how to call API endpoints
- And much more!

### Example of a code block

index.js

```
import * as React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, window.document.getElementById('root'));
```

You can also combine code blocks with a [tabs block](https://gitbook.com/docs/creating-content/blocks/tabs) to offer the same code example in multiple different languages.

### Code block options

When you click on the **Options menu** next to the code block, or the **Actions menu** in the block itself, you'll see a number of options you can set.

#### Set syntax…

You can set the syntax in your code block to any of the supported languages. This will enable syntax highlighting in that language, too.

**Note:** We use [Prism](https://github.com/PrismJS/prism) for syntax highlighting. You can use [Test Drive Prism](https://prismjs.com/test.html#language=markup) to check which languages Prism supports.

#### With line numbers

This will toggle line numbers for your code on and off.

Showing line numbers is useful when the code represents the contents of a file as a whole, or when you have long code blocks with lots of lines. Hiding line numbers is useful for snippets, usage instructions for command line or terminal expressions and similar scenarios.

#### With caption

This will toggle a caption that sits at the top of the block, above your lines of code.

The caption is often the name of a file as shown in [our example above](https://gitbook.com/docs/creating-content/blocks/code-block#example-of-a-code-block), but you can also use it as a title, description, or anything else you'd like.

#### Wrap code

This will toggle code wrapping on and off, so long lines of code will wrap to all be visible on the page at once.

Wrapping lines is useful when your code is long and you want to avoid having the viewer scroll back and forth to read it. If you toggle **Wrap code** on, you may also want to show line numbers — this will make it easier to read the code and understand where new lines start.

#### Expandable

This will toggle showing the code in full (when the toggle is off) or a collapsed window of the code which the user can expand (when the toggle is on).

The collapsed view defaults to showing 10 lines of code with a button to expand to show the full code block. If there are less than 10 lines of code, all the content will be shown.

### Code block actions

As well as the options above, you can also change the language the code block displays, and copy your code instantly.

#### Copy the code

Hover over a code block and a number of icons will appear. Click the middle icon to copy the contents of the code block to your clipboard.

**Note:** You can make code blocks [span the full width of your window](https://gitbook.com/docs/creating-content/blocks#full-width-blocks) by clicking on the **Options menu** next to the block and choosing **Full width**.

### Representation in Markdown

````
{% code title="index.js" overflow="wrap" lineNumbers="true" %}

```javascript
import * as React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, window.document.getElementById('root'));
```

{% endcode %}
````

---

## Page: https://gitbook.com/docs/creating-content/blocks/embed-a-url

To add an embedded URL, simply paste the link of the content you want to embed and hit `Enter`.

**Note:** The content you want to embed must be publicly available in order for GitBook to access the file. For example, when embedding a Google doc the share settings must be set to _Anyone with the link_.

### Videos

Embedded videos (e.g., YouTube, Vimeo) are supported.

**Note:** You can choose to auto-play and loop YouTube and Vimeo embeds by adding `?autoplay=1&loop=1` to the end of your video's URL.

### Codepen

CodePen embeds are supported.

### Spotify

Spotify embeds are supported.

### Representation in Markdown

```
{% embed url="URL_HERE" %}
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/insert-files

You can upload files to your GitBook space and add them to your page for people to view or download.

You can show some files, such as images and OpenAPI files, on the page itself for people to see without clicking anything. For others, such as PDFs, users will have to click to view or download it.

You can also optionally add a caption below any file you insert into your page to add more information if needed.

### Example of a file

Example file block with caption, PDF icon, file size, download link.

### Uploading a file

You can manage uploaded files in the Files side panel of your space. You can find the Files panel at the top of your space's table of contents.

To upload a file, drag and drop it into the **Drop your file or browse** section, or select it and use your system file dialog to select the file you want to upload.

**Note:** GitBook allows you to upload files up to 100MB per file.

You can also add files to your space when you add an [image block](https://gitbook.com/docs/creating-content/blocks/insert-images) or an [OpenAPI block](https://gitbook.com/docs/api-references/openapi). When you create one of these blocks, the Files panel will open, so you can either select a file, or upload a new file.

**Tip:** You can also drag and drop images from your file system directly into the editor — or paste a copied image into your content. GitBook will automatically add them to the Files side panel for the respective space, so you can view and manage them later.

### Renaming a file

To rename a file, open the **Actions menu** for the file, and click **Edit**. In the dialog prompt, enter the new name of your file.

### Deleting a file

To delete a file, open the **Actions menu** for the file and click **Delete**. After confirming in the dialog that you're sure you want to delete the file, your file will be deleted.

**Note:** Make sure you update any pages that included your deleted file! File blocks that reference a deleted file will show an empty block, or _Could not load image_ error.

### Replacing a file

If you have a file that simply needs updating to a new version, you can replace it. This will swap out the old file and put the new file in its place. Any blocks that previously referred to the old file will then refer to the new file.

To replace a file, open the **Actions menu** for the file and click **Replace**. In the file replacement dialog that appears, select the new file and wait for the upload indicator to complete. Your file will automatically update everywhere it appeared in your space.

**Tip:** Once you've uploaded an image or a file, you can reference it anywhere in your space by creating an image or a file block and selecting it from the **Files** side panel. We recommend you do this rather than uploading the image again every time you want to include it, to make it easier to replace images later and to avoid having multiple files with the same name.

### Representation in Markdown

```
{% file src="https://example.com/example.pdf" %}
    This is a caption for the example file.
{% endfile %}
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/tabs

A tab block is a single block with the option to add multiple tabs.

Each tab can contain multiple other blocks, of any type. So you can add code blocks, images, integration blocks and more to individual tabs in the same tab block.

### Add or delete tabs

To add a new tab to a tab block, hover over the edge of a tab and click the `+` button that appears. To delete a tab, open the tab's **Options menu** then select **Delete**.

### Example

Here is an example that lists instructions relevant to specific platforms:

**Windows:** Here are the instructions for Windows  
**macOS:** Here are the instructions for macOS  
**Linux:** Here are the instructions for Linux

### Representation in Markdown

```
{% tabs %}

{% tab title="Windows" %} Here are the instructions for Windows {% endtab %}

{% tab title="OSX" %} Here are the instructions for macOS {% endtab %}

{% tab title="Linux" %} Here are the instructions for Linux {% endtab %}

{% endtabs %}
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/stepper

Stepper blocks let you break down a tutorial or guide into separate, but clearly linked steps. Each step can contain multiple different blocks, allowing you to add detailed information.

### Example

1. **Add a stepper block** – To add a stepper block, hit `/` on an empty line or click the `+` on the left of the editor and select **Stepper** from the insert menu.
2. **Add some content** – Once you've inserted your stepper block, you can start adding content to it — including code blocks, drawings, images and much more.
3. **Add more steps** – Click the `+` below the step numbers or hit `Enter` twice to add another step to your stepper block. You can remove or change the style of the step header or step body if you wish.

### Representation in Markdown

```
## Example

{% stepper %}
{% step %}
### Step 1 title
Step 1 text
{% endstep %}
{% step %}
### Step 2 title
Step 2 text
{% endstep %}
{% endstepper %}
```

### Limitations

There are some limitations on which blocks you can create inside of a stepper block — for example, you cannot add expandable blocks or another stepper block. See all the blocks you can add by starting a new line within a stepper block and pressing `/` to bring up the insert palette.

---

## Page: https://gitbook.com/docs/creating-content/blocks/expandable

Expandable blocks are helpful in condensing what could otherwise be a lengthy paragraph. They are also great in step-by-step guides and FAQs.

By default, expandable blocks will be collapsed on your published docs site. If you want an expandable block to be expanded by default, open the block's **Options menu** and choose **Expanded by default**.

### Example

**Step 1: Start using expandable blocks** – To add an expandable block hit `/` on an empty block, or click the `+` on the left of the editor, and select **Expandable**.
Optionally, you can set expanded blocks to be **Expanded by default** in the block's **Options menu** — just like this block.

**Step 2: Add content to your block** – Once you've inserted an expandable block, you can add content to it — including lists and code blocks.

### Representation in Markdown

```
# Expandable blocks

<details open>

<summary>Add your expandable title here</summary>

Add your expandable body text here. This expandable is expanded by default.

</details>

<details>

<summary>Add your expandable title here</summary>

Add your expandable body text here. This expandable is collapsed by default.

</details>
```

### Limitations

There are some limitations on which blocks you can create inside of an expandable block. You can check the full list by starting a new line in an expandable block and pressing `/` to bring up the insert palette.

---

## Page: https://gitbook.com/docs/creating-content/blocks/cards

You can use cards to create a visually pleasing page layout, combining text and images in a grid. They're ideal for building landing pages or displaying any other content in a non-linear way.

You can adjust [switch between medium or large cards](https://gitbook.com/docs/creating-content/blocks/cards#card-size) and link them to the relevant resources.

### Example of a card

Cards with cover images, titles, and descriptions.

### Adding links

Hover over a card and open its **Options menu**. Here you can add a target link, so users can jump directly to a location when they click the card.

When creating cards, we recommend you use **target links instead of hyperlinks**. With a target link, your readers can click anywhere on the card to access the linked URL.

### Adding images

Hover over a card and open its **Options menu**. Here you can add a cover image to your card. Alternatively, just click the **Add cover image** option on the card itself.

This will open the **Select file** modal. Here you can drag and drop a new image into this, or use an image file you've previously uploaded to your space.

#### Adding images for dark mode

You can also add cover images that will only show in dark mode.

To do this, open the card's **Options menu** and choose **Cover** > **Edit cover** > **Add cover for dark mode**. This will open the **Select file** modal, where you can drag and drop a new image or select a previously-uploaded image.

#### Choosing the right image size

GitBook will automatically crop landscape images to a 16:9 ratio on desktop and mobile. If the images you upload are portrait or have a 1:1 ratio, they will be cropped to 16:9 on desktop and display as square or portrait on mobile.

On desktop, all card images will display in a landscape 16:9 ratio, regardless of their dimensions. We recommend using the same dimensions for consistency.

On mobile, square or portrait images will displayed as shown on the left. Landscape images will be displayed as shown on the right.

To keep things consistent across desktop and mobile, we recommend uploading all the images for your cards in a 16:9 format (e.g. 1920px x 1080px).

If you want your cards to adapt their layout depending on the screen size, we'd recommend uploading images with a 1:1 ratio, and the content of your image centered.

### Changing the size of cards

You can select the card size by opening the **Options menu** to the left of your card block. The **Medium** option creates three cards in one horizontal line, while the **Large** option shows two larger cards on each line.

**Note:** You can make card blocks [span the full width of your window](https://gitbook.com/docs/creating-content/blocks#full-width-blocks) by clicking on the **Options menu** next to the block and choosing **Full width**.

### Representation in Markdown

```
<table data-view="cards">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th data-hidden data-card-target data-type="content-ref"></th>
      <th data-hidden data-card-cover data-type="files"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Example title 1</strong></td>
      <td>Example description 1.</td>
      <td><a href="https://example.com">https://example.com</a></td>
      <td><a href="https://example.com/image1.svg">example_image1.svg</a></td>
    </tr>
    <tr>
      <td><strong>Example title 2</strong></td>
      <td>Example description 2.</td>
      <td><a href="https://example.com">https://example.com</a></td>
      <td><a href="https://example.com/image2.svg">example_image2.svg</a></td>
    </tr>
    <tr>
      <td><strong>Example title 3</strong></td>
      <td>Example description 3.</td>
      <td><a href="https://example.com">https://example.com</a></td>
      <td><a href="https://example.com/image3.svg">example_image3.svg</a></td>
    </tr>
  </tbody>
</table>
```

---

## Page: https://gitbook.com/docs/creating-content/blocks/columns

Columns are a great way to create different layouts for your documentation. You can add many different types of blocks inside a column, and adjust the width of each side to customize it to the design you need.

#### Create a seamless experience between your docs and product

Integrate your documentation right into your product experience, or give users a personalized experience that gives them what they need faster.

[Learn more](https://www.gitbook.com/#alpha-waitlist)

### Representation in Markdown

```
## Example

### Create a seamless experience between your docs and product

Integrate your documentation right into your product experience, or give users a personalized experience that gives them what they need faster.

<a href="https://www.gitbook.com/#alpha-waitlist" class="button primary">Learn more</a>

<figure><img src="../../.gitbook/assets/GitBook vision post.png" alt="An image of GitBook icons demonstrating side by side column functionality"><figcaption></figcaption></figure>
```

---

All 12 pages have been scraped and concatenated above. Content includes markdown representation, Git sync format, options, attributes, data-* properties (e.g. `data-with-frame`, `data-view`, `data-card-target`, `data-card-cover`, `data-hidden`), full-width options, sizing options, and other details from each page.