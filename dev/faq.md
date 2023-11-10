# FAQ

## Configuration
### Is it possible to run OpenSpace in kiosk mode and mask the display area ?
There are two steps and two options to achieving what I think you want;
1. To hide the GUI elements you can add the following script to the `.scene` file that you are using:
```lua
openspace.setPropertyValueSingle('Modules.CefWebGui.Visible', false);
openspace.setPropertyValueSingle('Dashboard.IsEnabled', false);
openspace.setPropertyValueSingle("RenderEngine.ShowLog", false);
openspace.setPropertyValueSingle("RenderEngine.ShowVersion", false);
openspace.setPropertyValueSingle("RenderEngine.ShowCamera", false);
```

2. There are two options for the masking:
  a. Copy the `single.xml` from the `config` folder and give it a new name (`single-possize.xml` in my case; my version attached here). In the `openspace.cfg` replace `SGCTConfig = sgct.config.single{}` with `SGCTConfig = "${CONFIG}/single-masked.xml` to use it. In the XML file modify lines 12 and 13. Both `Pos` and `Size` are in values from 0 to 1, so in my example i move the rendering window up to the top right by a quarter of the screen size.
b. Same first steps as (a) but instead of modifying the Pos and Size (example as `single-masked.xml`) you add `mask="mask.png"` to the `Viewport` tag. You can choose whichever filename you like. The image should be a black/white image image; the rendering is masked out where the image is black, shown where it is white. Please not that the `mask.png` has to be in the same folder as the `OpenSpace.exe` for this to work

http://data.openspaceproject.com/faq/mask.png
http://data.openspaceproject.com/faq/single-masked.xml
http://data.openspaceproject.com/faq/single-possize.xml

## Wormhole
### Is there a way to configure the Wormhole to fixate the passwords for connection & host? I would like to automate the connecting process, but I guess that is not possible with the random password generation at each start?
Yes, you can fix the password generation; if you start Wormhole.exe from the commandline you can pass `--password` and `--hostpassword` which will prevent the automatic generation of passwords. Additionally, you can also pass `--port` to manually fix the port

## Compiling
### MacOS
#### While running CMake , `No CMAKE_C_COMPILER could be found` or `No CMAKE_CXX_COMPILER could be found`
Running
`sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer`
before starting CMake can fix this if Xcode is installed on the machine.
