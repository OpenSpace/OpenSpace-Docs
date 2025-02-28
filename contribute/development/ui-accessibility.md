# UI Accessibility Guidelines

This page covers guidelines for accessibility when it comes to developing user interfaces or webpages for OpenSpace or related services. Below are some key points to think of from an accessiblity point of view when designing UI components or webpages. Note that the list is not exclusive, and may be extended in the future.

The points below may include a link to an issue on the OpenSpace GitHub. These are examples of comments from previously hired accessiblity consultants on different parts of the UI, and can act as a guidance on how to address a specific issue.

:::{note}
Note that many of our user interfaces are web-based and should as far as possible adhere to the [Web Content Accessbility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/).
:::


## Contrasts
In general contrasts are one of the key importances when designing the UI. Make sure that font colors, background colors, hover-effects, focus etc., all fulfill WCAG requirements (see below) at all times.

  - Useful [site](https://contrast-grid.eightshapes.com/) to check color contrast fulfill WCAG level AA or AAA
  - All color contrasts must meet atleast AA requirement of 4.5:1 or AAA 3:1, see [WCAG](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html) for more info. [#3103](https://github.com/OpenSpace/OpenSpace/issues/3103) [#3094](https://github.com/OpenSpace/OpenSpace/issues/3094)
  - Make sure contrasts are fulfilled in both light mode and dark mode.

## Navigation
  - Make sure buttons can be activated using both `Spacebar` and `Enter Key`. [#3092](https://github.com/OpenSpace/OpenSpace/issues/3092)
  - Make sure there is a way to close any window using keyboard, either through a cancel button or e.g, escape keypress
  - Make sure that the tab order of menu items make sense and are not jumping all over the menu. [#3099](https://github.com/OpenSpace/OpenSpace/issues/3099)

## General
- Make sure Qt elements have a `setAccessibileName` and/or `setAccessibleDescription` that are sensible, use descriptive names e.g., "new x", "edit x" instead of just "new" and "edit". [#3089](https://github.com/OpenSpace/OpenSpace/issues/3089)

  - Ensure forms clearly show which fields are required and which ones are optional e.g., using asterix (visual) and adding a descriptive text (e.g., "required") for screen readers. [#3101](https://github.com/OpenSpace/OpenSpace/issues/3101)
  - Prefer error dialog / modal over having an error message printed somewhere on screen. Optionally set the focus back to the problem input field (if possible) and add an accessible descriptive text. [#3100](https://github.com/OpenSpace/OpenSpace/issues/3100)
