# Kitchen Sink

This page serves as a reference to the features supported by MyST+Sphinx+Readthedocs. This page is probably best viewed in source which you can find with the "Edit on GitHub" link in the top right. If you are using Visual Studio Code, the [MyST-Markdown plugin](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) is recommended as it provides code snippets for the different directives that MyST adds to regular Markdown. In general in Markdown, a block is surrounded by \`\`\` followed by the name of the directive inside \{ \}. Directives can have arguments, which are surrounded by : :.

For example:

  \:\:\:{directive} Parameter
  :argument:
  :second-argument: Foobar

  \:\:\:

```{seealso}
Additional documentation:
 - [MyST](https://myst-parser.readthedocs.io/en/latest/index.html)
 - [Sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#code-examples)
 - [Sphinx Design](https://sphinx-design.readthedocs.io/en/furo-theme/)
```


Standard Markdown features like _italic_, *italic*, **bold**, __bold__, [links](https://example.org) or
 - unordered
 - lists

or
 1. ordered
 1. lists

are all available.

| Element        | Markdown Syntax      | Description                                   |
| -------------- | -------------------- | --------------------------------------------- |
| Header 1       | `# H1`               | Largest header, equivalent to `<h1>` in HTML. |
| Header 2       | `## H2`              | Second largest header.                        |
| Bold Text      | `**Bold**`           | Makes text bold.                              |
| Italic Text    | `_Italic_` or `*Italic*` | Makes text italic.                           |
| Link           | `[Text](URL)`        | Creates a hyperlink with the provided text.  |
| Image          | `![Alt text](URL)`   | Embeds an image.                              |
| Unordered List | `- Item`             | Creates a bulleted list.                      |
| Ordered List   | `1. Item`            | Creates a numbered list.                      |
| Blockquote     | `> Quote`            | Creates a blockquote.                         |
| Code (Inline)  | `` `Code` ``         | Displays inline code.                         |
| Code (Block)   | <pre>```<br>Code<br>```</pre> | Displays a block of code.               |
| Table          | See below            | Creates a table.

:::{table} Table with caption
:widths: auto
:align: center

| foo | bar |
| --- | --- |
| baz | bim |
:::


A [link][1] that doesn't have the URL locally, but hidden away in the bottom of the source.

- This is a manually-numbered footnote reference.[^3]
- This is an auto-numbered footnote reference.[^myref]

A longer footnote definition.[^mylongdef]

[^mylongdef]: This is the _**footnote definition**_.

    That continues for all indented lines

    - even other block elements

    Plus any preceding unindented lines,
that are not separated by a blank line

This is not part of the footnote.



The normal Markdown way:
![OpenSpace Logo](img/logo.png)

And the way with more options:
:::{image} img/logo.png
:alt: OpenSpace Logo
:class: bg-primary
:width: 200px
:align: center
:::

---


:::{note}
Just a standard note. Named `directive-node` in the plugin.
:::

:::{tip}
Some helpful tip.
:::

:::{danger}
Something dangerous tip.
:::

:::{warning}
A warning note. Named `directive-warning` in the plugin.
:::

:::{admonition} Alternative way of specifying
:class: warning

Here's my admonition content
:::

::::{note}
The next info should be nested
:::"{warning}
Here's my warning
:::
::::

:::{versionadded} 2.5
If something is only available in a specific version
:::

:::{versionchanged} 3.1
Something has changed in this version
:::

:::{deprecated} 4.5
Something has been deprecated but not removed
:::

:::{seealso}
Some other information that would be good to checkout
:::

:::{rubric} A heading that will not show up in the table of contents
:::

:::{hlist}
:columns: 2

 * A list of
 * short items
 * that should be
 * displayed
 * horizontally
:::

:::{code-block}
-- Lua is the default for code blocks
local abc = function()
  return [[
    a
  ]]
end
:::


:::{code-block} cpp
:linenos:
:caption: Line numbers and captions

int foo() {
  // But it can be changed to C++ as well
  return 1 * 2 * 3 * 4;
}
:::

:::{code-block} cpp
:linenos:
:emphasize-lines: 2, 4

// Highlighting some lines
int bar() {
  constexpr int One = 1;
  constexpr int Two = 2;
  constexpr int Three = 3;

  return One + Two + Three;
}
:::

Since Pythagoras, we know that {math}`a^2 + b^2 = c^2`


:::{card} Card Title
Some header information
^^^
Some text that is displayed in a nice card
+++
Footer information
:::

::::{tab-set}
:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::
::::

See [MermaidJS](http://mermaid.js.org/#/) documentation for more information
:::{mermaid}
sequenceDiagram
    Alice ->> Bob: Hello Bob, how are you?
    Bob-->>John: How about you John?
    Bob--x Alice: I am good thanks!
    Bob-x John: I am good thanks!
    Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

    Bob-->Alice: Checking with John...
    Alice->John: Yes... John, how are you?
:::

:::{mermaid}
graph LR
    A[Square Rect] -- Link text --> B((Circle))
    A --> C(Round Rect)
    B --> D{Rhombus}
    C --> D
:::

:::{mermaid}
gitGraph:
  commit "Ashish"
  branch newbranch
  checkout newbranch
  commit id:"1111"
  commit tag:"test"
  checkout main
  commit type: HIGHLIGHT
  commit
  merge newbranch
  commit
  branch b2
  commit
:::


:::{glossary}
Some Term
  The description what the term means

Sphinx
  Sphinx makes it easy to create intelligent and beautiful documentation.

MyST
  Myst is an adventure video game designed by the Miller brothers, Robyn and Rand. It was developed by Cyan, Inc., published by Broderbund, and initially released in 1993 for the Macintosh.
:::

To use it in the text use it like this {term}`Sphinx`

:::{math}
 \int (a + b)^{i_j} = \frac{c}{d}
:::

$$
\sum_{i=0}^\infty i^2
$$

Some way to specify targets for referencing back to it:

(some-label)=
> Text text text

Now we can refer back to the previous section {ref}`reference <some-label>` by inserting it in the text.

:::{py:function} send_message(sender, priority)

Send a message to a recipient

:param str sender: The person sending the message
:param priority: The priority of the message, can be a number 1-5
:type priority: int
:return: the message id
:rtype: int
:raises ValueError: if the message_body exceeds 160 characters
:::

{abbr}`LIFO (last-in, first-out)`

{command}`rm`

{kbd}`C-x C-f`

{menuselection}`Start --> Programs`


Include some external file:

:::{include} .gitignore
:::

% This is a comment that won't be printed into the main document


[1]: https://www.google.com "a title"
[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.
