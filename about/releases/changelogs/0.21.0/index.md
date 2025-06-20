# 0.21.0
  - Release Date: 2025-06-20
  - Commit: [80f46de](https://github.com/OpenSpace/OpenSpace/commit/80f46ded1f97d7de40a34179446e9cc47299ab91)
  - Full changelog: [link](https://github.com/OpenSpace/OpenSpace/releases/tag/releases%2Fv0.21.0)

Download version 0.21.0 on the OpenSpace website [installation page](https://openspaceproject.com/version-0210). Below are notes that highlight new content and bug fixes that will be relevant for OpenSpace users.

## A More Flexible Interface
-   Complete redesign of the user interface for easier use and better customization.
-   Dockable, resizable windows let you arrange panels how you like.
-   Toolbar controls let you show only the menus you use most.
-   Menus (like scene and property menus) are better organized.
-   A "Getting Started Tour" appears the first time you launch OpenSpace on a new computer.
-   Clear notifications alert you to warnings and errors.

## New Presentation Tools & Night Sky Features
-   New Night Sky panel, ideal for constellation and planetarium-style shows.
-   "ShowComposer" tool allows you to create your own custom control panels (`http://localhost:4680/showcomposer`) with narration scripts for presenters. 

## Enhanced Navigation
-   Zoom control using Z and X keys is now smoother and more responsive.
-   More accurate camera position and distance display, even when not focused on planets.
-   Each window can now have its own horizontal field of view (FOV).
-   Ability to mirror or offset display windows.
    
## Updated Datasets
-   Exoplanets now have: 
    -   Labels for star systems
    -   Color-coding based on planet type (e.g., super-Earth, gas giant)
    -   Optional surface textures
-   New profile: "Today’s Sun" shows current solar magnetic activity.
-   New content includes:
    -   Kuiper satellite constellation
    -   High-res maps of Titan and Phobos
    -   ESRI Wayback Earth map layers
-   Stars can now move over time using real motion data, if available.
-   Updated datasets and visuals for exoplanets, brown dwarfs, Neptune, Uranus, the Moon, and constellations.

## Easier File Handling & Content Loading
-   Drag and drop support: Add files or folders directly into OpenSpace.
-   Map files (WMS) and assets now load from a dedicated user folder (`globebrowsing`).
-   Launcher improvements:
    -   Dark mode support
    -   Better save options for profiles
    -   Icons to indicate user-created content
    -   Keyboard shortcuts for managing window layouts

## Accessibility and Language Support
-   Full keyboard navigation across the interface using `TAB` and `ENTER`.
-   Improved contrast and color consistency for readability.
-   Support added for future interface translation/localization.
-   New options for setting background and text colors on buttons.
-   Only focusable objects now display UI hints to reduce clutter.
    
## Improvements for Custom Datasets
-   New tools for creating and customizing content:
    -   Dome overlays, screen blackouts, time-linked image displays, and dashboard widgets
-   Scripted content can now:
    -   Run on a schedule
    -   Reload without restarting OpenSpace
    -   Track system memory usage   
-   Lua scripting enhancements:
    -   Safer sandboxed execution by default
    -   Streamlined navigation and focus functions
    -   Improved tagging and content reordering

## Bug Fixes
-   Resolved crashes related to maps, animations, layer deletion, and asset loading.
-   Fixes for:
    -   Non-English keyboard input
    -   Star rendering and Saturn ring shadows
    -   Field-of-view calculation issues
-   Improved performance and UI behavior across large screens and custom dashboards.
-   Numerous additional fixes to support smooth operation and content loading.

## Key Changes to Be Aware Of
-   The "Touch" profile has been removed.
-   Keybindings have changed:
    -   `ESC` has been replaced with `Ctrl + Q` to exit.
    -   `TAB`/`Shift + TAB` replaced with `F1`/`Shift + F1` to toggle the UI.   
-   Some assets, script commands, and fieldline properties have been renamed or reorganized.
-   Dashboard and rendering behavior may look different due to visual updates and defaults.
