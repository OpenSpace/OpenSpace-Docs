# UI Accessibility Guidelines

This page covers guidelines for accessibility when it comes to developing user interfaces or webpages for OpenSpace or related services. Below are some key points to think of from an accessiblity point of view when designing UI components or webpages. The list is not exclusive, and may be extended in the future.

:::{note}
Many of our user interfaces are web-based and should as far as possible adhere to the [Web Content Accessbility Guidelines (WCAG)](https://www.w3.org/TR/WCAG21/).
:::


## Contrasts
In general, contrasts are one of the key importances when designing the UI. Make sure that font colors, background colors, hover-effects, focus etc., all fulfill WCAG requirements (see below) at all times.

  - All color contrasts must meet atleast AA requirement of 4.5:1 or AAA 3:1, see [WCAG](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html) for more info.
    - Useful [site](https://contrast-grid.eightshapes.com/) to check color contrast fulfill WCAG level AA or AAA.
  - Make sure contrasts are fulfilled in both light mode and dark mode.
  - Also make sure that contrasts are fulfilled for text that is rendered on top of an image. A potential solution could be to add a background color or drop shadow to the text.

## Navigation
  - Make sure buttons can be activated using both `Spacebar` and `Enter Key`
  - Make sure there is a way to close any window using keyboard, either through a cancel button or e.g, escape keypress
  - Make sure that the tab order of menu items makes sense and is not jumping all over the menu, when focusing object using `Tab`.

## General
  - Ensure that all element have accessible names that are sensible. Use descriptive names e.g., "new x", "edit x" instead of just "new" and "edit"
    - Web: Use `aria-labels` when needed
    - Qt: Make sure Qt elements have a sensible `setAccessibileName` and/or `setAccessibleDescription`
  - Ensure forms clearly show which fields are required and which ones are optional e.g., using asterix (visual) and adding a descriptive text (e.g., "required") for screen readers
  - Make sure error messages are communicated to screen readers. Prefer error dialog / modal over having an error message printed somewhere on screen. Optionally set the focus back to the   problem input field (if possible) and add an accessible descriptive text
