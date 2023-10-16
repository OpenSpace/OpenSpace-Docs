# Kitchen Sink
This page serves as a reference to the features supported by the MyST + Sphinx + Read The Docs stack that is used to create this wiki page. This page is probably best viewed in source which you can find with the "Edit on GitHub" link in the top right. If you are using Visual Studio Code, the [MyST-Markdown plugin](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) is recommended as it provides code snippets for the different directives that MyST adds to regular Markdown. In general, a block is surrounded by `:::` followed by the name of the directive inside `{ }`. Directives can have arguments, which are surrounded by `: :`.

For example of this:
```
:::{directive} Parameter
:argument:
:second-argument: Foobar
:::
```

:::{seealso}
Additional documentation:
 - [MyST](https://myst-parser.readthedocs.io/en/latest/index.html)
 - [Sphinx](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#code-examples)
 - [Sphinx Design](https://sphinx-design.readthedocs.io/en/furo-theme/)
:::

## Markup
Standard Github-flavored Markdown is available as a basis. You can find more information about it [here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). For completeness, here is a quick reference list:

| Element        | Markdown Syntax      | Description                                   |
| -------------- | -------------------- | --------------------------------------------- |
| Header 1       | `# Header 1`         | Largest header, equivalent to `<h1>` in HTML. |
| Header 2       | `## Header 2`        | Second largest header.                        |
| Header 3       | `### Header 3`       | Third largest header.                         |
| Header 4       | `#### Header 4`      | Fourth largest header.                        |
| Header 5       | `##### Header 5`     | Fifth largest header.                         |
| Bold Text      | `**Bold**`           | Makes text bold.                              |
| Italic Text    | `_Italic_` or `*Italic*` | Makes text italic.                        |
| Link           | `[Text](URL)`        | Creates a hyperlink with the provided text.   |
| Image          | `![Alt text](URL)`   | Embeds an image.                              |
| Unordered List | `- Item`             | Creates a bulleted list.                      |
| Ordered List   | `1. Item`            | Creates a numbered list.                      |
| Blockquote     | `> Quote`            | Creates a blockquote.                         |
| Code (Inline)  | `` `Code` ``         | Displays inline code.                         |
| Code (Block)   | <pre>```<br>Code<br>```</pre> | Displays a block of code.            |
| Table          | See source           | Creates a table.                              |

### Heading without TOC entry
:::{rubric} A heading that will not show up in the table of contents
:::

### Subscript/Superscript
We can also write text in {sub}`subscript`, or {sup}`superscript` or other hings

### Abbreviations
Defining abbreviations, which have an explanation that is visible via hovering over the text: {abbr}`LIFO (last-in, first-out)`

### Commands
Displaying a program that is available on the computer: {command}`rm`

### Keystrokes
Showing a combination of keystrokes that should be pressed by a person to achieve something: {kbd}`C-x` {kbd}`C-f`

### Menu Selection
Showing a sequence of menu items that someone has to go through in order to achieve something: {menuselection}`Start --> Programs`

### Inline comments
% This is a comment that won't be printed into the main document

### Icons embedding
We can also provide images directly into the text: {octicon}`heart-fill;1em;sd-text-danger`. The list of all icons can be found [here](https://primer.style/design/foundations/icons).

## Tables
### Markdown-style
| foo | bar |
| --- | --- |
| baz | bim |

### MyST style
:::{table} Table with caption
:widths: auto
:align: center

| foo | bar |
| --- | --- |
| baz | bim |
:::

### Multi-column table
:::{hlist}
:columns: 2

 * A list of
 * short items
 * that should be
 * displayed
 * horizontally
:::


## Links
A [link][1] that doesn't have the URL locally, but hidden away in the bottom of the file. The link here would be the same as [this](https://www.google.com) link. We can also add footnotes, either as a manually-numbered reference[^3], or an automatically-numbered reference[^myref]. Footnotes can also be a lot longer, too[^mylongdef]. The actual content behind the footnote can be placed anywhere in the source file, but will always be rendered at the bottom of the page.

### Footnotes
[^mylongdef]: This is the _**footnote definition**_.

    That continues for all indented lines

    - even other block elements

    Plus any preceding unindented lines,
that are not separated by a blank line

This is not part of the footnote.


## Images
### Markdown
The normal Markdown way:
![OpenSpace Logo](https://source.unsplash.com/200x200/daily?cute+animals)

### Centering images
But MyST also added a second method that has way more options. See their [documentation](https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html#block-level-images) for more information.
:::{image} https://source.unsplash.com/200x200/daily?cute+animals
:alt: OpenSpace Logo
:class: bg-primary
:width: 200px
:align: center
:::

### Captions
Or with captions underneath
:::{figure} https://source.unsplash.com/200x200/daily?cute+animals
We can also add captions to the images by using the `figure` environment
:::

### Dark and Light theme
We can use different images for light and dark themes
:::{image} https://source.unsplash.com/200x200/daily?cute+dogs
:align: center
:class: only-light
:::

:::{image} https://source.unsplash.com/200x200/daily?cute+cats
:align: center
:class: only-dark
:::

:::{figure} https://source.unsplash.com/200x200/daily?cute+cats
:align: center
:figclass: only-light
:::

:::{figure} https://source.unsplash.com/200x200/daily?cute+dogs
:align: center
:figclass: only-dark
:::


## Videos
Embedding videos does not work natively in Markdown and we need to fall back to raw HTML instead:

<center><iframe width="740" height="530" id='tutorialPlayer' src="https://www.youtube.com/embed/YHl5L85hEUQ?enablejsapi=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></center>



## Callouts
MyST adds a bunch of different admonition styles, which are demonstrated here.

:::{attention}
Attention
:::

:::{caution}
Caution
:::

:::{danger}
Danger
:::

:::{error}
Error
:::

:::{hint}
Hint
:::

:::{important}
Important
:::

:::{note}
Note
:::

:::{seealso}
Some other information that would be good to checkout
:::

:::{tip}
tip
:::

:::{warning}
warning
:::


## Sidebar
:::{sidebar} Ch'ien / The Creative

    Lorem ipsum dolor sit amet consectetur adipisicing elit.

    .. image:: https://source.unsplash.com/200x200/daily?cute+puppy

    Lorem ipsum dolor sit amet consectetur adipisicing elit.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.
:::
There is the option to provide information in a sidebar as well. We'll just add some more text here that makes it more obvious. Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.


## Markups
:::{versionadded} 2.5
If something is only available in a specific version
:::

:::{versionchanged} 3.1
Something has changed in this version
:::

:::{deprecated} 4.5
Something has been deprecated but not removed
:::


## Code Highlighting
### Default language
:::{code-block}
-- There is no default language for code blocks
local abc = function()
  return [[
    a
  ]]
end
:::

```
-- This is also true for standard Markdown code highlighting
function(abc)
  return abc + abc
end
```

### Different language
:::{code-block} lua
-- But we can manually specify which language it is
local abc = function()
  return [[
    a
  ]]
end
:::

```lua
-- Also for blocks
function(abc)
  return abc + abc
end
```


:::{code-block} cpp
// It's possible to change the language for the syntax highlighting as well
std::vector<std::optional> foo() {
  return std::nullopt;
}
:::

```cpp
// Same for the standard Markdown, which is nicer for Visual Studio Code syntax highlighting
std::string_view bar() { return "abc"; }
```

### Line number and captions
:::{code-block} cpp
:linenos:
:caption: Line numbers and captions

// The directive-based way can have different options, for example to
// show line numbers and a caption
int foo() {
  // But it can be changed to C++ as well
  return 1 * 2 * 3 * 4;
}
:::

### Highlight lines
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

### Function defintions
It is also possible to define functions in place:

:::{py:function} send_message(sender, priority)

Send a message to a recipient

:param str sender: The person sending the message
:param priority: The priority of the message, can be a number 1-5
:type priority: int
:return: the message id
:rtype: int
:raises ValueError: if the message_body exceeds 160 characters
:::


## Math
There are different ways of highlighting mathematical equations, all of which use LaTeX-based syntax. Equations can be provided inline, for example like this: {math}`a^2 + b^2 = c^2`. Alternatively, it is also possible to provide formulas in a block environment. Option 1 as a directive:

:::{math}
 \int (a + b)^{i_j} = \frac{c}{d}
:::

and option 2 using the \$\$ markers:

$$
\sum_{i=0}^\infty i^2
$$


## Cards
:::{card} Simple Card Title
Some header information
^^^
Some text that is displayed in a nice card
+++
Footer information
:::


More fullyfledged example from the MyST documentation:
::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`markdown;1.5em;sd-mr-1` CommonMark-plus

MyST extends the CommonMark syntax specification, to support technical authoring features such as tables and footnotes.

+++
[Learn more »](https://example.org)
:::

:::{grid-item-card} {octicon}`plug;1.5em;sd-mr-1` Sphinx compatible

Use the MyST role and directive syntax to harness the full capability of Sphinx, such as admonitions and figures, and all existing Sphinx extensions.

+++
[Learn more »](https://example.org)
:::

:::{grid-item-card} {octicon}`tools;1.5em;sd-mr-1` Highly configurable

MyST-parser can be configured at both the global and individual document level,
to modify parsing behaviour and access extended syntax features.

+++
[Learn more »](https://example.org)
:::

::::


## Carousels
````{card-carousel} 2

```{card} card 1
```

```{card} card 2
```

```{card} card 3
```

```{card} card 4
```

```{card} card 5
```

```{card} card 6
```
````

## Dropdown
### No Title
```{dropdown}
Dropdown content
```

### With title
```{dropdown} Dropdown title
Dropdown content
```

### Standard open
```{dropdown} Open dropdown
:open:

Dropdown content
```


## Buttons
```{button-link} https://example.com
Button text
```

```{button-link} https://example.com
:color: primary
Button text
```

```{button-link} https://example.com
:color: secondary
:expand:
```


## Tabs
Tabs can be useful if there are multiple ways of doing something, for example if we want to highlight examples in multiple programming languages.
::::{tab-set}
:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::
::::

::::{tab-set}
:::{tab-item} Lua
```
local openspace = ...
openspace.globebrowsing.goToGeo(123.0, -40.0)
```
:::

:::{tab-item} JavaScript
```javascript
let openspace = ...;
openspace.globebrowsing.goToGeo(123.0, -40.0)
```
:::

:::{tab-item} Python
```python
openspace = ...
openspace.globebrowsing.goToGeo(123.0, -40.0)
```
:::
::::


## Diagram
See [MermaidJS](http://mermaid.js.org/#/) documentation for more information about the available diagram types

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


## Glossary
Defining glossary terms that can be used across the entire documentation page. Regardless where the glossary terms are defined, they will be usable on any page.

:::{glossary}
Some Term
  The description what the term means

Sphinx
  Sphinx makes it easy to create intelligent and beautiful documentation.

MyST
  Myst is an adventure video game designed by the Miller brothers, Robyn and Rand. It was developed by Cyan, Inc., published by Broderbund, and initially released in 1993 for the Macintosh.
:::

To use it in the text use it like this {term}`Sphinx`


## Section Labels
Some way to specify targets for referencing back to it:

(some-label)=
> Text text text

Now we can refer back to the previous section {ref}`reference <some-label>` by inserting it in the text.


## Include files
### Verbatim include

Include the `.gitignore` file:
:::{include} /.gitignore
:::

### Include file with syntax highlighting
#### Raw include
```{literalinclude} example.json
:language: json
```

#### With Caption
```{literalinclude} example.json
:language: json
:caption: With a caption to [download](example.json)
```

#### Emphasize lines
```{literalinclude} example.json
:language: json
:emphasize-lines: 5,6
```

#### Selected lines
Only show selected lines

```{literalinclude} example.json
:language: json
:lines: 1, 3, 7-9, 10
```




[1]: https://www.google.com "a title"
[^myref]: This is an auto-numbered footnote definition.
[^3]: This is a manually-numbered footnote definition.
