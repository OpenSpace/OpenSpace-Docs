# Assets Panel
![Assets Panel Button](/using-openspace/toolbar/assets/toolbar_button_assets.png)

{menuselection}`Windows --> Content --> Assets`

The Assets Panel is an interactive way to access the assets available to OpenSpace. Clicking on an asset will load it into OpenSpace.

:::{figure} assets_panel.png
:align: center
:width: 80%
:figwidth: 70%
:alt: OpenSpace's Assets Panel

OpenSpace's Assets Panel.
:::

When you bring the Assets Panel up, it is similar to the Actions Panel in that it operates in a folder structure. The home icon at the top reports where you are within the file structure.

If we click on the `Built-in assets` folder, we will see that reflected in the blue-shaded path at the top of the panel, and, of course, see a listing of all the assets and folders located there.

:::{figure} assets_panel_built_in.png
:align: center
:width: 80%
:figwidth: 70%
:alt: OpenSpace's Assets Panel showing built-in assets

OpenSpace's Assets Panel showing the built-in assets in your OpenSpace folder.
:::

Most of the assets in `Built-in assets` are organized in subfolders. However, there are several assets located in this folder, namely, the `base` and `base_blank` assets and the `default_keybindings` and `base_keybindings` assets. Notice these appear blue, meaning they are files not folders. 

There are several actions you can take on an asset. The green checkmark signifies the asset is loaded, and there is a trashcan if you want to unload the asset from the current run. The three dots open a menu for further actions, which include copying the asset's path and reloading the asset. (Reloading the asset can be useful if you're editing an asset and want to reload a new version, mostly in the development phase of an asset.)


If we navigate to the Digital Universe assets, using `Built-in assets/scene/digitaluniverse`, we can see many of them are loaded, but not all of them are in the default profile.

:::{figure} assets_panel_du.png
:align: center
:width: 80%
:figwidth: 70%
:alt: OpenSpace's Assets Panel showing the Digital Universe assets

OpenSpace's Assets Panel showing the Digital Universe assets.
:::

To load one of these assets, we can simply click on the asset file name, and OpenSpace will attempt to load the asset file and accompanying data. However, please read the following warnings before you do so.


:::{warning}
Using the Assets Panel can temporarily hamper your computer if you're trying to load a large data set. Initializing the asset will freeze OpenSpace. If you're flying, flight will freeze until the data set is initialized and the data are locally cached. If you're loading a small data set, then this won't affect the graphics too much---maybe a small hiccup. However, if you're loading a large data set, particularly if you've not loaded it before and it needs to cache, then it could hamper performance noticeably. 

It's best to use this panel when you are familiar with the data, and when you're working on developing an asset and not giving a demonstration to an audience.
:::

:::{danger}
Unfamiliarity with the data set you're loading could result in exceeding your computer's memory. OpenSpace will crash if you run out of RAM.
:::