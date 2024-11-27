# Controlling OpenSpace remotely

For remotely starting up OpenSpace, remote control tools like Remote Desktop or SSH can be used. A set of scripts for starting up OpenSpace 
over SSH has been shared [on github.](https://gist.github.com/curiousercreative/84d70417bbbb183bf68043b8b1127d65)
Once OpenSpace is running, there are several ways in which OpenSpace can be controlled remotely over the network, from another computer or device.

1. Using the [html-based button pages](/creating-data-assets/custom-web-ui/html-controls-setup/index) served from the computer running OpenSpace. 
Note that this will work without modification only if the browser is run on the same computer which is running OpenSpace, 
for example using Remote Desktop on Windows or VNC for Linux. 
Read on below for configuration changes needed, if you want to run a web server on the local machine and access it from a browser on a remote system. 
   
2. Using the Web GUI - The main gui of the OpenSpace project as seen in the screenshots on the [Getting Started](/getting-started/index) page
can be accessed via a browser at port 4680, for example if the computer's IP address is 10.0.0.3, then the GUI can be accessed at: `http://10.0.0.3:4680` - but some configuration changes are needed as noted below.

The web interface can be made accessible to other devices by modifying the settings. This can be done by editing the `openspace.cfg` file, which would then cause the changes made
to apply to all users of the installation. In the `.cfg` file, both the ip addresses, of the remote client as well as of the machine running OpenSpace,
need to be entered, (for example, if OpenSpace is running on a computer with IP address of 10.0.0.3 and the remote client's IP address is 10.0.0.7)
```
    Server = {
        AllowAddresses = { "127.0.0.1", "localhost", "10.0.0.3", "10.0.0.7" },
        ...
    },
    ...
    WebGui = {
        Address = "10.0.0.3",
        ...
    },

```

OR temporary changes can be made through the UI by first changing the "Property Visibility" setting in the UI from "User" to "Advanced User" under {menuselection}`Settings --> OpenSpace Engine`. Once that is done, change the allowed addresses at {menuselection}`Settings --> Server --> Interfaces --> DefaultWebSocketInterface` to include both the client and the server addresses along with localhost,
or change the default access to "Allow" from "Deny". These changes will not be reflected next time OpenSpace is launched.
