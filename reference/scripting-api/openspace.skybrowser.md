# `openspace.skybrowser`
## Functions overview

:::{list-table}
:header-rows: 1
:widths: 2 10
:width: 100%
*   - Name
    - Documentation


*   - [`addDisplayCopy`](#skybrowseraddDisplayCopy-target)
    - [Takes an identifier to a sky browser and adds a rendered copy to it]{#skybrowseraddDisplayCopy-list}


*   - [`addPairToSkyBrowserModule`](#skybrowseraddPairToSkyBrowserModule-target)
    - [Takes the identifier of the sky target and a sky browser and adds them to the sky browser module]{#skybrowseraddPairToSkyBrowserModule-list}


*   - [`adjustCamera`](#skybrowseradjustCamera-target)
    - [Takes an identifier to a sky browser or sky target]{#skybrowseradjustCamera-list}


*   - [`centerTargetOnScreen`](#skybrowsercenterTargetOnScreen-target)
    - [Takes an identifier to a sky browser and animates its corresponding target to the center of the current view]{#skybrowsercenterTargetOnScreen-list}


*   - [`createTargetBrowserPair`](#skybrowsercreateTargetBrowserPair-target)
    - [Creates a sky browser and a target]{#skybrowsercreateTargetBrowserPair-list}


*   - [`disableHoverCircle`](#skybrowserdisableHoverCircle-target)
    - [Disables the hover circle, if there is one added to the sky browser module]{#skybrowserdisableHoverCircle-list}


*   - [`finetuneTargetPosition`](#skybrowserfinetuneTargetPosition-target)
    - [Finetunes the target depending on a mouse drag]{#skybrowserfinetuneTargetPosition-list}


*   - [`getListOfImages`](#skybrowsergetListOfImages-target)
    - [Deprecated in favor of 'listOfExoplanets']{#skybrowsergetListOfImages-list}


*   - [`getTargetData`](#skybrowsergetTargetData-target)
    - [Deprecated in favor of 'targetData']{#skybrowsergetTargetData-list}


*   - [`getWwtImageCollectionUrl`](#skybrowsergetWwtImageCollectionUrl-target)
    - [Deprecated in favor of 'wwtImageCollectionUrl']{#skybrowsergetWwtImageCollectionUrl-list}


*   - [`initializeBrowser`](#skybrowserinitializeBrowser-target)
    - [Takes an identifier to a sky browser and starts the initialization for that browser]{#skybrowserinitializeBrowser-list}


*   - [`listOfImages`](#skybrowserlistOfImages-target)
    - [Returns a list of all the loaded AAS WorldWide Telescope images that have been loaded]{#skybrowserlistOfImages-list}


*   - [`loadImagesToWWT`](#skybrowserloadImagesToWWT-target)
    - [Takes an identifier to a sky browser or target and loads the WWT image collection to that browser]{#skybrowserloadImagesToWWT-list}


*   - [`loadingImageCollectionComplete`](#skybrowserloadingImageCollectionComplete-target)
    - [Sets the image collection as loaded in the sky browser]{#skybrowserloadingImageCollectionComplete-list}


*   - [`moveCircleToHoverImage`](#skybrowsermoveCircleToHoverImage-target)
    - [Moves the hover circle to the coordinate specified by the image index]{#skybrowsermoveCircleToHoverImage-list}


*   - [`reloadDisplayCopyOnNode`](#skybrowserreloadDisplayCopyOnNode-target)
    - [Reloads the sky browser display copy for the node index that is sent in]{#skybrowserreloadDisplayCopyOnNode-list}


*   - [`removeDisplayCopy`](#skybrowserremoveDisplayCopy-target)
    - [Takes an identifier to a sky browser and removes the latest added rendered copy to it]{#skybrowserremoveDisplayCopy-list}


*   - [`removeSelectedImageInBrowser`](#skybrowserremoveSelectedImageInBrowser-target)
    - [Takes an identifier to a sky browser or target and an index to an image]{#skybrowserremoveSelectedImageInBrowser-list}


*   - [`removeTargetBrowserPair`](#skybrowserremoveTargetBrowserPair-target)
    - [Takes in identifier to a sky browser or target and removes them]{#skybrowserremoveTargetBrowserPair-list}


*   - [`scrollOverBrowser`](#skybrowserscrollOverBrowser-target)
    - [Takes an identifier to a sky browser or a sky target and a vertical field of view]{#skybrowserscrollOverBrowser-list}


*   - [`selectImage`](#skybrowserselectImage-target)
    - [Takes an index to an image and selects that image in the currently selected sky browser]{#skybrowserselectImage-list}


*   - [`sendOutIdsToBrowsers`](#skybrowsersendOutIdsToBrowsers-target)
    - [Sends all sky browsers' identifiers to their respective CEF browser]{#skybrowsersendOutIdsToBrowsers-list}


*   - [`setBorderColor`](#skybrowsersetBorderColor-target)
    - [Takes an identifier to a sky browser or a sky target and a rgb color in the ranges [0, 255]]{#skybrowsersetBorderColor-list}


*   - [`setBorderRadius`](#skybrowsersetBorderRadius-target)
    - [Takes an identifier to a sky browser and a radius value between 0 and 1, where 0 is rectangular and 1 is circular]{#skybrowsersetBorderRadius-list}


*   - [`setBrowserRatio`](#skybrowsersetBrowserRatio-target)
    - [Sets the screen space size of the sky browser to the numbers specified by the input [x, y]]{#skybrowsersetBrowserRatio-list}


*   - [`setEquatorialAim`](#skybrowsersetEquatorialAim-target)
    - [Takes the identifier of a sky browser or a sky target and equatorial coordinates Right Ascension and Declination]{#skybrowsersetEquatorialAim-list}


*   - [`setHoverCircle`](#skybrowsersetHoverCircle-target)
    - [Takes an identifier to a screen space renderable and adds it to the module]{#skybrowsersetHoverCircle-list}


*   - [`setImageLayerOrder`](#skybrowsersetImageLayerOrder-target)
    - [Takes an identifier to a sky browser or a sky target, an image index and the order which it should have in the selected image list]{#skybrowsersetImageLayerOrder-list}


*   - [`setOpacityOfImageLayer`](#skybrowsersetOpacityOfImageLayer-target)
    - [Takes an identifier to a sky browser or sky target, an index to an image and a value for the opacity]{#skybrowsersetOpacityOfImageLayer-list}


*   - [`setSelectedBrowser`](#skybrowsersetSelectedBrowser-target)
    - [Takes an identifier to a sky browser or target]{#skybrowsersetSelectedBrowser-list}


*   - [`setVerticalFov`](#skybrowsersetVerticalFov-target)
    - [Takes an identifier to a sky browser or a sky target and a vertical field of view]{#skybrowsersetVerticalFov-list}


*   - [`showAllTargetsAndBrowsers`](#skybrowsershowAllTargetsAndBrowsers-target)
    - [Show or hide all targets and browsers]{#skybrowsershowAllTargetsAndBrowsers-list}


*   - [`startFinetuningTarget`](#skybrowserstartFinetuningTarget-target)
    - [Starts the fine-tuning of the target rendered copy to it]{#skybrowserstartFinetuningTarget-list}


*   - [`startSetup`](#skybrowserstartSetup-target)
    - [Starts the setup process of the sky browers]{#skybrowserstartSetup-list}


*   - [`stopAnimations`](#skybrowserstopAnimations-target)
    - [Stop animations]{#skybrowserstopAnimations-list}


*   - [`targetData`](#skybrowsertargetData-target)
    - [Returns a table of data regarding the current view and the sky browsers and targets]{#skybrowsertargetData-list}


*   - [`translateScreenSpaceRenderable`](#skybrowsertranslateScreenSpaceRenderable-target)
    - [Takes an identifier to a sky browser or sky target and the [x, y] starting position and the [x, y] translation vector]{#skybrowsertranslateScreenSpaceRenderable-list}


*   - [`wwtImageCollectionUrl`](#skybrowserwwtImageCollectionUrl-target)
    - [Returns the AAS WorldWide Telescope image collection url]{#skybrowserwwtImageCollectionUrl-list}

:::

## Functions

(skybrowseraddDisplayCopy-target)=
### [`addDisplayCopy`](#skybrowseraddDisplayCopy-list)
Takes an identifier to a sky browser and adds a rendered copy to it. The first argument is the position of the first copy. The position is in RAE or Cartesian coordinates, depending on if 'Use Radius Azimuth Elevation' is checked. The second argument is the number of copies. If RAE is used, they will be evenly spread out on the azimuth.


:::{card} Parameters


* identifier `String` 



* numberOfCopies `Integer?` - Default value: `1` 



* position `vec3?` - Default value: `glm::vec3(2.1f, 0.f, 0.f)` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.addDisplayCopy(identifier, numberOfCopies, position)
:::
___

(skybrowseraddPairToSkyBrowserModule-target)=
### [`addPairToSkyBrowserModule`](#skybrowseraddPairToSkyBrowserModule-list)
Takes the identifier of the sky target and a sky browser and adds them to the sky browser module.


:::{card} Parameters


* targetId `String` 



* browserId `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.addPairToSkyBrowserModule(targetId, browserId)
:::
___

(skybrowseradjustCamera-target)=
### [`adjustCamera`](#skybrowseradjustCamera-list)
Takes an identifier to a sky browser or sky target. Rotates the camera so that the target is placed in the center of the view.


:::{card} Parameters


* id `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.adjustCamera(id)
:::
___

(skybrowsercenterTargetOnScreen-target)=
### [`centerTargetOnScreen`](#skybrowsercenterTargetOnScreen-list)
Takes an identifier to a sky browser and animates its corresponding target to the center of the current view.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.centerTargetOnScreen(identifier)
:::
___

(skybrowsercreateTargetBrowserPair-target)=
### [`createTargetBrowserPair`](#skybrowsercreateTargetBrowserPair-list)
Creates a sky browser and a target.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.createTargetBrowserPair()
:::
___

(skybrowserdisableHoverCircle-target)=
### [`disableHoverCircle`](#skybrowserdisableHoverCircle-list)
Disables the hover circle, if there is one added to the sky browser module.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.disableHoverCircle()
:::
___

(skybrowserfinetuneTargetPosition-target)=
### [`finetuneTargetPosition`](#skybrowserfinetuneTargetPosition-list)
Finetunes the target depending on a mouse drag. rendered copy to it. First argument is the identifier of the sky browser, second is the start position of the drag and third is the end position of the drag.


:::{card} Parameters


* identifier `String` 



* translation `vec2` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.finetuneTargetPosition(identifier, translation)
:::
___

(skybrowsergetListOfImages-target)=
### [`getListOfImages`](#skybrowsergetListOfImages-list)
Deprecated in favor of 'listOfExoplanets'


Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.getListOfImages()
:::
___

(skybrowsergetTargetData-target)=
### [`getTargetData`](#skybrowsergetTargetData-list)
Deprecated in favor of 'targetData'


Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.getTargetData()
:::
___

(skybrowsergetWwtImageCollectionUrl-target)=
### [`getWwtImageCollectionUrl`](#skybrowsergetWwtImageCollectionUrl-list)
Deprecated in favor of 'wwtImageCollectionUrl'


Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.getWwtImageCollectionUrl()
:::
___

(skybrowserinitializeBrowser-target)=
### [`initializeBrowser`](#skybrowserinitializeBrowser-list)
Takes an identifier to a sky browser and starts the initialization for that browser. That means that the browser starts to try to connect to the AAS WorldWide Telescope application by sending it messages. And that the target matches its appearance to its corresponding browser.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.initializeBrowser(identifier)
:::
___

(skybrowserlistOfImages-target)=
### [`listOfImages`](#skybrowserlistOfImages-list)
Returns a list of all the loaded AAS WorldWide Telescope images that have been loaded. Each image has a name, thumbnail url, equatorial spherical coordinates RA and Dec, equatorial Cartesian coordinates, if the image has celestial coordinates, credits text, credits url and the identifier of the image which is a unique number.


Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.listOfImages()
:::
___

(skybrowserloadImagesToWWT-target)=
### [`loadImagesToWWT`](#skybrowserloadImagesToWWT-list)
Takes an identifier to a sky browser or target and loads the WWT image collection to that browser.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.loadImagesToWWT(identifier)
:::
___

(skybrowserloadingImageCollectionComplete-target)=
### [`loadingImageCollectionComplete`](#skybrowserloadingImageCollectionComplete-list)
Sets the image collection as loaded in the sky browser. Takes an identifier to the sky browser.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.loadingImageCollectionComplete(identifier)
:::
___

(skybrowsermoveCircleToHoverImage-target)=
### [`moveCircleToHoverImage`](#skybrowsermoveCircleToHoverImage-list)
Moves the hover circle to the coordinate specified by the image index.


:::{card} Parameters


* imageUrl `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.moveCircleToHoverImage(imageUrl)
:::
___

(skybrowserreloadDisplayCopyOnNode-target)=
### [`reloadDisplayCopyOnNode`](#skybrowserreloadDisplayCopyOnNode-list)
Reloads the sky browser display copy for the node index that is sent in. .If no ID is sent in, it will reload all display copies on that node.


:::{card} Parameters


* nodeIndex `Integer` 



* id `String?` - Default value: `"all"` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.reloadDisplayCopyOnNode(nodeIndex, id)
:::
___

(skybrowserremoveDisplayCopy-target)=
### [`removeDisplayCopy`](#skybrowserremoveDisplayCopy-list)
Takes an identifier to a sky browser and removes the latest added rendered copy to it.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.removeDisplayCopy(identifier)
:::
___

(skybrowserremoveSelectedImageInBrowser-target)=
### [`removeSelectedImageInBrowser`](#skybrowserremoveSelectedImageInBrowser-list)
Takes an identifier to a sky browser or target and an index to an image. Removes that image from that sky browser.


:::{card} Parameters


* identifier `String` 



* imageUrl `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.removeSelectedImageInBrowser(identifier, imageUrl)
:::
___

(skybrowserremoveTargetBrowserPair-target)=
### [`removeTargetBrowserPair`](#skybrowserremoveTargetBrowserPair-list)
Takes in identifier to a sky browser or target and removes them.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.removeTargetBrowserPair(identifier)
:::
___

(skybrowserscrollOverBrowser-target)=
### [`scrollOverBrowser`](#skybrowserscrollOverBrowser-list)
Takes an identifier to a sky browser or a sky target and a vertical field of view. Changes the field of view as specified by the input.


:::{card} Parameters


* identifier `String` 



* scroll `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.scrollOverBrowser(identifier, scroll)
:::
___

(skybrowserselectImage-target)=
### [`selectImage`](#skybrowserselectImage-list)
Takes an index to an image and selects that image in the currently selected sky browser.


:::{card} Parameters


* imageUrl `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.selectImage(imageUrl)
:::
___

(skybrowsersendOutIdsToBrowsers-target)=
### [`sendOutIdsToBrowsers`](#skybrowsersendOutIdsToBrowsers-list)
Sends all sky browsers' identifiers to their respective CEF browser.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.sendOutIdsToBrowsers()
:::
___

(skybrowsersetBorderColor-target)=
### [`setBorderColor`](#skybrowsersetBorderColor-list)
Takes an identifier to a sky browser or a sky target and a rgb color in the ranges [0, 255].


:::{card} Parameters


* identifier `String` 



* red `Integer` 



* green `Integer` 



* blue `Integer` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setBorderColor(identifier, red, green, blue)
:::
___

(skybrowsersetBorderRadius-target)=
### [`setBorderRadius`](#skybrowsersetBorderRadius-list)
Takes an identifier to a sky browser and a radius value between 0 and 1, where 0 is rectangular and 1 is circular


:::{card} Parameters


* identifier `String` 



* radius `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setBorderRadius(identifier, radius)
:::
___

(skybrowsersetBrowserRatio-target)=
### [`setBrowserRatio`](#skybrowsersetBrowserRatio-list)
Sets the screen space size of the sky browser to the numbers specified by the input [x, y].


:::{card} Parameters


* identifier `String` 



* ratio `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setBrowserRatio(identifier, ratio)
:::
___

(skybrowsersetEquatorialAim-target)=
### [`setEquatorialAim`](#skybrowsersetEquatorialAim-list)
Takes the identifier of a sky browser or a sky target and equatorial coordinates Right Ascension and Declination. The target will animate to this coordinate and the browser will display the coordinate.


:::{card} Parameters


* identifier `String` 



* rightAscension `Number` 



* declination `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setEquatorialAim(identifier, rightAscension, declination)
:::
___

(skybrowsersetHoverCircle-target)=
### [`setHoverCircle`](#skybrowsersetHoverCircle-list)
Takes an identifier to a screen space renderable and adds it to the module.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setHoverCircle(identifier)
:::
___

(skybrowsersetImageLayerOrder-target)=
### [`setImageLayerOrder`](#skybrowsersetImageLayerOrder-list)
Takes an identifier to a sky browser or a sky target, an image index and the order which it should have in the selected image list. The image is then changed to have this order.


:::{card} Parameters


* identifier `String` 



* imageUrl `String` 



* imageOrder `Integer` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setImageLayerOrder(identifier, imageUrl, imageOrder)
:::
___

(skybrowsersetOpacityOfImageLayer-target)=
### [`setOpacityOfImageLayer`](#skybrowsersetOpacityOfImageLayer-list)
Takes an identifier to a sky browser or sky target, an index to an image and a value for the opacity.


:::{card} Parameters


* identifier `String` 



* imageUrl `String` 



* opacity `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setOpacityOfImageLayer(identifier, imageUrl, opacity)
:::
___

(skybrowsersetSelectedBrowser-target)=
### [`setSelectedBrowser`](#skybrowsersetSelectedBrowser-list)
Takes an identifier to a sky browser or target. Sets that sky browser currently selected.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setSelectedBrowser(identifier)
:::
___

(skybrowsersetVerticalFov-target)=
### [`setVerticalFov`](#skybrowsersetVerticalFov-list)
Takes an identifier to a sky browser or a sky target and a vertical field of view. Changes the field of view as specified by the input.


:::{card} Parameters


* identifier `String` 



* verticalFieldOfView `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.setVerticalFov(identifier, verticalFieldOfView)
:::
___

(skybrowsershowAllTargetsAndBrowsers-target)=
### [`showAllTargetsAndBrowsers`](#skybrowsershowAllTargetsAndBrowsers-list)
Show or hide all targets and browsers. Takes a boolean that sets it to either be shown or not.


:::{card} Parameters


* show `Boolean` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.showAllTargetsAndBrowsers(show)
:::
___

(skybrowserstartFinetuningTarget-target)=
### [`startFinetuningTarget`](#skybrowserstartFinetuningTarget-list)
Starts the fine-tuning of the target rendered copy to it.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.startFinetuningTarget(identifier)
:::
___

(skybrowserstartSetup-target)=
### [`startSetup`](#skybrowserstartSetup-list)
Starts the setup process of the sky browers. This function calls the Lua function 'sendOutIdsToBrowsers' in all nodes in the cluster.


Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.startSetup()
:::
___

(skybrowserstopAnimations-target)=
### [`stopAnimations`](#skybrowserstopAnimations-list)
Stop animations. Takes an identifier to a sky browser.


:::{card} Parameters


* identifier `String` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.stopAnimations(identifier)
:::
___

(skybrowsertargetData-target)=
### [`targetData`](#skybrowsertargetData-list)
Returns a table of data regarding the current view and the sky browsers and targets. returns a table of data regarding the current targets.


Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.targetData()
:::
___

(skybrowsertranslateScreenSpaceRenderable-target)=
### [`translateScreenSpaceRenderable`](#skybrowsertranslateScreenSpaceRenderable-list)
Takes an identifier to a sky browser or sky target and the [x, y] starting position and the [x, y] translation vector.


:::{card} Parameters


* identifier `String` 



* startingPositionX `Number` 



* startingPositionY `Number` 



* translationX `Number` 



* translationY `Number` 


:::

Return type: `void` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.translateScreenSpaceRenderable(identifier, startingPositionX, startingPositionY, translationX, translationY)
:::
___

(skybrowserwwtImageCollectionUrl-target)=
### [`wwtImageCollectionUrl`](#skybrowserwwtImageCollectionUrl-list)
Returns the AAS WorldWide Telescope image collection url.


Return type: `Table` 

:::{code-block} lua
:caption: Signature
openspace.skybrowser.wwtImageCollectionUrl()
:::

