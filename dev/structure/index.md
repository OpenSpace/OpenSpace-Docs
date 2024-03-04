# Code Structure
% Here is the link to describe the syntax used in this document

## Libraries
Here is an incomplete list of libraries that are involved to build the _OpenSpace_ executable. 
:::{mermaid}
:zoom:

classDiagram
  Ghoul --> openspace-core
  Ghoul --> openspace-module-atmosphere
  Ghoul --> openspace-module-base
  Ghoul --> openspace-module-globebrowsing
  Ghoul --> openspace-module-space

  openspace-core --> openspace-module-atmosphere
  openspace-module-atmosphere --> openspace-module-collection
  openspace-core --> openspace-module-base
  openspace-module-base --> openspace-module-collection
  openspace-core --> openspace-module-space
  openspace-module-space --> openspace-module-collection
  openspace-core --> openspace-module-globebrowsing
  openspace-module-globebrowsing --> openspace-module-collection
  GDAL --> openspace-module-globebrowsing
  openspace-core --> openspace-module-volume
  openspace-core --> openspace-module-kameleon
  openspace-kameleon --> openspace-module-kameleonvolume
  openspace-volume --> openspace-module-kameleonvolume
  openspace-core --> openspace-module-kameleonvolume

  GLFW --> SGCT
  SGCT --> OpenSpace
  openspace-core --> OpenSpace
  openspace-module-collection --> OpenSpace
:::
 - [Ghoul](https://github.com/OpenSpace/Ghoul) is a helper library that contains classes and functions that are useful beyond just OpenSpace
 - [SGCT](https://github.com/SGCT/SGCT) is a library that helps with cluster synchronization and window creation
 - `openspace-core` contains the core elements of the "game engine" part of OpenSpace, such as the handling of the scene graph, scripting, rendering, interaction methods, navigation, and others
 - Functionality is divided into _Modules_ that can that implement abstract classes defined in the `openspace-core`. Modules can depend on other modules and even other third-party libraries
 - _Modules_ are collected in the `openspace-module-collection` which in itself does not contain any additional code
 - The _OpenSpace_ application consists of SGCT, `openspace-core`, and the `openspace-module-collection`

## Classes
The `openspace-core` project contains all of the fundamental classes that are needed for the engine part of OpenSpace. These include a `SceneGraphNode` which is collected into a `Scene`. The `Scene` has one special `SceneGraphNode` called the `Root`, which is the only scene graph node without a parent. A few of these are abstract base classes which are then derived from in other modules and thus filled with functionality.

Examples of these abstract classes are:
  - `Renderable`:  A class that represents anything that is rendered within the 3D scene and shows up on screen
  - `Translation`:  A class that describes some form of translation relative to the scene graph node's parent
  - `Rotation`:  A class that describes some form of rotation relative to the scene graph node's parent
  - `Scale`:  A class that describes some form of scaling relative to the scene graph node's parent
  - `ScreenSpaceRenderable`:  A class that renders something on the screen but is not affected by the camera movement

:::{mermaid}
:zoom:

classDiagram

  namespace core {
  class RenderEngine {
    +render()
    +renderOverlays()
  }

  class Scene {
    +update()
    +render()
  }

  class PropertyOwner {
    - std::string _identifier
    - std::string _guiName
    - PropertyOwner _owner
    - std::vector<PropertyOwner*> _subOwners
  }

  class Property {
    - std::string _identifier
    - _guiName
    + set(std::any)
    - std::any get()
  }

  class SceneGraphNode {
    +initialize()
    +initializeGL()
    +deinitialize()
    +deinitializeGL()
    +update(UpdateData)
    +render(RenderData)
  }

  class Renderable {
    +initialize()
    +initializeGL()
    +deinitialize()
    +deinitializeGL()
    +update()
    +render()
  }

  class Translation {
    +position()
  }

  class Rotation {
    +matrix()
  }

  class Scale {
    +scaleValue()
  }

  class ScreenSpaceRenderable {
    +initialize()
    +initializeGL()
    +deinitialize()
    +deinitializeGL()

    +update()
    +render()
  }

  }

  namespace openspace-base {
    class RenderableGrid
    class RenderableSphere

    class ScreenSpaceImageLocal

    class StaticTranslation
    class TimelineTranslation
    class StaticRotation
    class StaticScale
  }

  namespace openspace-space {
    class RenderableStars

    class SpiceTranslation
  }

  namespace openspace-globebrowsing {
    class RenderableGlobe
  }

  PropertyOwner <|-- SceneGraphNode
  PropertyOwner <|-- Renderable
  PropertyOwner <|-- Translation
  PropertyOwner <|-- Rotation
  PropertyOwner <|-- Scale
  PropertyOwner <|-- Scene
  PropertyOwner <|-- ScreenSpaceRenderable
  PropertyOwner <|-- RenderEngine

  PropertyOwner "1" --> "*" Property

  RenderEngine "1" --> "1" Scene
  RenderEngine "1" --> "0..1" ScreenSpaceRenderable
  Scene "1" --> "*" SceneGraphNode
  SceneGraphNode "1" --> "0..1" Renderable
  SceneGraphNode "1" --> "0..1" Translation
  SceneGraphNode "1" --> "0..1" Rotation
  SceneGraphNode "1" --> "0..1" Scale


  Renderable <|-- RenderableGrid
  Renderable <|-- RenderableSphere
  ScreenSpaceRenderable <|-- ScreenSpaceImageLocal
  Translation <|-- StaticTranslation
  Translation <|-- TimelineTranslation
  Rotation <|-- StaticRotation
  Scale <|-- StaticScale

  Renderable <|-- RenderableStars
  Translation <|-- SpiceTranslation

  Renderable <|-- RenderableGlobe
:::

## Assets
All content is controlled through the inclusion of assets. Assets are fundamentally Lua scripts that have access to a special variable `asset` which is injected by OpenSpace. This variable has a few functions that allow the asset to affect OpenSpace. A selection of these functions are:
  - `asset.require`: Causes this asset to load another asset file, the path of which is provided either as a relative or absolute path. This function returns a table that contains all of the symbols that were `asset.export`ed by the required asset (see below)
  - `asset.onInitialize`: This function takes a function as an argument which is executed when the asset is asked to initialize itself. A common use case for this is for the asset to add a scene graph node to the scene in OpenSpace
  - `asset.onDeinitialize`: Analogously to the `onInitialize`, the function passed as an argument into this function is called when the asset is to be unloaded
  - `asset.export`: Export a single element to anyone that `asset.require`s this asset.

Through the user of the `asset.require` function, assets form a tree where a _Parent_ `require`s their _Children_.

### Simple Example
In this example, the child asset simply defines a variable that is then read by the parent asset and printed to the console.
```{literalinclude} example1_child.asset
:language: lua
```

```{literalinclude} example1_parent.asset
:language: lua
```

### Advanced Example
In this example, the child asset is defining, adding, and exporting a scene graph node that is used in the parent asset to specify the parent of a scene graph node.
```{literalinclude} example2_child.asset
:language: lua
```

```{literalinclude} example2_parent.asset
:language: lua
```
