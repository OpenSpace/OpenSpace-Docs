# Image Testing
OpenSpace is using an image-based regression testing on the backend. Its two main goals are to (a) prevent code changes accidentally affecting the visualization and (b) generating screenshots for use in the documentation that keep up to date with the current OpenSpace version.


## Server
The generated images are available at [https://regression.openspaceproject.com](https://regression.openspaceproject.com).

Each test has a _Name_ and multiple tests are combined into a _Group_. The name of the group is unique and within a group, each test has a unique name. Each test has one _Reference Image_, which is the approved state of that rendering. Each time the tests are run, a new _Candidate Image_ is created which is compared against the _Reference Image_ to create a _Difference Image_. The _Difference Image_ shows the pixels that are different in red and the pixels that are the same in white. The perceptual change between the _Reference_ and _Candidate_ image is reported as an error percentage.

Additionally, each test also reports how long it took to run the test, as well as the access to the OpenSpace log file that was generated when running the test.

Here are examples of how the three image types look like:

:::{figure} example_candidate.png
:align: center
:width: 540px
The candidate image for example test
:::

:::{figure} example_reference.png
:align: center
:width: 540px
The reference image for example test
:::

:::{figure} example_difference.png
:align: center
:width: 540px
The difference image for example test
:::


## Local testing
All image tests should be tested manually before committing them into the repository. See the [OpenSpace-VisualTesting](https://github.com/OpenSpace/OpenSpace-VisualTesting) repository's README for more information on how to use the _Runner_ application to run individual tests locally. The Runner will execute the test and save the rendered screenshot locally in a `test` folder. The screenshot should correspond to the result that the test is supposed to create.


## Test Files
The image test files are located in the `visualtests` folder in the main OpenSpace repository. The regression server will automatically run through all tests that are contained in this folder.

The files are organized in folders, where the folder names are used as the _Group_ name for the tests within, and the filename of each test (without the `.ostest` extension) is used as the _Name_ of the test. Each folder can contain additional subfolders. The top-level folders are predetermined based on what the tests will be used for:

  - `documentation`: Files that generate images used for the documentation page

    Files in this folder are sorted based on the location in the documentation where they are used. For example, images that are used in the Dawn profile should be placed in `profiles/dawn/name.png`

  - `profiles`: Integration test files that verify individual views for the different profiles

    All tests belonging to a specific profile should be grouped into a subfolder with the profiles name. If possible, as many of the visible elements of the profiles should be tested.

  - `example`: Tests using the individual example asset files from the data/assets folder

    The subfolders in this folder should be organized to mimick the folder structure of `data/assets/examples` exactly, including that the test of a specific example asset must be named identical to the filename of the example asset. For example the test for `data/assets/examples/rotation/globerotation/globe.asset` should be placed in `visualtests/example/rotation/globerotation/globe.ostest`

  - `misc`: Other tests that are testing various pieces of the rendering

    In this folder, common sense should be used to group tests into reasonable categories.

Top-level folders should generally only be added sparingly and tests that do not fit any of the other tests, should be placed in the `misc` folder with a properly named subfolder first.

:::{important}
If at all possible, it should be avoided to move or rename tests as third-party users might depend on the URL of the location. In particular all of the tests included in the `documentation` folder must be verified in the documentation repository and all links must be updated.
:::


## Test Structure
`.ostest` files are JSON files that describe the different ordered instructions for the regression server. All available actions are described in detail further below in this document. There is also a Python-based wizard that can be used to interactively generated `.ostest` files, which is also described below.

Each test must have a `screenshot` instruction as the **last** entry, which causes an image to be created that is used as the result of the test. Only exactly one `screenshot` instruction per test is currently supported. Each `.ostest` file is a JSON file with two top-level keys: `profile` provides the name of the profile that should be loaded before running these test instructions, and `commands` is a list of instructions that should be executed after the profile is loaded. All instructions must have a `type` and `value` key to determine which type of instruction it is and the parameters for that instruction.

:::{important}
By default on the servers that generate tests for [https://regression.openspaceproject.com](https://regression.openspaceproject.com), all tests always start paused, MRF caching is enabled, and the user interface and dashboard items are disabled.

That means it is not necessary to explicitly add instructions for these changes.
:::

### Best practices
  - All tests should start with the instruction to set a specific time to improve reproducibility
  - The fewer instructions there are per test, the better
  - Adding `wait` instructions to ensure OpenSpace has time to load dynamic datasets increases reliability, but too many `wait`s will slow down the overall testing
  - Avoid `recording` instructions and use `navigationstate` instead
  - Avoid `script` if possible and use dedicated instructions when they exist. If we see the same `script` instruction used in several tests, they can be upgraded to a dedicated instruction at a later stage

### Instructions
:::
{.glossary .index-list}
`action`
: Triggers an action that must already be defined in the profile or previously defined in the test. The provided value must be a string that is the identifier of the action that should be triggered.
:
: Example: `{ "type": "action", "value": "os.FadeDownTrails" }`
: Lua scripting equivalent: `openspace.action.triggerAction`

`asset`
: Loads a given asset file. The provided value must be a string that is the path to the asset file to be loaded. This is specified relative to the `data/asset` folder inside OpenSpace.
:
: Example: `{ "type": "asset", "value": "path/to/file.asset" }`
: Lua scripting equivalent: `openspace.asset.add`

`deltatime`
: Instantly changes the delta time in OpenSpace to the provided value. The provided value must be a number that is the delta time in seconds per real-time second that the engine should be set to.
:
: Example: `{ "type": "deltatime", "value": 10 }`
:
: Lua scripting equivalent: `openspace.time.setDeltaTime`

`navigationstate`
: Instantly moves the camera to the provided navigation state. The provided value must be an object that must contain at least an `anchor` and `position` key and may optionally contain the keys `aim`, `referenceFrame`, `up`, `yaw`, `pitch`, and `timestamp`. All these values are then used to instantaneously set the position and rotation of the camera.
:
: Example: `{ "type": "navigationstate", "value": { "anchor": "Juno", "pitch": -0.0165756, "position": [ -22.49081, 1.191533, 26.35740 ], "up": [ 0.0288083, 0.999373, -0.0205962 ], "yaw": 0.152454 } }`
:
: Lua scripting equivalent: `openspace.navigation.setNavigationState`

`pause`
: Determines whether the in-game clock should be paused or resumed. The provided value must be a boolean that is the clock state after the instruction.
:
: Example: `{ "type": "pause", "value": false }`
:
: Lua scripting equivalent: `openspace.time.setPause`

`property`
: Instantly sets a specific property or group of properties to the specified value. The provided value must be an object containing another `property` and `value` key. The (other) `property` key is the identifier or regex for the property or properties that should be set. The (other) `value` key is the new value for the property where the type must match the (other) `property`.
:
: Example: `{ "type": "property", "value": { "property": "Scene.Constellations.Renderable.Enabled", "value": true } }`
:
: Lua scripting equivalent: `openspace.setPropertyValue`

`recording`
: Triggers the playback of a session recording. The provided value is the name of the session recording file that should be played.
:
: Example: `{ "type": "recording", "value": "solarsystem.osrec" }`
:
: Lua scripting equivalent: `openspace.sessionRecording.startPlayback`

`screenshot`
: Takes a screenshot of the application. At the moment, there can be only exactly one instruction of this type and it must be the last instruction in the test. This instruction is the only one to not use the `value` key.
:
: Example: `{ "type": "screenshot" }`
:
: Lua scripting equivalent: `openspace.takeScreenshot`

`script`
: Instantly executes the script that is passed in as a value. That value must be a string that is the Lua script to execute.
:
: Example: `{ "type": "script", "value": "openspace.printError('Hello world')" }`
:
: Lua scripting equivalent: `value`

`time`
: Sets the in-game time to the provided value. The value can be either a string, which needs to be a valid date-time string, or a number, which represents the number of seconds past the J2000 epoch.
:
: Example: `{ "type": "time", "value": "2016-07-01T00:00:01.00" }`
:
: Lua scripting equivalent: `openspace.time.setTime`

`wait`
: Causes the test to wait for the specified number of seconds. Note that the OpenSpace testing instance is still running in the background and is, for example continuing to load dynamic content while the test is waiting.
:
: Example: `{ "type": "wait", "value": 2 }`
:
: Lua scripting equivalent: none
:::


## Wizard
The main OpenSpace repository contains a wizard that helps with creating `.ostest` files. The wizard is located in `support/testwizard` and requires a working Python installation on the system. First, the necessary packages need to be installed by running `pip install -r requirements.txt` from that folder. Before running the wizard, OpenSpace needs to be started with the profile for which a test should be created. Then, the wizard is run by `python main.py` which starts an interactive shell.

When starting, the wizard will provide information about the different instructions that can be added and then ask for the name of the test, which will become the filename for the `.ostest` file. After that, the wizard will ask for instructions to add to the test. The general workflow is to set up changes in the running OpenSpace version and then pick the instruction in the wizard which will retrieve the necessary information from the running OpenSpace instance. For cases where that is not possible, the wizard will ask for additional input when the instruction was selected.

To finalize the test, no instruction should be selected, which will in turn automatically add a `screenshot` instruction and write the finished test to disk under the name provided in the first prompt.
