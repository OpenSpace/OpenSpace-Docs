# FAQ
## Configuration
### Is it possible to run OpenSpace in kiosk mode and mask the display area ?
There are two steps and two options to achieving what I think you want;
  1. To hide the GUI elements you can add the following scripts to the "Additional Scripts" section of your `.profile` file that you are using:
     ```lua
     openspace.setPropertyValueSingle('Modules.CefWebGui.Visible', false);
     openspace.setPropertyValueSingle('Dashboard.IsEnabled', false);
     openspace.setPropertyValueSingle("RenderEngine.ShowLog", false);
     openspace.setPropertyValueSingle("RenderEngine.ShowVersion", false);
     openspace.setPropertyValueSingle("RenderEngine.ShowCamera", false);
     ```
  1. There are two options for the masking:
     1. Copy the `single.json` from the `config` folder and give it a new name (`single-possize.json` in my case; my version attached here). In the `openspace.cfg` replace `SGCTConfig = sgct.config.single{}` with `SGCTConfig = "${CONFIG}/single-masked.json` to use it. In the XML file modify lines 12 and 13. Both `Pos` and `Size` are in values from 0 to 1, so in my example i move the rendering window up to the top right by a quarter of the screen size.
     1. Same first steps as (a) but instead of modifying the Pos and Size (example as `single-masked.json`) you add `mask: "mask.png"` to the `Viewport` key. You can choose whichever filename you like. The image should be a black/white image image; the rendering is masked out where the image is black, shown where it is white. Please not that the `mask.png` has to be in the same folder as the `OpenSpace.exe` for this to work

- The mask file: <path:mask.png>
- Configuration file 1: <path:single-masked.json>
- Configuration file 2: <path:single-possize.json>

## Wormhole
### Is there a way to configure the Wormhole to fixate the passwords for connection & host? I would like to automate the connecting process, but I guess that is not possible with the random password generation at each start?
Yes, you can fix the password generation; if you start Wormhole.exe from the commandline you can pass `--password` and `--hostpassword` which will prevent the automatic generation of passwords. Additionally, you can also pass `--port` to manually fix the port
