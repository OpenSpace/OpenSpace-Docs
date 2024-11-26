---
authors:
  - name: Brian Abbott, Micah Acinapura
    affiliation: American Museum of Natural History
---


# Create a Profile 

:::{warning}
This section is in progress. Text will appear on this page in the future.
:::


## Customizing Profiles
[Profiles](/profiles/index) help us to 
1. Set properties to initial values when we start up OpenSpace
2. Load the assets we desire to display
3. Set keybindings for various actions
4. Set initial camera location and orientation
and more advanced uses like additional modules and additional scripts. Though we can [create profiles by hand](/profiles/index), the recommended way and the easier way would be to use the profile editor which is accessed via the "Edit" or "New" buttons under the 'Choose Profile' section of the Launcher window when starting up OpenSpace.

## Add an asset
Let's take the example of the dwarf planet Haumea for customizing a profile. The default profile does not include this dwarf planet (though the default_full profile does), so let's edit the default profile to add Haumea. With the default profile selected, click "Edit" under the 'Choose Profile' section of the Launcher window. Now choose the "Edit" button next to Assets in the Profile Editor window.
:::{figure} 91-edit-assets-profile-editor.png 
The Edit button for Assets in the Profile Editor
:::
The asset selector window which opens up lists all the assets available under data/assets of the current installation. Since we know we're looking for Haumea, we can directly type it into the search box and find it immediately instead of having to navigate through all the folders, and enable it with the checkbox on the right, as below.
:::{figure} 92-find-haumea-and-enable.png 
Finding the Haumea asset and enabling it using the Search box
:::
After clicking "Save", we can save this profile as default_with_Haumea by typing that name in the Profile Name box and then "Save" at the bottom of the Profile Editor window.
:::{figure} 93-save-default-with-haumea.png 
Save the profile with a new name
:::

:::{note}
Note that you can also add an asset temporarily, or in a one-off manner, by using the [console](/using-openspace/scripting/console/index) as mentioned in the last section of [this page](/creating-data-assets/ephemeris/kepler), or by dragging and dropping the **.asset** file into the OpenSpace window after OpenSpace has started up.
:::

## Change the initial Camera Position
Next, let's change another setting in our new profile. When OpenSpace starts up with our new profile, it still starts with Earth in the frame. Let's change this default view to Saturn instead. For that, we need to click the "Edit" button in the Launcher window to open the Profile Editor, and then choose the "Edit" button under Camera, as below.
:::{figure} 94-edit-camera.png 
Edit the Camera settings in the Profile Editor
:::
We can then change the Camera Position set in the Geo State tab, replacing Earth with Saturn, and increasing the altitude a bit since Saturn is so much bigger than Earth. We should now "Save" the Camera Position and then "Save" the profile. 
:::{figure} 95-change-geo-state.png 
Change the Geo State Anchor value 
:::
Now, if we start up OpenSpace with this profile, we're greeted with the initial view of Saturn instead of Earth.
:::{figure} 96-starts-with-saturn.png 
This profile now starts OpenSpace with a view of Saturn
:::



