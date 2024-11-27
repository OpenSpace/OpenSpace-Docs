# `openspace`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`absPath`](#absPath-target)
    - [Passes the argument to FileSystem::absolutePath, which resolves occuring path tokens and returns the absolute path]{#absPath-list}


*   - [`addCustomProperty`](#addCustomProperty-target)
    - [Creates a new property that lives in the `UserProperty` group]{#addCustomProperty-list}


*   - [`addSceneGraphNode`](#addSceneGraphNode-target)
    - [Loads the SceneGraphNode described in the table and adds it to the SceneGraph]{#addSceneGraphNode-list}


*   - [`addScreenSpaceRenderable`](#addScreenSpaceRenderable-target)
    - [/ Will create a ScreenSpaceRenderable from a lua Table and add it in the RenderEngine]{#addScreenSpaceRenderable-list}


*   - [`addTag`](#addTag-target)
    - [Adds a Tag to a SceneGraphNode identified by the provided uri]{#addTag-list}


*   - [`addToPropertyValue`](#addToPropertyValue-target)
    - [Add a value to the property with the given identifier]{#addToPropertyValue-list}


*   - [`appendToListProperty`](#appendToListProperty-target)
    - [Add a value to the list property with the given identifier]{#appendToListProperty-list}


*   - [`bindKey`](#bindKey-target)
    - [Binds a key to Lua command to both execute locally and broadcast to all clients if this node is hosting a parallel connection]{#bindKey-list}


*   - [`boundingSphere`](#boundingSphere-target)
    - [Returns the bounding sphere of the scene graph node with the given string as identifier]{#boundingSphere-list}


*   - [`clearKey`](#clearKey-target)
    - [Unbinds the key or keys that have been provided]{#clearKey-list}


*   - [`clearKeys`](#clearKeys-target)
    - [Clear all key bindings]{#clearKeys-list}


*   - [`configuration`](#configuration-target)
    - [Returns the whole configuration object as a Dictionary]{#configuration-list}


*   - [`createDirectory`](#createDirectory-target)
    - [Creates a directory at the provided path, returns true if directory was newly created and false otherwise]{#createDirectory-list}


*   - [`createSingleColorImage`](#createSingleColorImage-target)
    - [Creates a 1 pixel image with a certain color in the cache folder and returns the path to the file]{#createSingleColorImage-list}


*   - [`directoryExists`](#directoryExists-target)
    - [Checks whether the provided directory exists]{#directoryExists-list}


*   - [`directoryForPath`](#directoryForPath-target)
    - [This function extracts the directory part of the passed path]{#directoryForPath-list}


*   - [`downloadFile`](#downloadFile-target)
    - [Downloads a file from Lua interpreter]{#downloadFile-list}


*   - [`dpiScaling`](#dpiScaling-target)
    - [Extracts the DPI scaling for either the GUI window or if there is no dedicated GUI window, the first window]{#dpiScaling-list}


*   - [`fadeIn`](#fadeIn-target)
    - [Fades in the node(s) with the given identifier over the given time in seconds]{#fadeIn-list}


*   - [`fadeOut`](#fadeOut-target)
    - [Fades out the node(s) with the given identifier over the given time in seconds]{#fadeOut-list}


*   - [`fileExists`](#fileExists-target)
    - [Checks whether the provided file exists]{#fileExists-list}


*   - [`getProperty`](#getProperty-target)
    - [Returns a list of property identifiers that match the passed regular expression]{#getProperty-list}


*   - [`getPropertyValue`](#getPropertyValue-target)
    - [Returns the value the property, identified by the provided URI]{#getPropertyValue-list}


*   - [`hasMission`](#hasMission-target)
    - [Returns whether a mission with the provided name has been loaded]{#hasMission-list}


*   - [`hasProperty`](#hasProperty-target)
    - [Returns whether a property with the given URI exists]{#hasProperty-list}


*   - [`hasSceneGraphNode`](#hasSceneGraphNode-target)
    - [Checks whether the specifies SceneGraphNode is present in the current scene]{#hasSceneGraphNode-list}


*   - [`interactionSphere`](#interactionSphere-target)
    - [Returns the interaction sphere of the scene graph node with the given string as identifier]{#interactionSphere-list}


*   - [`invertBooleanProperty`](#invertBooleanProperty-target)
    - [Inverts the value of a boolean property with the given identifier]{#invertBooleanProperty-list}


*   - [`isMaster`](#isMaster-target)
    - [Returns whether the current OpenSpace instance is the master node of a cluster configuration]{#isMaster-list}


*   - [`keyBindings`](#keyBindings-target)
    - [Returns the strings of the script that are bound to the passed key and whether they were local or remote key binds]{#keyBindings-list}


*   - [`layerServer`](#layerServer-target)
    - [Returns the current layer server from the configuration]{#layerServer-list}


*   - [`loadJson`](#loadJson-target)
    - [Loads the provided JSON file and returns it back to the caller]{#loadJson-list}


*   - [`loadMission`](#loadMission-target)
    - [Load mission phases from file]{#loadMission-list}


*   - [`makeIdentifier`](#makeIdentifier-target)
    - [Create a valid identifier from the provided input string]{#makeIdentifier-list}


*   - [`markInterestingNodes`](#markInterestingNodes-target)
    - [This function marks the scene graph nodes identified by name as interesting, which will provide shortcut access to focus buttons and featured properties]{#markInterestingNodes-list}


*   - [`markInterestingTimes`](#markInterestingTimes-target)
    - [This function marks interesting times for the current scene, which will create shortcuts for a quick access]{#markInterestingTimes-list}


*   - [`nodeByRenderableType`](#nodeByRenderableType-target)
    - [Returns a list of all scene graph nodes in the scene that have a renderable of the specific type]{#nodeByRenderableType-list}


*   - [`printDebug`](#printDebug-target)
    - [Logs the passed value to the installed LogManager with a LogLevel of 'Debug']{#printDebug-list}


*   - [`printError`](#printError-target)
    - [Logs the passed value to the installed LogManager with a LogLevel of 'Error']{#printError-list}


*   - [`printFatal`](#printFatal-target)
    - [Logs the passed value to the installed LogManager with a LogLevel of 'Fatal']{#printFatal-list}


*   - [`printInfo`](#printInfo-target)
    - [Logs the passed value to the installed LogManager with a LogLevel of 'Info']{#printInfo-list}


*   - [`printTrace`](#printTrace-target)
    - [Logs the passed value to the installed LogManager with a LogLevel of 'Trace']{#printTrace-list}


*   - [`printWarning`](#printWarning-target)
    - [Logs the passed value to the installed LogManager with a LogLevel of 'Warning']{#printWarning-list}


*   - [`property`](#property-target)
    - [Returns a list of property identifiers that match the passed regular expression]{#property-list}


*   - [`propertyValue`](#propertyValue-target)
    - [Returns the value the property, identified by the provided URI]{#propertyValue-list}


*   - [`readCSVFile`](#readCSVFile-target)
    - [Loads the CSV file provided as a parameter and returns it as a vector containing the values of the each row]{#readCSVFile-list}


*   - [`readFile`](#readFile-target)
    - [Reads a file from disk and return its contents]{#readFile-list}


*   - [`rebindKey`](#rebindKey-target)
    - [Rebinds all scripts from the old key (first argument) to the new key (second argument)]{#rebindKey-list}


*   - [`removeCustomProperty`](#removeCustomProperty-target)
    - []{#removeCustomProperty-list}


*   - [`removeInterestingNodes`](#removeInterestingNodes-target)
    - [This function removes unmarks the scene graph nodes identified by name as interesting, thus removing the shortcuts from the features properties list]{#removeInterestingNodes-list}


*   - [`removeSceneGraphNode`](#removeSceneGraphNode-target)
    - [Removes the SceneGraphNode identified by name or by extracting the 'Identifier' key if the parameter is a table]{#removeSceneGraphNode-list}


*   - [`removeSceneGraphNodesFromRegex`](#removeSceneGraphNodesFromRegex-target)
    - [Removes all SceneGraphNodes with identifiers matching the input regular expression]{#removeSceneGraphNodesFromRegex-list}


*   - [`removeScreenSpaceRenderable`](#removeScreenSpaceRenderable-target)
    - [Given a ScreenSpaceRenderable name this script will remove it from the RenderEngine]{#removeScreenSpaceRenderable-list}


*   - [`removeTag`](#removeTag-target)
    - [Removes a tag (second argument) from a scene graph node (first argument)]{#removeTag-list}


*   - [`resetCamera`](#resetCamera-target)
    - [Resets the camera position to the same position where the profile originally started]{#resetCamera-list}


*   - [`resetScreenshotNumber`](#resetScreenshotNumber-target)
    - [Reset screenshot index to 0]{#resetScreenshotNumber-list}


*   - [`saveSettingsToProfile`](#saveSettingsToProfile-target)
    - [Collects all changes that have been made since startup, including all property changes and assets required, requested, or removed]{#saveSettingsToProfile-list}


*   - [`sceneGraphNodes`](#sceneGraphNodes-target)
    - [Returns a list of all scene graph nodes in the scene]{#sceneGraphNodes-list}


*   - [`screenSpaceRenderables`](#screenSpaceRenderables-target)
    - [Returns a list of all screen-space renderables]{#screenSpaceRenderables-list}


*   - [`setCurrentMission`](#setCurrentMission-target)
    - [Set the currnet mission]{#setCurrentMission-list}


*   - [`setDefaultDashboard`](#setDefaultDashboard-target)
    - [This function sets the default values for the dashboard consisting of 'DashboardItemDate', 'DashboardItemSimulationIncrement', 'DashboardItemDistance', 'DashboardItemFramerate', and 'DashboardItemParallelConnection']{#setDefaultDashboard-list}


*   - [`setDefaultGuiSorting`](#setDefaultGuiSorting-target)
    - [This function sets the default GUI sorting for the space environment to increasing size, from solar system, through Milky Way, Universe and finishing with other elements]{#setDefaultGuiSorting-list}


*   - [`setParent`](#setParent-target)
    - [The scene graph node identified by the first string is reparented to be a child of the scene graph node identified by the second string]{#setParent-list}


*   - [`setPathToken`](#setPathToken-target)
    - [Registers the path token provided by the first argument to the path in the second argument]{#setPathToken-list}


*   - [`setPropertyValue`](#setPropertyValue-target)
    - [Sets all property(s) identified by the URI (with potential wildcards) in the first argument]{#setPropertyValue-list}


*   - [`setPropertyValueSingle`](#setPropertyValueSingle-target)
    - [Sets the property identified by the URI in the first argument]{#setPropertyValueSingle-list}


*   - [`setScreenshotFolder`](#setScreenshotFolder-target)
    - [Sets the folder used for storing screenshots or session recording frames]{#setScreenshotFolder-list}


*   - [`takeScreenshot`](#takeScreenshot-target)
    - [Take a screenshot and return the screenshot number]{#takeScreenshot-list}


*   - [`toggleFade`](#toggleFade-target)
    - [Toggles the fade state of the node(s) with the given identifier over the given
          time in seconds]{#toggleFade-list}


*   - [`toggleShutdown`](#toggleShutdown-target)
    - [Toggles the shutdown mode that will close the application after the countdown timer is reached]{#toggleShutdown-list}


*   - [`unloadMission`](#unloadMission-target)
    - [Unloads a previously loaded mission]{#unloadMission-list}


*   - [`unzipFile`](#unzipFile-target)
    - [This function extracts the contents of a zip file]{#unzipFile-list}


*   - [`version`](#version-target)
    - [This function returns information about the current OpenSpace version]{#version-list}


*   - [`walkDirectory`](#walkDirectory-target)
    - [Walks a directory and returns the contents of the directory as absolute paths]{#walkDirectory-list}


*   - [`walkDirectoryFiles`](#walkDirectoryFiles-target)
    - [Walks a directory and returns the files of the directory as absolute paths]{#walkDirectoryFiles-list}


*   - [`walkDirectoryFolders`](#walkDirectoryFolders-target)
    - [Walks a directory and returns the subfolders of the directory as absolute paths]{#walkDirectoryFolders-list}


*   - [`worldPosition`](#worldPosition-target)
    - [Returns the world position of the scene graph node with the given string as identifier]{#worldPosition-list}


*   - [`worldRotation`](#worldRotation-target)
    - [Returns the world rotation matrix of the scene graph node with the given string as identifier]{#worldRotation-list}


*   - [`writeDocumentation`](#writeDocumentation-target)
    - [Writes out documentation files]{#writeDocumentation-list}

:::

## Functions

(absPath-target)=
### [`absPath`](#absPath-list)
Passes the argument to FileSystem::absolutePath, which resolves occuring path tokens and returns the absolute path.


:::{card} Parameters


* path `String` 


:::

Return type: `Path` 

:::{code-block} lua
:caption: Signature
openspace.absPath(path)
:::
___

(addCustomProperty-target)=
### [`addCustomProperty`](#addCustomProperty-list)
Creates a new property that lives in the `UserProperty` group.


:::{card} Parameters


* identifier `String` 


    * The identifier that is going to be used for the new property 

* type `CustomPropertyType` 


    * The type of the property, has to be one of \"DMat2Property\", \"DMat3Property\", \"DMat4Property\", \"Mat2Property\", \"Mat3Property\", \"Mat4Property\", \"BoolProperty\", \"DoubleProperty\", \"FloatProperty\", \"IntProperty\", \"StringProperty\", \"StringListProperty\", \"LongProperty\", \"ShortProperty\", \"UIntProperty\", \"ULongProperty\", \"DVec2Property\", \"DVec3Property\", \"DVec4Property\", \"IVec2Property\", \"IVec3Property\", \"IVec4Property\", \"UVec2Property\", \"UVec3Property\", \"UVec4Property\", \"Vec2Property\", \"Vec3Property\", \"Vec4Property\" 

* guiName `String?` 


    * The name that the property uses in the user interface. If this value is not provided, the `identifier` is used instead 

* description `String?` 


    * A description what the property is used for 

* onChange `String?` 


    * A Lua script that will be executed whenever the property changes
:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.addCustomProperty(identifier, type, guiName, description, onChange)
:::
___

(addSceneGraphNode-target)=
### [`addSceneGraphNode`](#addSceneGraphNode-list)
Loads the SceneGraphNode described in the table and adds it to the SceneGraph.


:::{card} Parameters


* node `Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.addSceneGraphNode(node)
:::
___

(addScreenSpaceRenderable-target)=
### [`addScreenSpaceRenderable`](#addScreenSpaceRenderable-list)
/ Will create a ScreenSpaceRenderable from a lua Table and add it in the RenderEngine


:::{card} Parameters


* screenSpace `Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.addScreenSpaceRenderable(screenSpace)
:::
___

(addTag-target)=
### [`addTag`](#addTag-list)
Adds a Tag to a SceneGraphNode identified by the provided uri


:::{card} Parameters


* uri `String` 



* tag `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.addTag(uri, tag)
:::
___

(addToPropertyValue-target)=
### [`addToPropertyValue`](#addToPropertyValue-list)
Add a value to the property with the given identifier. Works on both numerical and string properties, where adding to a string property means appending the given string value to the existing string value.


:::{card} Parameters


* identifier `String` 



* value `String | Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.addToPropertyValue(identifier, value)
:::
___

(appendToListProperty-target)=
### [`appendToListProperty`](#appendToListProperty-list)
Add a value to the list property with the given identifier. The value can be any type, as long as it is the correct type for the given property. Note that a number will be converted to a string automatically.


:::{card} Parameters


* identifier `String` 



* value `any` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.appendToListProperty(identifier, value)
:::
___

(bindKey-target)=
### [`bindKey`](#bindKey-list)
Binds a key to Lua command to both execute locally and broadcast to all clients if this node is hosting a parallel connection.


:::{card} Parameters


* key `String` 



* action `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.bindKey(key, action)
:::
___

(boundingSphere-target)=
### [`boundingSphere`](#boundingSphere-list)
Returns the bounding sphere of the scene graph node with the given string as identifier.


:::{card} Parameters


* identifier `String` 


:::

Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.boundingSphere(identifier)
:::
___

(clearKey-target)=
### [`clearKey`](#clearKey-list)
Unbinds the key or keys that have been provided. This function can be called with a single key or with an array of keys to remove all of the provided keys at once.


:::{card} Parameters


* key `String | String[]` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.clearKey(key)
:::
___

(clearKeys-target)=
### [`clearKeys`](#clearKeys-list)
Clear all key bindings


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.clearKeys()
:::
___

(configuration-target)=
### [`configuration`](#configuration-list)
Returns the whole configuration object as a Dictionary


Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.configuration()
:::
___

(createDirectory-target)=
### [`createDirectory`](#createDirectory-list)
Creates a directory at the provided path, returns true if directory was newly created and false otherwise. If `recursive` flag is set to true, it will automatically create any missing parent folder as well


:::{card} Parameters


* path `Path` 



* recursive `Boolean?` - Default value: `false` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.createDirectory(path, recursive)
:::
___

(createSingleColorImage-target)=
### [`createSingleColorImage`](#createSingleColorImage-list)
Creates a 1 pixel image with a certain color in the cache folder and returns the path to the file. If a cached file with the given name already exists, the path to that file is returned. The first argument is the name of the file, without extension. The second is the RGB color, given as {r, g, b} with values between 0 and 1.


:::{card} Parameters


* name `String` 



* color `vec3` 


:::

Return type: `Path` 

:::{code-block} lua
:caption: Signature
openspace.createSingleColorImage(name, color)
:::
___

(directoryExists-target)=
### [`directoryExists`](#directoryExists-list)
Checks whether the provided directory exists.


:::{card} Parameters


* file `Path` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.directoryExists(file)
:::
___

(directoryForPath-target)=
### [`directoryForPath`](#directoryForPath-list)
This function extracts the directory part of the passed path. For example, if the parameter is 'C:\\\\OpenSpace\\\\foobar\\\\foo.txt', this function returns 'C:\\\\OpenSpace\\\\foobar'.


:::{card} Parameters


* file `Path` 


:::

Return type: `Path` 

:::{code-block} lua
:caption: Signature
openspace.directoryForPath(file)
:::
___

(downloadFile-target)=
### [`downloadFile`](#downloadFile-list)
Downloads a file from Lua interpreter


:::{card} Parameters


* url `String` 



* savePath `String` 



* waitForCompletion `Boolean?` - Default value: `false` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.downloadFile(url, savePath, waitForCompletion)
:::
___

(dpiScaling-target)=
### [`dpiScaling`](#dpiScaling-list)
Extracts the DPI scaling for either the GUI window or if there is no dedicated GUI window, the first window.


Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.dpiScaling()
:::
___

(fadeIn-target)=
### [`fadeIn`](#fadeIn-list)
Fades in the node(s) with the given identifier over the given time in seconds. The identifier can contain a tag and/or a wildcard to target several nodes. If the fade time is not provided then the 'OpenSpaceEngine.FadeDuration' property will be used instead. If the third argument (endScript) is provided then that script will be run after the fade is finished.


:::{card} Parameters


* identifier `String` 



* fadeTime `Number?` 



* endScript `String?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.fadeIn(identifier, fadeTime, endScript)
:::
___

(fadeOut-target)=
### [`fadeOut`](#fadeOut-list)
Fades out the node(s) with the given identifier over the given time in seconds. The identifier can contain a tag and/or a wildcard to target several nodes. If the fade time is not provided then the 'OpenSpaceEngine.FadeDuration' property will be used instead. If the third argument (endScript) is provided then that script will be run after the fade is finished.


:::{card} Parameters


* identifier `String` 



* fadeTime `Number?` 



* endScript `String?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.fadeOut(identifier, fadeTime, endScript)
:::
___

(fileExists-target)=
### [`fileExists`](#fileExists-list)
Checks whether the provided file exists.


:::{card} Parameters


* file `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.fileExists(file)
:::
___

(getProperty-target)=
### [`getProperty`](#getProperty-list)
Returns a list of property identifiers that match the passed regular expression


:::{card} Parameters


* regex `String` 


:::

Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.getProperty(regex)
:::
___

(getPropertyValue-target)=
### [`getPropertyValue`](#getPropertyValue-list)
Returns the value the property, identified by the provided URI. Deprecated in favor of the 'propertyValue' function


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.getPropertyValue()
:::
___

(hasMission-target)=
### [`hasMission`](#hasMission-list)
Returns whether a mission with the provided name has been loaded.


:::{card} Parameters


* missionName `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.hasMission(missionName)
:::
___

(hasProperty-target)=
### [`hasProperty`](#hasProperty-list)
Returns whether a property with the given URI exists


:::{card} Parameters


* uri `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.hasProperty(uri)
:::
___

(hasSceneGraphNode-target)=
### [`hasSceneGraphNode`](#hasSceneGraphNode-list)
Checks whether the specifies SceneGraphNode is present in the current scene.


:::{card} Parameters


* nodeName `String` 


:::

Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.hasSceneGraphNode(nodeName)
:::
___

(interactionSphere-target)=
### [`interactionSphere`](#interactionSphere-list)
Returns the interaction sphere of the scene graph node with the given string as identifier.


:::{card} Parameters


* identifier `String` 


:::

Return type: `Number` 

:::{code-block} lua
:caption: Signature
openspace.interactionSphere(identifier)
:::
___

(invertBooleanProperty-target)=
### [`invertBooleanProperty`](#invertBooleanProperty-list)
Inverts the value of a boolean property with the given identifier


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.invertBooleanProperty(identifier)
:::
___

(isMaster-target)=
### [`isMaster`](#isMaster-list)
Returns whether the current OpenSpace instance is the master node of a cluster configuration. If this instance is not part of a cluster, this function also returns 'true'.


Return type: `Boolean` 

:::{code-block} lua
:caption: Signature
openspace.isMaster()
:::
___

(keyBindings-target)=
### [`keyBindings`](#keyBindings-list)
Returns the strings of the script that are bound to the passed key and whether they were local or remote key binds.


:::{card} Parameters


* key `String` 


:::

Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.keyBindings(key)
:::
___

(layerServer-target)=
### [`layerServer`](#layerServer-list)
Returns the current layer server from the configuration


Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.layerServer()
:::
___

(loadJson-target)=
### [`loadJson`](#loadJson-list)
Loads the provided JSON file and returns it back to the caller. Please note that if the JSON contains keys that array of an array type, they are converted into a Dictionary with numerical keys and the numerical keys start with 1.


:::{card} Parameters


* path `Path` 


:::

Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.loadJson(path)
:::
___

(loadMission-target)=
### [`loadMission`](#loadMission-list)
Load mission phases from file.


:::{card} Parameters


* mission `Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.loadMission(mission)
:::
___

(makeIdentifier-target)=
### [`makeIdentifier`](#makeIdentifier-list)
Create a valid identifier from the provided input string. Will replace invalid characters like whitespaces and some punctuation marks with valid alternatives


:::{card} Parameters


* input `String` 


:::

Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.makeIdentifier(input)
:::
___

(markInterestingNodes-target)=
### [`markInterestingNodes`](#markInterestingNodes-list)
This function marks the scene graph nodes identified by name as interesting, which will provide shortcut access to focus buttons and featured properties


:::{card} Parameters


* sceneGraphNodes `String[]` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.markInterestingNodes(sceneGraphNodes)
:::
___

(markInterestingTimes-target)=
### [`markInterestingTimes`](#markInterestingTimes-list)
This function marks interesting times for the current scene, which will create shortcuts for a quick access


:::{card} Parameters


* times `Table[]` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.markInterestingTimes(times)
:::
___

(nodeByRenderableType-target)=
### [`nodeByRenderableType`](#nodeByRenderableType-list)
Returns a list of all scene graph nodes in the scene that have a renderable of the specific type


:::{card} Parameters


* type `String` 


:::

Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.nodeByRenderableType(type)
:::
___

(printDebug-target)=
### [`printDebug`](#printDebug-list)
Logs the passed value to the installed LogManager with a LogLevel of 'Debug'. For Boolean, numbers, and strings, the internal values are printed, for all other types, the type is printed instead


:::{card} Parameters


* Unnamed parameter of type *


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.printDebug()
:::
___

(printError-target)=
### [`printError`](#printError-list)
Logs the passed value to the installed LogManager with a LogLevel of 'Error'. For Boolean, numbers, and strings, the internal values are printed, for all other types, the type is printed instead


:::{card} Parameters


* Unnamed parameter of type *


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.printError()
:::
___

(printFatal-target)=
### [`printFatal`](#printFatal-list)
Logs the passed value to the installed LogManager with a LogLevel of 'Fatal'. For Boolean, numbers, and strings, the internal values are printed, for all other types, the type is printed instead


:::{card} Parameters


* Unnamed parameter of type *


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.printFatal()
:::
___

(printInfo-target)=
### [`printInfo`](#printInfo-list)
Logs the passed value to the installed LogManager with a LogLevel of 'Info'. For Boolean, numbers, and strings, the internal values are printed, for all other types, the type is printed instead


:::{card} Parameters


* Unnamed parameter of type *


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.printInfo()
:::
___

(printTrace-target)=
### [`printTrace`](#printTrace-list)
Logs the passed value to the installed LogManager with a LogLevel of 'Trace'. For Boolean, numbers, and strings, the internal values are printed, for all other types, the type is printed instead


:::{card} Parameters


* Unnamed parameter of type *


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.printTrace()
:::
___

(printWarning-target)=
### [`printWarning`](#printWarning-list)
Logs the passed value to the installed LogManager with a LogLevel of 'Warning'. For Boolean, numbers, and strings, the internal values are printed, for all other types, the type is printed instead


:::{card} Parameters


* Unnamed parameter of type *


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.printWarning()
:::
___

(property-target)=
### [`property`](#property-list)
Returns a list of property identifiers that match the passed regular expression


:::{card} Parameters


* regex `String` 


:::

Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.property(regex)
:::
___

(propertyValue-target)=
### [`propertyValue`](#propertyValue-list)
Returns the value the property, identified by the provided URI. Deprecated in favor of the 'propertyValue' function


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.propertyValue()
:::
___

(readCSVFile-target)=
### [`readCSVFile`](#readCSVFile-list)
Loads the CSV file provided as a parameter and returns it as a vector containing the values of the each row. The inner vector has the same number of values as the CSV has columns. The second parameter controls whether the first entry in the returned outer vector is containing the names of the columns


:::{card} Parameters


* file `Path` 



* includeFirstLine `Boolean?` - Default value: `false` 


:::

Return type: `String[][]` 

:::{code-block} lua
:caption: Signature
openspace.readCSVFile(file, includeFirstLine)
:::
___

(readFile-target)=
### [`readFile`](#readFile-list)
Reads a file from disk and return its contents.


:::{card} Parameters


* file `Path` 


:::

Return type: `String` 

:::{code-block} lua
:caption: Signature
openspace.readFile(file)
:::
___

(rebindKey-target)=
### [`rebindKey`](#rebindKey-list)
Rebinds all scripts from the old key (first argument) to the new key (second argument)


:::{card} Parameters


* oldKey `String` 



* newKey `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.rebindKey(oldKey, newKey)
:::
___

(removeCustomProperty-target)=
### [`removeCustomProperty`](#removeCustomProperty-list)



:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.removeCustomProperty(identifier)
:::
___

(removeInterestingNodes-target)=
### [`removeInterestingNodes`](#removeInterestingNodes-list)
This function removes unmarks the scene graph nodes identified by name as interesting, thus removing the shortcuts from the features properties list


:::{card} Parameters


* sceneGraphNodes `String[]` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.removeInterestingNodes(sceneGraphNodes)
:::
___

(removeSceneGraphNode-target)=
### [`removeSceneGraphNode`](#removeSceneGraphNode-list)
Removes the SceneGraphNode identified by name or by extracting the 'Identifier' key if the parameter is a table.


:::{card} Parameters


* node `String | Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.removeSceneGraphNode(node)
:::
___

(removeSceneGraphNodesFromRegex-target)=
### [`removeSceneGraphNodesFromRegex`](#removeSceneGraphNodesFromRegex-list)
Removes all SceneGraphNodes with identifiers matching the input regular expression.


:::{card} Parameters


* name `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.removeSceneGraphNodesFromRegex(name)
:::
___

(removeScreenSpaceRenderable-target)=
### [`removeScreenSpaceRenderable`](#removeScreenSpaceRenderable-list)
Given a ScreenSpaceRenderable name this script will remove it from the RenderEngine. The parameter can also be a table in which case the 'Identifier' key is used to look up the name from the table.


:::{card} Parameters


* identifier `String | Table` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.removeScreenSpaceRenderable(identifier)
:::
___

(removeTag-target)=
### [`removeTag`](#removeTag-list)
Removes a tag (second argument) from a scene graph node (first argument)


:::{card} Parameters


* uri `String` 



* tag `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.removeTag(uri, tag)
:::
___

(resetCamera-target)=
### [`resetCamera`](#resetCamera-list)
Resets the camera position to the same position where the profile originally started


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.resetCamera()
:::
___

(resetScreenshotNumber-target)=
### [`resetScreenshotNumber`](#resetScreenshotNumber-list)
Reset screenshot index to 0.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.resetScreenshotNumber()
:::
___

(saveSettingsToProfile-target)=
### [`saveSettingsToProfile`](#saveSettingsToProfile-list)
Collects all changes that have been made since startup, including all property changes and assets required, requested, or removed. All changes will be added to the profile that OpenSpace was started with, and the new saved file will contain all of this information. If the argument is provided, the settings will be saved into new profile with that name. If the argument is blank, the current profile will be saved to a backup file and the original profile will be overwritten. The second argument determines if a file that already exists should be overwritten, which is 'false' by default.


:::{card} Parameters


* saveFilePath `String?` 



* overwrite `Boolean?` - Default value: `true` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.saveSettingsToProfile(saveFilePath, overwrite)
:::
___

(sceneGraphNodes-target)=
### [`sceneGraphNodes`](#sceneGraphNodes-list)
Returns a list of all scene graph nodes in the scene


Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.sceneGraphNodes()
:::
___

(screenSpaceRenderables-target)=
### [`screenSpaceRenderables`](#screenSpaceRenderables-list)
Returns a list of all screen-space renderables


Return type: `String[]` 

:::{code-block} lua
:caption: Signature
openspace.screenSpaceRenderables()
:::
___

(setCurrentMission-target)=
### [`setCurrentMission`](#setCurrentMission-list)
Set the currnet mission.


:::{card} Parameters


* missionName `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.setCurrentMission(missionName)
:::
___

(setDefaultDashboard-target)=
### [`setDefaultDashboard`](#setDefaultDashboard-list)
This function sets the default values for the dashboard consisting of 'DashboardItemDate', 'DashboardItemSimulationIncrement', 'DashboardItemDistance', 'DashboardItemFramerate', and 'DashboardItemParallelConnection'


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.setDefaultDashboard()
:::
___

(setDefaultGuiSorting-target)=
### [`setDefaultGuiSorting`](#setDefaultGuiSorting-list)
This function sets the default GUI sorting for the space environment to increasing size, from solar system, through Milky Way, Universe and finishing with other elements


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.setDefaultGuiSorting()
:::
___

(setParent-target)=
### [`setParent`](#setParent-list)
The scene graph node identified by the first string is reparented to be a child of the scene graph node identified by the second string.


:::{card} Parameters


* identifier `String` 



* newParent `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.setParent(identifier, newParent)
:::
___

(setPathToken-target)=
### [`setPathToken`](#setPathToken-list)
Registers the path token provided by the first argument to the path in the second argument. If the path token already exists, it will be silently overridden.


:::{card} Parameters


* pathToken `String` 



* path `Path` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.setPathToken(pathToken, path)
:::
___

(setPropertyValue-target)=
### [`setPropertyValue`](#setPropertyValue-list)
Sets all property(s) identified by the URI (with potential wildcards) in the first argument. The second argument can be any type, but it has to match the type that the property (or properties) expect. If the third is not present or is '0', the value changes instantly, otherwise the change will take that many seconds and the value is interpolated at each step in between. The fourth parameter is an optional easing function if a 'duration' has been specified. If 'duration' is 0, this parameter value is ignored. Otherwise, it can be one of many supported easing functions. See easing.h for available functions. The fifth argument is another Lua script that will be executed when the interpolation provided in parameter 3 finishes.
The URI is interpreted using a wildcard in which '*' is expanded to '(.*)' and bracketed components '{ }' are interpreted as group tag names. Then, the passed value will be set on all properties that fit the regex + group name combination.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.setPropertyValue()
:::
___

(setPropertyValueSingle-target)=
### [`setPropertyValueSingle`](#setPropertyValueSingle-list)
Sets the property identified by the URI in the first argument. The second argument can be any type, but it has to match the type that the property expects. If the third is not present or is '0', the value changes instantly, otherwise the change will take that many seconds and the value is interpolated at each step in between. The fourth parameter is an optional easing function if a 'duration' has been specified. If 'duration' is 0, this parameter value is ignored. Otherwise, it has to be one of the easing functions defined in the list below. This is the same as calling the setValue method and passing 'single' as the fourth argument to setPropertyValue. The fifth argument is another Lua script that will be executed when the interpolation provided in parameter 3 finishes.
 Avaiable easing functions: Linear, QuadraticEaseIn, QuadraticEaseOut, QuadraticEaseInOut, CubicEaseIn, CubicEaseOut, CubicEaseInOut, QuarticEaseIn, QuarticEaseOut, QuarticEaseInOut, QuinticEaseIn, QuinticEaseOut, QuinticEaseInOut, SineEaseIn, SineEaseOut, SineEaseInOut, CircularEaseIn, CircularEaseOut, CircularEaseInOut, ExponentialEaseIn, ExponentialEaseOut, ExponentialEaseInOut, ElasticEaseIn, ElasticEaseOut, ElasticEaseInOut, BounceEaseIn, BounceEaseOut, BounceEaseInOut


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.setPropertyValueSingle()
:::
___

(setScreenshotFolder-target)=
### [`setScreenshotFolder`](#setScreenshotFolder-list)
Sets the folder used for storing screenshots or session recording frames


:::{card} Parameters


* newFolder `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.setScreenshotFolder(newFolder)
:::
___

(takeScreenshot-target)=
### [`takeScreenshot`](#takeScreenshot-list)
Take a screenshot and return the screenshot number. The screenshot will be stored in the ${SCREENSHOTS} folder.


Return type: `Integer` 

:::{code-block} lua
:caption: Signature
openspace.takeScreenshot()
:::
___

(toggleFade-target)=
### [`toggleFade`](#toggleFade-list)
Toggles the fade state of the node(s) with the given identifier over the given
          time in seconds. The identifier can contain a tag and/or a wildcard to target
          several nodes. If the fade time is not provided then the
          "OpenSpaceEngine.FadeDuration" property will be used instead. If the third
          argument (endScript) is provided then that script will be run after the fade
          is finished.


:::{card} Parameters


* identifier `String` 



* fadeTime `Number?` 



* endScript `String?` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.toggleFade(identifier, fadeTime, endScript)
:::
___

(toggleShutdown-target)=
### [`toggleShutdown`](#toggleShutdown-list)
Toggles the shutdown mode that will close the application after the countdown timer is reached


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.toggleShutdown()
:::
___

(unloadMission-target)=
### [`unloadMission`](#unloadMission-list)
Unloads a previously loaded mission.


:::{card} Parameters


* missionName `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.unloadMission(missionName)
:::
___

(unzipFile-target)=
### [`unzipFile`](#unzipFile-list)
This function extracts the contents of a zip file. The first argument is the path to the zip file. The second argument is the directory where to put the extracted files. If the third argument is true, the compressed file will be deleted after the decompression is finished.


:::{card} Parameters


* source `String` 



* destination `String` 



* deleteSource `Boolean?` - Default value: `false` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.unzipFile(source, destination, deleteSource)
:::
___

(version-target)=
### [`version`](#version-list)
This function returns information about the current OpenSpace version. The resulting table has the structure: 
:::{code-block} lua
 Version = { Major = <number> Minor = <number> Patch = <number> }, Commit = <string> Branch = <string> 
:::


Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.version()
:::
___

(walkDirectory-target)=
### [`walkDirectory`](#walkDirectory-list)
Walks a directory and returns the contents of the directory as absolute paths. The first argument is the path of the directory that should be walked, the second argument determines if the walk is recursive and will continue in contained directories. The default value for this parameter is \"false\". The third argument determines whether the table that is returned is sorted. The default value for this parameter is \"false\".


:::{card} Parameters


* path `Path` 



* recursive `Boolean?` - Default value: `false` 



* sorted `Boolean?` - Default value: `false` 


:::

Return type: `Path[]` 

:::{code-block} lua
:caption: Signature
openspace.walkDirectory(path, recursive, sorted)
:::
___

(walkDirectoryFiles-target)=
### [`walkDirectoryFiles`](#walkDirectoryFiles-list)
Walks a directory and returns the files of the directory as absolute paths. The first argument is the path of the directory that should be walked, the second argument determines if the walk is recursive and will continue in contained directories. The default value for this parameter is \"false\". The third argument determines whether the table that is returned is sorted. The default value for this parameter is \"false\".


:::{card} Parameters


* path `Path` 



* recursive `Boolean?` - Default value: `false` 



* sorted `Boolean?` - Default value: `false` 


:::

Return type: `Path[]` 

:::{code-block} lua
:caption: Signature
openspace.walkDirectoryFiles(path, recursive, sorted)
:::
___

(walkDirectoryFolders-target)=
### [`walkDirectoryFolders`](#walkDirectoryFolders-list)
Walks a directory and returns the subfolders of the directory as absolute paths. The first argument is the path of the directory that should be walked, the second argument determines if the walk is recursive and will continue in contained directories. The default value for this parameter is \"false\". The third argument determines whether the table that is returned is sorted. The default value for this parameter is \"false\".


:::{card} Parameters


* path `Path` 



* recursive `Boolean?` - Default value: `false` 



* sorted `Boolean?` - Default value: `false` 


:::

Return type: `Path[]` 

:::{code-block} lua
:caption: Signature
openspace.walkDirectoryFolders(path, recursive, sorted)
:::
___

(worldPosition-target)=
### [`worldPosition`](#worldPosition-list)
Returns the world position of the scene graph node with the given string as identifier.


:::{card} Parameters


* identifier `String` 


:::

Return type: `vec3` 

:::{code-block} lua
:caption: Signature
openspace.worldPosition(identifier)
:::
___

(worldRotation-target)=
### [`worldRotation`](#worldRotation-list)
Returns the world rotation matrix of the scene graph node with the given string as identifier.


:::{card} Parameters


* identifier `String` 


:::

Return type: `mat3x3` 

:::{code-block} lua
:caption: Signature
openspace.worldRotation(identifier)
:::
___

(writeDocumentation-target)=
### [`writeDocumentation`](#writeDocumentation-list)
Writes out documentation files


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.writeDocumentation()
:::

