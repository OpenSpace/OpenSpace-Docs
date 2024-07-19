# 0.20.1
  - Release Date: 2024-07-18
  - Commit: [b368116](https://github.com/OpenSpace/OpenSpace/commit/c26f9db7d427c9d72f339f745cb2e5fb243ca6aa)
  - Full changelog: [link](https://github.com/OpenSpace/OpenSpace/releases/tag/releases%2Fv0.20.1)

Download version 0.20.1 for Windows and Mac on the OpenSpace website [installation page](https://openspaceproject.com/version-0201). Below are notes that highlight new content and bug fixes that will be relevant for OpenSpace users.


## Features
- **TileProviderByDate**: A new TileProvider type to select tile providers based on the date. Has been applied to the VIIRS Earth Layers.
- **Load More Models**: The model loading system now supports models with vertex colors.
- **Image Sequencing Performance**: Improved framerate during image sequencing.

## User Interface
- **Scene Menu**:
  - Possiblity to control the sorting of scene graph nodes in the Scene menu using a numerical value. This has been applied to the grids that show different distances.
  - Access Focus and Navigation controls in the popout menu per scene graph node.
  - Restructuring of the hierarchical menu groups. [See details below](#updated-hierarchy-in-scene-menu).

## Content
- **2024 Digital Universe Data Update**
  - **Updated Datasets For**: Stars & labels, Constellations, Exoplanets, Globular Clusters, H2 Regions, Open Clusters, Planetary Nebulae, Pulsars, Quasars, Sload Digital Sky Survey, Supernova Remnants.
  - **New Datasets**: Star Distance Uncertainty, White/Brown Dwarfs.
  - Updated descriptions for some additional datasets.
- **New Assets** (apart from Digital Universe):
  - Example asset to show the current in-game time in a screenspace object.
  - An advanced example asset for the point cloud rendering, changing the orientation of the points.
- **Updates to Existing Assets/Profiles**
  - New keybinds to set the time to realtime and "now" using arrow keys Down and Up respectively.
  - Fixed spelling mistake in the Haumea model.
  - Removed warning from hdf.asset.
  - Our provided assets no longer include version numbers (these were unused and inconsistent).
- **Content Creation**
  - DashboardItems can now be added to ScreenSpaceDashboards from assets.
  - Layers specification in RenderableGlobe is now optional.
  - Improved error messages for asset loading.
  - A task to generate a raw volume (used in for example RenderableTimeVaryingVolume) from a CSV file.
  - Actions are no longer "local" by default.

## Lua (Scripting)
- A new Lua function to calculate the number of seconds between two dates: `openspace.time.duration(start, end)`.
- A new Lua function to create debug coordinate axes for a scene graph node: `openspace.debugging.createCoordinateAxes()`.

## Bug Fixes
- **Stability and Performance**: Several bug fixes addressing crashes, rendering issues, UI errors, and data handling problems.

## Breaking Changes
- Actions that no dot specify `IsLocal` will now be not local per default. Before, it was the opposite.
- The old Lua function for creating debug coordinate axes (`openspace.debugging.addCartesianAxes`) has been replaced with the new function ([see above](#lua-scripting)) and no longer exists.
- RenderEngine properties `ShowStatistics`, `StatisticsScale` and `ShowFrameInformation` have been moved to the Debugging Module.
- **Digital Universe Update**:
  - The star positions have been updated, so any custom content that is based on these positions (such as bookmarks) may require updating.
  - Constellations (Extragalactic) is removed.
  - The Dwarfs asset has been split up into White and Brown Dwarfs.
  - The Oort Sphere has been moved into its own asset file.
  - Separate assets for all-sky images:
    - The Milky Way Sphere scene graph node and asset have been removed and replaced with the Visible Milky Way in All Sky Images. New Identifier: `MilkyWay` -> `AllSky_Visible`.
    - H Alpha has been moved from the backgroundradiation.asset to its own asset. New Identifier: `HAlpha` -> `AllSky_HAlpha`.
  - Cosmic Background Explorer has a new identifier and GUI name. New Identifier: `CBE` -> `COBE`. New name in GUI: 1990 COBE CMB.

## Updated Hierarchy in Scene Menu

As part of updating the Digital Universe datasets, there has also been a significant change to the hierarchical structure of the Scene menu in the user interface. The GUI paths have been updated to better reflect

- The default top categories are now "Night Sky", "Solar System", "Milky Way", and "Universe". "Other" has been removed, and what was previously located under this group has been spread out to the other categories. Notice the addition of the "Night Sky" category to collect content that is specifically related to studying the night sky.
- The Grids, Lines and Points from "Other" has been moved to "Solar System/Grids", "Milky Way/Grids", "Universe/Grids", and "Night Sky/Coordinate Systems".
- The structure within the top categories has also been slightly changed to be more informative, correct (previously some objects that aren't galaxies were located under "Galaxies" in the menu, for example), and easier to explore. Note particularly that what was previously located in "Universe/Galaxies" is now split up into "Nearby Surveys" and "Deep Sky Surveys" under Universe, and that "Milky Way" now has several extra groups for collecting related objects that did not exist previously.
- Note that the top categories are no longer in order based on universal "scale", e.g. first Solar System, then Milky Way, then Universe. This is a known bug and is being worked on.

Below is a comparison of the hierarchy in the Scene menu before and after this update. The image shows what's under each of the top categories, one level into the menu tree.

:::{figure} SceneMenu_duUpdate_restructure.png
:width: 50em
:::
