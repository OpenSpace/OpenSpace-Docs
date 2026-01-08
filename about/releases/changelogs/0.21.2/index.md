This patch release fixes an issue where planetary surfaces would disappear when the camera approaches them and high-resolution images were displayed.

# Features
  - Added the functionality to automatically choose a discrete graphics card over an integrated graphics card on laptops that have both
  - Improved the rendering of orbital trajectories, specifically for very large datasets (#3739)
  - Improved the visual fidelity of Saturn's rings and its shadow on the planet (#3749)

## UI
  - Moved the map of Earth from the night sky panel into the GeoLocation panel and add the ability to search for features on other planetary bodies (OpenSpace/OpenSpace-WebGui#184)
  - Added a confirmation dialog to some property settings that are irreversible, like disabling the mouse input (#3730)
  - Correctly reflect in the user interface when navigation and time controls are disabled during recording playbacks (OpenSpace/OpenSpace-WebGui#175)
  - Added a new tab to the ScreenSpace renderables panel to add a browser with a specific webpage (OpenSpace/OpenSpace-WebGui#177)
  - Added the functionality to hide panels at lower visibility levels. Hide the ScriptLog unless the visibility is set to "Advanced User" (OpenSpace/OpenSpace-WebGui#186)
  - Improved the keybinds panel to show all keys bound to a specific key instead of needed to manually switch between Shift, Alt, and Ctrl keybindings (OpenSpace/OpenSpace-WebGui#182)
  - Improved the handling of text fields that are too long by displaying hover tooltips that show the full name of, for example, scene graph nodes (OpenSpace/OpenSpace-WebGui#188)

# Content
## New Assets
  - Added a new asset for 3I/ATLAS
  - Added a new asset with an action for locking temporal layers (#3760)

## Updates to existing Assets/Profiles
  - Updated the temporal night time layer on Earth as the previous was no longer working
  - Changed GUI naming and coloring for 1I/'Oumuamua and 2I/Borisov and added labels for both
  - Removed Plutos Keplerian trail as the new kernels are now reaching back to 1549 (#3726)
  - Renamed Galactic Line/Band to equator and updated their identifiers (#3737)
  - Added a longitude/latitude grid to Earth (#3059)
  - Added missing absPath() in the slidedeck example
  - Fixed the Sun glare to use the correct billboarding for fisheye rendering

## Content creation
  - `ContiguousMode` in `RenderableOrbitalKepler` is now an AdvancedUser property

## API
  - Added the camera view direction information to the camera topic (#3741)

# Bug Fixes
  - Occasionally, the camera was moved outside the universe when rotating around Earth (#3497)
    - *Important*: If you are using the MRF cache, you need to delete the `mrf_cache/Earth/Height Layers/Terrain_tileset` folder
  - The JWST profile failed to load
  - The Euclid profile failed to load
  - The Messenger profile failed to load
  - It was not possible to load the user interface on a different device (OpenSpace/OpenSpace-WebGui#187)
  - Shift-clicking the enabled checkbox for scene graph node caused the immediateness to get stuck (#3744)
  - The info button in the kebab menu of the current scene graph was not visible (#3735)
  - When the Lua console was open, any keystroke was still being used by the main user interface (#3649)
  - The `GanymedePosition` scene graph node was placed in the incorrect folder in the Juice profile
  - The names for many profiles in the meta information was incorrect (#3743)
  - The opacity slider for the Milky Way galaxy was inoperable
  - The quick adjust slider in the time panel was broken (OpenSpace/OpenSpace-WebGui#176)
  - The "All globes" illumination was not actually applied to all globes (#3729)
  - It was not possible to focus the camera on Charon
  - The Local Dwarf Groups were using a wrong color mapping
  - It was not possible to pick a text value from the script log in the Profile editor (#3620)
  - The menu bar on MacOS was incorrectly set, causing crashes
  - It was not possible to use relative paths in a GeoJSON texture (#3761)
  - The planets sonification was crashing when no planets were available
  - The documentation for RenderablePlaneSpout and RenderableSphereSpout was missing
  - The min/max values for the transform matrix of a RenderableModel were set incorrectly (#3746)
  - When calling `setPropertyValue` with a 0 second duration, the postscript was not called
  - Some long tooltip descriptions were not correctly broken across lines (OpenSpace/OpenSpace-WebGui#180)
  - It was possible to drag a hidden window from just below the menu bar (OpenSpace/OpenSpace-WebGui#183)
  - Exoplanet globes were producing warning messages when they only had a single solid color (#3728)
  - Exoplanet globes were producing warning messages when MRF caching was enabled
  - Image layers based on PNG and JPG were producing excessive warning messages when MRF caching was enabled
  - Using the `toggleFade` function was printing an error message even though there was no error condition
  - The Video module had an enabled property that was unused

