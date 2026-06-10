# OpenSpace 0.22.0

## Highlights

OpenSpace 0.22.0 is a major release bringing significant performance improvements, new rendering capabilities, and important platform changes marking a large step towards a future 1.0 release.

**Platform:** macOS support has been removed due to Apple's long-standing failure to advance their OpenGL support. OpenSpace now targets **OpenGL 4.6**, delivering improved rendering performance across the board.

**Performance:** Asteroid and orbital rendering via `RenderableOrbitalKepler` is up to **8x faster** thanks to multithreading and CPU-side vertex computation. Kepler data loading (e.g. Minor Planet Center) is up to **20x faster**. Additional gains come from fewer texture binds and triple-buffered NDI streaming.

**New Renderables:** This release introduces `RenderableVectorField` for 3D vector volume visualization, dynamic shadow mapping between models and globes, Solar Imagery rendering (`RenderableSolarImagery` / `RenderableSolarImageryProjection`), Dynamical Molecular Systems via the [ViaMD](https://github.com/scanberg/viamd) library, and new `ScreenSpaceText`/`ScreenSpaceDate` objects.

**Content & Workflow:** A new **AssetBuilder** application simplifies scene graph node creation without manually editing `.asset` files. **Profile Add-ons** provide opt-in curated asset collections (interstellar objects, DESI, dwarf planets, minor moons, asteroids). Asset files have been extensively reorganized into composable parts.

**UI:** New panels for browsing/adding assets at runtime, interactive WMS layer addition for GlobeBrowsing, improved touch gestures, millisecond time display, and a redesigned Lua console with tab completion and word-level editing.

**Infrastructure:** Default servers have migrated from Utah-based to New York-based and the new BigBang servers. Satellite data is now relayed through OpenSpace's own proxy to reduce load on Celestrak.

> **Note:** This release contains multiple breaking changes. See individual sections below for details on renamed scene graph nodes, changed asset file locations, API updates, and removed features.

---

## Features

  - Use a discrete graphics card preferentially over an integrated card if both exist
  - Improve the overall performance and rendering speed of the `RenderableOrbitalKepler` class (#3739, #3799)
    - Compute relevant vertices on CPU rather than filtering all vertices on the GPU to lower the required memory
    - Remove geometry shader for trails rendering
    - Added multithreading and a better system for updating which segments to render for each orbit. This causes a speed-up of asteroid rendering of about 4-8x
    - Added multithreading for loading of data decreasing the loading time. For example the Minor Planet Center data loading time was reduced by 20x
    - Added support for "Camera View Direction" in addition to existing "Camera Position Normal"
    - Changed GUI name of RenderingMode "Points+Trails" to "Points and Trails"
  - Improvements for the rendering of planarary globes
    - Add support for relative paths in GeoJSON's SpriteTexture (#3761)
    - Increase the visual fidelity of the shadows on a planetary ring (#3749)
    - More user-friendly name for the default properties in a GeoJSON
  - Improve documentations in many places
    - Add missing documentation for many Asset components on the docs.openspaceproject.com page
    - Add more (correctly) restrictive parameter restrictions for Assets components, indicating for example where only positive numbers are allowed
    - Better documentation for the `SGCTConfig` and `Profile` options in the `openspace.cfg` configuration file
  - Various improvement for the `RenderableTrailTrajectory`  (#3742, #2128, #3740)
    - **Breaking Change** Removed `SweepChunk` feature as it was not enabled by default and didn't perform as expected
    - Added toggle for Accurate Trail Points (in asset: AccurateTrail)
    - Removed max vertices ceiling and fixed issues with sample interval
    - Fixed point size rendering issue
  - Add the ability to render a visual indicator for the mouse interaction (#3781)
  - Make the port used by TUIO for touch input configurable (#3813)
  - Various improvements to the `RenderableModel`
    - Add the ability to control the strength of specular highlights
    - Add a mode to render the model as a wireframe
    - Add the ability to overwrite the color of the rendered model
    - The `ResetTileProviders` property is now a `Developer` level property
  - As the Utah-based servers are no longer available, they have been replaced as the default with the New York-based ones for map layers and HttpSynchronizationRepositories (#3847)
  - Add the ability to render dynamic shadows using a `RenderableModel` as a shadow sources and `RenderableGlobe` and `RenderableModel` and receivers of shadows (#3801)
    - See the `data/assets/examples/shadowmapping.asset` for example on how to add shadows to models and globes
  - Add button mappings for Mouse4 and Mouse5 to (CTLR and CTRL+Shift) in order to be able to land on planets using only the mouse (#3850)
  - Various performance improvements
    - Fewer texture bind calls
    - Added triple-buffering to the NDI streaming to prevent some blocking and thus increase transfer speeds
  - Remove support for Mac OS (#3919)
    - Unfortunately Apple has not managed to update their support of OpenGL in the last 16 years, which is impacting all non-MacOS users since we are unable to maintain a dual   rendering path just for MacOS
    - Similarly, the C++ standard on MacOS compilers is lagging the support offered by compilers on Windows and Linux
  - Update the code to use OpenGL 4.6 (#3903)
    - This update brings with it a bunch of small performance improvements that sum up to the default profile running XX% faster than in 0.21.4
    - All graphics cards that do not support OpenGL 4.6 also have been reclared End-of-Life by Nvidia/AMD/Intel, so no graphics card currently running OpenSpace should be affected,   but some very old drivers might be updated
  - Add keybind for toggling idle behavior (#3906)
  - Add a new Renderable type `RenderableVectorField` that takes a 3D volume containing vector data and renders that data using arrows (#3897)
  - Delete the temporary folder with every startup to prevent stale files
  - Add Profile add-ons (#3947)
    - Add-ons represents opt-in features consisting of a list of curated assets. A profile can recommend add-ons that would be suitable for the specific profile, but it should always   be possible to include any add-on into any profile
    - Add addon 'Interstellar Objects' to display the paths of the known interstellar objects
    - Add addon 'desi' to show the results of the DESI instrument
    - Add addon 'dwarf_planets' to show the positions, trails, and globes of the various known Dwarf planets
    - Add addon 'minor_moons' to add the minor moons of the gas giants
    - Add addon 'asteroids' to show some of the known asteroids and comets in the solarsystem
  - Adding the ability to fade the `RenderableGaiaStars`
  - Rename "Idle Behavior" to "Idle Motion" (#3949)
  - Add the ability to enable remote debugging in CEF, but disable it by default
  - The use of the old [data.openspaceproject.com](https://data.openspaceproject.com) is phased out in favor of the new BigBang server [liu-se.bigbang.openspaceproject.com](https://  liu-se.bigbang.openspaceproject.com) and [amnh-us.bigbang.openspaceproject.com](https://amnh-us.bigbang.openspaceproject.com)
  - Adds SolarBrowsing feature (#3926)
    - Two new renderables: `RenderableSolarImagery`, which renders images from a specific spacecraft onto a quad in space. The `SolarImagery` supports multiple instruments so you can   load multiple folders of images and switch between them at runtime.  `RenderableSolarImageryProjection` takes a list of `RenderableSolarImagery` `Identifiers` and projects them   onto a sphere centered on the Sun. Images from multiple sources that overlap will blend color. Any area that is not projected onto will be some default gray-ish value to indicate   no data. Note that there is currently a limitation to assume we're projecting onto the Sun in our solar system.
    - More documentation is available [on the Docs page](https://docs.openspaceproject.com/latest/building-content/solarbrowsing/index.html)
  - Add properties to the `ScreenSpaceBrowser` that allow the sending of keyboard inputs to the displayed browser (#3980)
  - Rendering of Dynamical Molecular Systems using the ViaMD rendering library (#3889)
    - This includes rendering of full quantum-mechanical systems using, for example, GROMACS, but also rendering of individual atoms or proteins from the Protein database
    - More documentation is available at XXX
  - Add the ability to show a full trail for a `RenderableTrailOrbit` (#3757)
    - Added toggle `Force full orbit trail` to that shows a full orbit worth of trail
    - Added toggle that limits forced trail to only be visible between the start time and one orbital period after the end time
    - Added three new properties to asset called `StartTime`, `EndTime` and `LimitToTimeRange`
  - Remove the `configuration_helper` script. Instead a new `default.json` Window layout is now being used to create a window 2/3s the size of the primary monitor (#3986)
  - Updated the texture handling in the `RenderablePointCloud` class, resulting in slightly lower memory footprint (#3990)
  - Add support for different colors and the use of images when blacking out the rendering (#3983)
    - **Breaking Change** The blackout values have been moved into a separate PropertyOwner, thus changing the URI to the blackout factor
    - **Breaking Change** The blackout factor value was inverted compared to the previous solution for consistency with other sliders
  - Add support for CSV format from Celestrak and change requesting format to reduce the amount of bandwidth needed by Celestrak (#4015)
  - Add a new interpolation method to the properties that will cause the value to bounce back and forth between the current value and the selected value (#4013)
  - Improve touch gestures and interaction (#4005)
    - Update handling of 1-finger rotation, pinch, and panning
    - Fix unreliable tap detection
    - Refocus to the current focus node on a triple-tap
    - Only apply direct manipulation if first touch is on the object in question
    - Make zoom/pinch detection more reliable by checking for finger movement, and update roll gesture and computation
    - Reduce default sensitivities a bit for more precise control
    - Make it possible to roll and zoom and the same time
    - Reduce roll sensitivity a bit
  - AssetBuilder (#4012)
    - The AssetBuilder is a new application located in the `bin` folder that is currently capable of generating scene graph nodes. Files are stored in a file format that makes it   possible to edit them later without the need to manually edit any text files. The AssetBuilder is a replacement for manually editing `.asset` files and is capable of creating   files that do not require any complicated Lua scripting
    - More documentation is available at XXX
    - The ability to create more types (ScreenSpace objects, actions, etc) and the ability to access non-local data resources will be added to the AssetBuilder in the future
  - Add trigger properties to jump to the start or end times of a `TimeFrameInterval`
  - Improved that stuttering behavior of playing back videos in clustered environments (#4032)
  - Issues in the creation of an off-screen rendering surface are now better communicated as errors
  - The rendering in the window is now disabled if the window is iconified unless the `render-while-hidden` setting is enabled in the Window Configuration
  - Add the ability for the Window Configuration to further customize the values loaded from Scalable meshes files
  - Add the ability to leave out the window size parameter in a Window Configuration which will cause the window size to be automatically set to 2/3s the size of the primary monitors   resolution
  - Update external dependencies:
    - Tracy 0.10 -> 0.13.1
    - date master -> v3.0.4
    - Assimp v5.4.3 -> v6.0.4
    - Catch2 v3.8.0 -> v3.14.0
    - Freetype2 v2.13.3 -> v2.14.3
    - glbinding master -> v3.5.0
    - glm master -> v1.0.3
    - NDI v4 -> v6
    - nlohmann::json v3.12.0 -> 96c1b52
    - jsonvalidator v2.3.0 -> v2.4.0
    - OpenVR master -> v2.15.6


## Launcher

  - Disable edit button in the Launcher if we start with a built-in profile
  - Add a duplicate button to the action menu in the launcher (#2418)
  - Add the ability to choose units in the Simulation Time Dialog (#1391)
  - Added better tooltip information for items in the dropdown menus. The items now contain both descriptions and file paths
  - Added new icon for user profiles and Window Configuration that are outside of the user folder (called "External")



## UI

  - Add tabs to the "Add webpage" object in the ScreenSpace panel (OpenSpace/OpenSpace-WebGui#177)
  - Adds property confirmation modal hint to properties (#3730)
  - `RenderableOrbitalKepler`'s `ContiguousMode` is now an "Advanced User" property
  - Add new panel to browse assets and be able to add and remove assets (#591, #3798)
    - The new panel shows a list of all assets in the OpenSpace folder and the User folder and provides the ability to add any asset at runtime
    - Assets loaded directly by the profile and assets loaded at runtime can also be removed in the new panel at runtime
  - Add a new GlobeBrowsing panel to be able to interactively add new layers that are provided by WMS servers (for example GIBS) (#3849)
    - Any layer can be added as a ColorLayer, HeightLayer, Overview, or any other layer
    - Any WMS server with a compliant GetCapabilities API end point can be dynamically added at runtime
  - When trying to remove a layer, a "Needs confirmation" dialog will now be shown to prevent accidental remove
  - Add notifications to indicate when files are being downloaded and show the download status and speed when adding assets while OpenSpace is running (OpenSpace/OpenSpace-WebUI#190)
  - Add a new custom view to better expose the video playback controls (OpenSpace/OpenSpace-WebUI#192)
  - The time panel in the toolbar at the bottom can now handle milliseconds (OpenSpace/OpenSpace-WebUI#197)
  - The User Panel has been slightly redesigned to support opening panels in an external browser
  - The Idle Motion is now exposed as a state and a button in the top bar (OpenSpace/OpenSpace-WebUI#199)
  - Add a new overlay window that displays information on how to connect an external browser to OpenSpace. Also displays a QR code to simplify that connection (OpenSpace/  OpenSpace-WebUI#198)
  - Update the order and better organize the windows that can be shown into submenus (#3872)
  - Updates to the Night Sky panel
    - Cleanup the look and feel of the the cardinal direction buttons (#3754)
    - Redesign layout for markings tab and introduce a new toggle component (OpenSpace/OpenSpace-WebUI#207)
    - Redesign cardinal directions part to look different than the others
    - Refactor cardinal direction and make it listen to the currently shown texture
    - Add animation to ToggleCard and move to general components
    - Add placeholder buttons for hide all per group
  - Improve the rendering performance by animating the in-progress fade state of the checkbox instead of directly using the Fade value (OpenSpace/OpenSpace-WebUI#208)
  - Add a new checkbox to control whether a new folder should be created when saving screenshots (OpenSpace/OpenSpace-WebUI#211)
  - Add fixed minimum width to time panel menu button. Prevents the rest of the UI from "jumping around" (OpenSpace/OpenSpace-WebUI#213)
  - Change the style of the scene graph node info table to have fixed header width (#3951)
  - The confirmation modal dialogs now disable the URI of the property that caused the dialog to appear to provide more context
  - Adjust properties to new capitalization rules (title casing using APA style)
  - Improve the UX of the in-game console (#3772)
    - Fix CTRL + Left/Right arrow key not being consumed correctly
    - Add CTRL + backspace and CTRL + delete shortcuts to delete whole words
    - Add tab completion for paths and nested Lua functions
    - Render command buffer overflow as rows instead of horizontal scrolling
    - Add the ability to paste into the Lua console (from the primary selection area on Linux) with the middle mouse button
  - When popping out scene graph nodes, they will be added to the right side of the screen instead of a floating window (OpenSpace/OpenSpace-WebUI#224)
  - Improving the layout of the time controls in the Night Sky panel to prevent fast time progression from making the elements jump around (OpenSpace/OpenSpace-WebUI#217)
  - Change the default height of targets in the GeoLocation panel to 10 km (OpenSpace/OpenSpace-WebUI#226)


## Content
### New Assets

  - Add new assets for the labels for interstellar objects 1I/'Oumuamua and 2I/Borisov
  - Add new assets for the position, label, and trail for interstellar object 3I/ATLAS
  - Add new asset with action for locking the displayed time of temporal layers (#3760)
  - Add new assets for positions and labels for the Earth-Sun Lagrange point 3 (#2819)
  - Add new asset defining an inertial Moon scene graph node
  - Add new assets to the Digital Universe catalog showing the DESI galaxies and quasars
  - Add new satellite groups available on Celestrak (#4017)
  - Add assets for globe browsing layers previously distributed via Zip files separately from the homepage


### New Maps

  - Use new temporal night time layer on Earth as the previous one was no longer working
  - Added new higher resolution Jupiter texture and made it the default (#3851)
  - Apply the existing New Horizons map as a layer to Pluto and Charon


### Updates to existing Assets/Profiles

  - Update the visibility of nodes that are not focusable or not user-facing to reduce the clutter in the scene menu
  - Use the correct value range for the coloring of the Local Dwarf groups objects
  - The "All globes standard illumination" and "All globes global illumination" will now apply to all globes instead of explicitly mentioned planets and moons in the solar system (#3729)
  - Remove Pluto's trail calculated through Keplerian elements as the new SPICE kernels now reach back to 1549 (#3726)
  - Rename galactic line/band in the Night Sky to equator (#3737)
  - Change asset location, GUI naming, and coloring for 1I/'Oumuamua and 2I/Borisov
  - Various fixes for different example assets
  - Add a Lat/long grid overlay for Earth in the `default` profile (#3059)
  - Increase the maximum tile level for the ESRI World Imagery layer from 19 to 21
  - Corrected start and end times for Voyager 1 & 2
  - Provide `ShadowGroup` for Saturn causing the Moons to cast a shadow onto Saturn
  - Fix spelling mistake in Cutplane Equatorial scene graph node
  - Add the correct scale factors to the Saturn included in the Night Sky profile
  - Made `paleo_map.asset` layers not enabled by default since there are so many of them (#3853)
  - Remove some unused intermediate scene graph nodes (Itokawa, Gaia)
  - Rename the New Horizons Label identifier from  `Labels` to `NewHorizonsLabels`
  - Update various elements of the Apollo photogrammetry models
    - Fixed issue with boulder floating off the heightmap
    - Cleaned up asset to utilize GlobeRotation and remove the extra holder scene graph node
    - Updated shading to make default lighting properties for boulders more match the existing photos (#3843)
  - Add missing caching to the default layer for Callisto (#3863)
  - Add the ability to control the color mapping options of the exoplanet rings (#3845)
  - Move keybind in SolarStorm2012 profile for looping Batsrus model from `B` to `S` (#3886)
  - Added new blend function that is a mixture of a blend and a multiply for layers that provide better blending option for night layers
  - More rigorous handling of which kernel exposes which Spice object to be able to provide more meaningful error messages or error messages at all (#3901)
  - Remove constellation assets that define keybinds and remove predefined keybinds from the SlideDeck asset
  - Remove keybinds from provided profiles
  - **Breaking Change** Remove global openspace bookmarks file. The `localbookmarks` file is split up into  into one for globes and one for stellar positions each with their own CSV   files and formats
    - @TODO: Conversion guide
  - Update the Exoplanets Archive data used in the Exoplanets panel
  - Added WSA version 6.2 to Today's Sun profile (#3932)
  - Make the Pluto trail the same length as the planets and the other dwarf planets (#3952)
  - Update data and add new moons for the minor moons of Jupiter, Saturn, Uranus, and Neptune (#3927)
  - Satellite track requests to Celestrak will now we handled through our own new relay server, which reduce the bandwidth load on the Celestrak servers (#3989)
  - Adjust the URL used to download ISWA data used in the Today's Sun profile (#3992)
  - Cleanup of Asset file locations and separation of asset files into composable parts (#3993)
    - Many assets before defined the object, the trail, sometimes a label and sometimes actions in the same asset, meaning that it was impossible to get, for example, the trail for an   object without also loading the labels. The contents of the following asset groups have been split up. The previous asset is now a "meta" asset that includes the other new asset   files. In many cases this also caused the introduction of a subfolder to hold the new assets (except for regular planets)   For example:  ->  `mars.asset` -> `globe.asset` +   `trail.asset` + `label.asset` + `actions.asset` + `mars.asset` and the new `mars.asset` includes all other four.
      - Dwarf planets (special: If a dwarf planet is specified as a RenderableGlobe, the new asset is `globe.asset`; if it is a model, it is `model.asset`
        - Planets
        - Major and Minor moons of planets
        - The Sun
        - ISS, Hubble, Tiangong, Aqua, SNPP, and Terra
        - Interstellar objects
    - Planet assets no longer implicitly include their trails
    - Some naming harmonization specifically with the dwarf planets to export the objects as their correct name
    - All minor moons for gas planets are now in the `minor` subfolder and each group has received its own subfolder
    - Don't explicitly `Enabled = false` labels, but use `Enabled = asset.enabled` and use the `false` on the meta asset
    - Only use `asset.enabled` in the second-to-last meta asset.  It was causing a lot of warnings otherwise when meta assets (particularly for layers) were included from multiple   places
    - Moving the Server-location detection into all `default_layers.asset`s
    - **Breaking Changes**
      - Scene Graph Nodes
        - Exporting all objects using their Identifier rather than a custom name
        - `ErisGlobe` -> `ErisModel`
        - `GonggongGlobe` -> `Gonggong`
        - `MakemakeGlobe` -> `MakemakeModel`
        - `OrcusGlobe` -> `Orcus`
        - `QuaoarGlobe` -> `Quaoar`
        - `SednaGlobe` -> `Sedna`
      - Asset file locations
        - A _large_ number of assets have changed locations. The most visible changes will be that planets and moons will now be exported through the `/globe.asset`. So any `asset.  require` that used for example `earth/earth` or `mars/mars` before, will now need to use `earth/globe`, `mars/globe`, etc
        - `dwarf_planets/pluto/minor/...` -> `dwarf_planets/pluto/moons/...`
        - `charon` -> `moons/charon`
        - The minor moons for all gas giants are now in the `minor` folder
        - Renamed Deimos and Phobos asset files
  - Add actions and tags to easier show and hide some of the elements in the Night Sky profile (#3998)
  - Disable face culling for some of the educational models that have issues due to single triangle planes
  - Disable face culling for models that have issues (#4022)
  - Remove satellite groups no longer available on Celestrak (#4017)
  - Retire WSA 5.4 Today's Sun assets. Use versionless Today's Sun asset names and update visual tests to target WSA 6.2 data within a valid timeframe (#4028)
  - Update star dataset to include Alcor (#4035)
  - Update SBDB data and change SSSB identifiers (#4041)
    - Add new groups and update files for existing groups
    - Remove unsupported asteroids and comet groupings
    - **Breaking Change** Use capital identifiers for asteroids and comets
  - DU updates for spring 2026 (#4058)
  - Improve the visual look of the Mercury overlay maps by using the new MultiplyMix blend layer (#4075)
  - The `base` asset no longer includes the `base_keybindings`
  - The offline profile now includes the `base_keybindings` (#4076)
  - Convert the usage of TLE to CSV for the generation of a SPICE kernel used for ISS orientation (#4096)
  - Add Artemis 2 assets and include them in the artemis profile (#4099)
  - **Breaking Change** Move existing Artemis 1 assets into a new `artemis` subfolder
  - The `offline` profile now includes the maps for Pluto and Charon


## Content creation

  - Remove enabled property from the video module
  - Improve error message quality for the ShaderPreprocessor
  - Add new ScreenSpaceText objects (#3794)
    - `ScreenSpaceText`: Can be used to print a fixed text onto the screen
    - `ScreenSpaceDate`: Can print the current in-game simulation time to the screen. Uses the same parameters and properties as `DashboardItemDate`
  - Add support for loading compressed `.glb` models
  - The debug axes now use the bounding sphere instead of the interaction sphere for the default size
  - Add the ability to map equirectangular and fisheye images onto `RenderableSphere`s (#3837)
  - Add a new debug property to `RenderableGlobe` to toggle horizon-based culling
  - Make it possible to confiure the level at which the model space rendering switches to camera space rendering per Globe
  - Adding support for the Predictive Science Inc's Magnetohydrodynamic Algorithm outside a Sphere (MAS) simulation to the `RenderableFieldlineSequence` type
  - Add a new task `FindLastClosedFieldlinesTask` and improve the existing `KameleonVolumeToFieldlinesTask` (#3887)
  - **Breaking Change** Make asset path comparison case-insensitive on Windows (#3855)
  - Some obsolete and non-functioning rendering methods in the Gaia module were removed
  - Changed shader uniforms to not begin with a capital letter
  - Add support to provide a table for the `bindKey` function that extracts the Identifier
  - Add parameter for setting the output directory in the `ExoplanetDataPreparationTask` task and create the folder if it does not exist
  - **Breaking Change** Removed the `MieScatteringExtinctionPropCoefficient` parameter from the `RenderableAtmosphere` in favor of writing the correct Rayleigh and Mie scattering   parameters directly
  - Rename SkyBrowser's "Hover Circle" to "Hover Indicator" (#3960)
  - Rename `ScreenshotUseDate` property of `RenderEngine` to `ScreenshotUseDateTime`
  - Make screenshot folder also use seconds in name. Add a new TriggerProperty to cause a new folder to be created
  - Allow specification of filenames when requesting multiple URLs in UrlSynchronization
  - Better guard against missing GP data when loading Kepler position data
  - Remove the `ToyVolume` module
  - Add a warning when the a transition level is requested in the `TileProviderByLevel` that does not exist anywhere in the data
  - Add `LazyLoading` parameters to the `RenderableSphereImageLocal` (#4019) and `ScreenSpaceImageLocal` classes
  - Expose the ability to enable the calibration pattern to the `ScreenSpaceInsetBlackout`
  - Add read only properties for video player playback status (#4031)
  - Add and apply opacity properties for RenderableFov (#4047)
  - Add a more meaningful description for timeframe propertyowners in union
  - Improve the quality of documentation for many numerical properties, providing more range information
  - Print informational messages in shaders even when it is not an error
  - Add the ability to load multiple GP datasets and into the `RenderableOrbitalKepler` class, which get then internally concatenated
  - Add a new feature to invert the size mapping for the `RenderablePointCloud` class (#4107)
  - The NOAA Science-on-a-sphere Blue Marble dataset now also contains two heightmaps for the data


### Lua

  - The `toggleFade` function will no longer report an error if a wildcard or tag matching was requested but no match was found
  - Add new function `profileName` and `profilePath` returning Profile information (#3734)
  - Add support for specifying the format string for the `openspace.time.SPICE()` function
  - Add an additional parameter to the `downloadFile` function to determine if the download should be skipped if the destination file path already exists
  - Add new Lua function `openspace.imageSize` to query size of an image
  - Add new function `loadNavigationStatefromFile` to return the state rather than setting it.
  - Deprecate  `loadNavigationState` in favor of `openspace.navigation.setNavigationState(openspace.navigation.loadNavigationState("<path>"))`  (#3955)


### API

  - Add camera view direction and subsolar coordinates to the information sent by the CameraTopic (#3741)
  - Remove the explicit string-based name for the current OpenSpace version
  - Truck movement and rolls in the Camera API are no longer internally represented as two-dimensional value where one of the dimensions is ignored
  - Remove unused keyframe time reference modes and update the SessionRecording version. All previous SessionRecording files will be automatically converted upon loading
  - Complete overhaul of many Topics that are used by the JSON and Python APIs  (#3896)
  - A new event is now published indicating finishing loading of the profile
  - Update SessionRecording version to write orientation quaternions in the standard (w,x,y,z) order (#3826)
  - Update the Topic, JavaScript, and Python API versions to 1.0.0 (#4055)


## Bug Fixes

  - Force OpenSpace_Helper to the dedicated graphics card. Fixes a crash on laptops
  - Disable uniform location errors for globes when they only have a single solid color (#3728)
  - Fix issue where the incorrect string markers were copied when picking a ScriptLog in the Profile Editor (#3620)
  - Fix issue where the console did not have correct focus when opened (#3649)
  - Fix missing info button for current scene graph node (#3735)
  - Fix issue where a property interpolation would not cause the postscript to be called
  - Fix errors with meta information of profiles (#3743)
  - Fix crash in planets sonification when no planets have been added
  - Disable caching for exoplanet textures that are based on images to prevent warnings when enabling MRF caching
  - Fixes missing calls to `absPath` in the  slidedeck example
  - Fix issue where the `Fade` value wsa not applied for the RenderableGalaxy
  - Fix Sun glare to use the correct billboarding for fisheye rendering
  - Fix min and max values of RenderableModel transform matrix (#3746)
  - Fix issue where the labels component would not load correctly with a path containing path tokens (#3751)
  - Fix issue where the camera would be moved to near-infinity with a blank screen while rotating around Earth (#3497)
  - Remove warning when trying to MRF cache local image files
  - Fix issue with infinite lock in the LuaConsole if the window is minimized while the console is open
  - Remove warnings for missing uniforms in `RenderableGlobe` under some conditions (#3770)
  - Fix issue with the TileProviderByLevel example when no name is specified
  - Fix issue where a model transformation determinant of 0 would cause the rendering of a model to fail (#3177)
  - Fix OpenGL errors being raised when disabling ring shadows when rings were disabled (#3779)
  - Fix identifier for the action to toggle planets and moons that caused it to not function
  - Fix inconsistencies in the fieldline coloring during time changes in the Today's Sun profile (#3786)
  - Symbols in Stacktraces should now be correctly resolved on user machines
  - Fixed incorrect rendering of planet-onto-ring shadows in fisheye projection mode (#3776, #3784)
  - Fix the error being raised when disabling the "Perform Shading" property on Saturn
  - Fixed incorrect path for MPC kepler data causing it to fail to load
  - Remove offset for max chunk level, fixing disappearing height tiles on Earth (#3791)
  - Fix issue where the sandbox permissions for the CEF process were misconfigured on Linux (#3711)
  - Fix issue where the mean motion for the data retrieved from the Minor Planet Center was calculated incorrectly (#3804)
  - Fix issue where specifying a custom `openspace.cfg` configuration file, the `${BASE}` path token will be set to the location of the configuration file instead of the base of the OpenSpace installation (#3806)
  - Fix overdraw issue that caused flickering in `RenderableSphericalGrid` when the opacity was set to a value less than `1`
  - Fix crash that would occur when deinitializing `ScreenSpaceRenderableRenderable`
  - Fix issue where the heightmap of Earth close to the surface would disappear as the max chunk level was miscalculated when no overview was available (#3771)
  - Fix issue where the Sun trail action was using the wrong time (#3848, #3817)
  - Fix issue where the top bar submenus could not be interactecd with on touch screens (#3867)
  - Fix crash that would occur when a session recording includes a malformed `setPropertyValue` call
  - Fix an issue where static transforms would not update correctly when starting OpenSpace with a paused time
  - Fix an issue where the native ImGui slides would not display large value ranges correctly (#3883)
  - Fix issue where the travel speed indicator computation would use the wrong rotation (#3878)
  - Fix issues with the New York-based MOLA layer where the tile pixel size was set incorrectly (#3890)
  - Fix error in offline profile when trying to set SkyBrowser module's Enabled property that no longer exists (#3900)
  - Fix crash that would occur when an asset requires itself. Instead provide an error message
  - Fix issue with the linear path rotation where the rotation would be on an independent timeline from the movement, resulting in weird and unexpected behaviors of the camera (#3913)
  - Fix issue where the `EnableFadeIn` variable for `RenderableStars` was not read from the asset correctly (#3935)
  - Fix issue where you could not play an audio file that has ended without manually stopping it before (#3818)
  - Fix issue with the `ConstructOctreeTask` that would cause it to not detect files correctly
  - Fix crash that occurred when disabling a `RenderableModel` shown inside a `ScreenSpaceRenderableRenderable` (#3976)
  - Fix crash that occurred when trying to load a TLE file that does not exist (#3962)
  - Fix an issue where a `RenderableModel` would not render correctly inside a `ScreenSpaceRenderableRenderable` (#3977)
  - Write an error message when failing to save a session recording (#3830)
  - Prevent crash at shutdown when disabling a server interface
  - Fix issue where the default tab order in the Launcher was wrong
  - Fix incorrect orientation for Apollo15
  - Fix issue where the engine mode was not correctly reset to user control when there was an error loading a session recording causing the application to effectively hang (#3815)
  - Fix issue where setting a path on Windows using `\` in the `openspace.cfg` file would not always work correctly (#3861)
  - Fix issue where the incorrect data mapping name was used to retrieve luminosity values in `RenderableStars` (#3961)
  - Fix an issue that would prevent the application from starting when we should start with the previous profile, but that file had been deleted since the last startup (#4000)
  - Fix a crash when changing the model scale of a `RenderableModel` contained in a `ScreenSpaceRenderableRenderable` (#4002)
  - Fix issue where setting the profile from a command-line option would fail with absolute paths or files with extensions
  - Fix crash that could occur when passing a wrong type into the `setPropertyValue` or `setPropertyValueSingle` functions (#4018)
  - Fixed issue where the Clouds/Magellan Combo layer would not transition correctly (#4024)
  - Prevent crash when specifying a `RenderablePlaneImageLocal` as lazy loading when it starts as being enabled
  - Fix errors that occurd when running actions in the NightSky/Misc asset
  - Fix issue where a saved JSON navigation state was not loadable
  - Fix issues when trying to store setting a `TriggerProperty` in a Session Recording
  - Fix an issue where large number of parameter settings for base classes were not displayed correctly in the documentation
  - Fix an issue where the FITS sphere texture was not refreshing on timestamp changes (#4084)
  - Disable horizon culling by default to fix issue globebrowsing flickering (#4010)
  - Fix URL for the `lo_mr_mosaic_newyork.wms` that would cause the data to not load correctly (#4057)
  - Fix issue with RenderableTravelSpeed indicator showing wrong positions with high delta time (#3898)
  - Fix issue where removing an asset that owned an PropertyOwner which had one of its properties currently being interpolated would cause a crash (#4092)
  - Fix an issue where unloading an image that was loaded lazily was not actually unloaded (#4073)
  - Launcher fixes (#4086)
    - Fix issue where new "apply-without-saving" config did not properly get selected after creation
    - Fix issue where profiles and configs showed full file path or variable expansion path instead of name in the launcher GUI
    - Fix issue where tooltip displayed empty box
  - Fix issue where the `PlayAudio` parameter for video files was not extracted correctly from the asset files
  - Fix issue that sometimes could lead to a crash when removing an asset that contains a video
  - Fix crash when calling the `saveSettingsToProfile` function (#4101)
  - Fix issue where the Display copies of the SkyBrowser were not treated correctly when opening or closing the GUI panel (OpenSpace/OpenSpace-WebUI#200)
  - Add aria labels to UI components that were missing in a number of places (OpenSpace/OpenSpace-WebUI#203)
  - Fix an issue with default minRange for minMax range that would cause different properties to be linked (#3914)
  - Fix an issue with the user interface when removing a globe layer (#3790)
  - Fix issue where an overflowing long list in the user interface would not show the scrollbar (#3821)
  - Fix broken search button in the GeoLocation panel and do not clear search on blur (OpenSpace/OpenSpace-WebUI#218)
  - Fix issue where the meta documentation for an asset loaded at runtime was not displayed correctly (#3911)
  - Fix issue where manually typing a SessionRecording filename into the user interface would cause the last character of the filename to be dropped
  - Fix issue where a shader error in an included shader file would cause the file path to grow unlimited and fill the log and cause a crash
  - Fix an issue in the SGCT FontManager that could cause some font paths to not resolve correctly on Windows (SGCT/SGCT#114)
  - Fix an issue that would cause the Scalable mesh files from being read correctly (SGCT/SGCT#120)
  - Fix an issue where the rendering would freeze when providing 0 or negative capture threads for screenshot generation (SGCT/SGCT#121)
  - Fix an issue where some UI elements were not disabled correctly during automatic camera movements or session recordering playback (OpenSpace/OpenSpace-WebUI#175)
  - Fix errors when loading the Euclid, JWST, and Messenger profiles
  - Fix an issue where the info box in the user interface was not scrollable, leading to long texts breaking the layouting (OpenSpace/OpenSpace-WebUI#225)
  - Fix an issue where the CEF cache was left in an unusable state, preventing the application from starting again. The CEF cache is now deleted at every startup


## Breaking Changes
@TODO at the end
  - RenderableAtmosphere's `MieScatteringExtinctionPropCoefficient` is now called `MieScatteringExtinctionPropCoefficient`
