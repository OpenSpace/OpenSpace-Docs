# E&S Site Configuration

## Installing & Running OpenSpace in a COSM/E&S Digistar Dome

This document contains details for getting OpenSpace to run in a COSM / Evans & Sutherland Digistar planetarium. Each planetarium has unique features, so this document is not guaranteed to contain all of the necessary instructions to run OpenSpace.

### Typical System Overview
A Digistar system uses a host computer used to control the planetarium display. The host (DSHOST) is networked to multiple Digi Star Graphics Processor (DSGP) computers which render the content and send output to projectors.
The output of each DSGP runs through a proprietary sync card that uses the upper-left pixel data as a frame number to synchronize all channels. This sync card does not appear to interfere with the identification of the projector in Windows. The hostname pattern is `DSGP#`, and IP address pattern is `192.168.2.1#`

### Configure All Digistar Computers Prior to OpenSpace Installation
The following installation and configuration steps will need to be done on the DSHOST and all DSGP computers in the system. The work on each DSGP computer can be done by starting a Windows Remote Desktop Session from the DSHOST to that computer, or by accessing the remote drives in the file manager (e.g. typing `\\DSGP3\C$` in the file manager URL bar will provide access to the C:\\ drive on DSGP3). If Windows requires credentials, use those provided in the [COSM internal wiki page](https://internal.openspaceproject.com/en/misc/ens-site-configuration).

#### Install Additional Software
Before OpenSpace can be installed, the DSHOST and DSGPs need to have a few software utilities installed. These are listed below, along with a description of what they do and why they are necessary:
1. **C-Troll** - A Windows-only application suite that provides the ability to control the OpenSpace application in the Digistar cluster (DSHOST + DSGPs). This software can be found [here](https://github.com/c-toolbox/C-Troll).
2. **Microsoft Visual C++ Redistributable for Visual Studio 2017** - This is not required in all cases but should be installed anyway on all computers. It can be downloaded from [here](https://www.visualstudio.com/downloads/).

#### Configure Windows Settings
The following configuration settings are probably already done, but should still be checked on the DSHOST _and_ all DSGPs. 
* Each computer needs to have file and print sharing enabled
* Each computer needs to be able to see all others in the **Network** section of the File manager
* The default **Admin$** share is defined

#### Configure Windows Firewall
All computers in the system must have firewall rules to allow TCP incoming & outgoing traffic for the ports specified in the SGCT config file (shown below). For this system, rules were set for ports 20400-20420. Follow these steps to set firewall rules:
  1. Open **Control Panel** and select **Windows Firewall** and then **Advanced Settings**
  2. Select "Inbound Rules" and a new dialog box will appear
  3. Select "New Rule"
  4. Select "Port" then click Next
  5. Select "TCP" and type ports 20400-20420 in the ports text box, then click Next
  6. Select "Allow the Connection", then click Next
  7. Ensure that the rule is accepted for all profiles (all checked), then click Next
  8. Type "OpenSpace" for a rule name and click Exit to accept this new rule
  9. Now back in the **Advanced Settings** window for the firewall, select "Outbound Rules", and go back to step 3 above to apply the TCP rule for the same ports

#### Generate Configuration Files for the Dome
Digistar software contains a CreateMPCDI.exe utility that will read the configuration/calibration files and generate an .mpcdi file for the dome. The utility is located somewhere in the Digistar installation directory. A Digistar version that contains updates from June 2024 or later will contain the necessary changes that fix the projection distortion.
Running it on the system's main (DSHOST) computer will create a file (probably called SystemConfiguration.mpcdi) for the dome.

The next steps will convert the .mpcdi file into an SGCT configuration file that OpenSpace can use.
1. Rename the .mpcdi file with a .zip extension.
2. Extract/unzip the contents
3. Move the .pfm files to OpenSpace/config/mesh/.
4. Use the [OpenSpace tools server](https://tools.openspaceproject.com/)'s COSM configuration file converter to upload & convert the extracted mpcdi.xml file.
5. In order to make this translation work from the COSM/E&S MPCDI warping, OpenSpace needs to render an FOV from which a smaller area will be extracted and warped to fit the necessary dome distortion. This means that some of what OpenSpace renders will not be used. In some dome configurations, the warping required for each projector may be extreme enough that the resulting resolution is low quality due to a small portion of the rendered result being expanded to fit the projector's output resolution. A solution for this is to increase the resolution of the content that OpenSpace renders, so that when a smaller portion of this rendered window is expanded, the result will look good. This can be done by leaving the `size` entry to be the projector's default resolution, but adding a `res` entry with x and y values that are larger than the `size` values. The `res` values should have the same aspect ratio, but scaled up to compensate for the distortion. The amount of the scaling is up to the user, but it should be proportional to how much the image is warped, because while increased scaling improves the resolution quality, it also reduces the framerate.
6. Move the resulting mpcdi.json file to OpenSpace/config/, and rename it if desired.

### Create a Staging Directory for the OpenSpace installation
The staging directory will contain all of the files necessary to constitute a working OpenSpace software install for each DSGP. It is best to start with a full version of OpenSpace (minimal install _plus_ the necessary download data). This staging area can be on the Digistar DSHOST computer, or on an external drive (e.g. USB drive) that will be used to copy to the computers at the time of installation. This directory will reside in C:\OpenSpace, and should contain:
1. The OpenSpace software folder, which might be a release version or a custom-built version.
2. The resulting .json configuration file obtained by converting the COSM MPCDI file via the tools conversion page.
3. C-Troll software mentioned above. A release can be used without needing to compile a version.
Modify the C:\OpenSpace\openspace.cfg file in the following ways:
1. Set it to use the converted configuration file discussed in the previous section: `SGCTConfig = ${CONFIG}/<config_from_conversion_tool>.json` 
2. Set it to bypass the launcher using this line: `BypassLauncher = true`

### Configure C-Troll
The details of configuring C-Troll can be found at [its repository](https://github.com/c-toolbox/C-Troll), so only the most relevant details are provided here.
Use the C-Troll editor to edit the specific files discussed below.
Create an openspace applications file(applications/openspace.js) containing the `executable` path (e.g. C:/OpenSpace/bin/RelWithDebInfo/OpenSpace.exe), and a `workingDirectory` entry with that same path to OpenSpace.exe.
Create a node file for all computers in the dome, including the host. Create host.json with name `host` and port 20400. The IP address will likely be 192.168.2.99 for a Digistar configuration. Create a `dsgp#.json` file for each DSGP. Each file will contain:
```text
"name": "dsgp#",
"ip": "192.168.2.10#",
"port": 2040#
```
where `#` is the number of the DSGP in its hostname, starting with 1. This assumes that the IP addresses are set according to the pre-assigned DSGP number.
For clusters, create a clusters/dome.json file with all of the node names discussed above contained in an array entry for nodes (e.g. `"nodes": [ "host", "dsgp1", "dsgp2", ... ]`)

### Copy Staging Directory to All Digistar Computers
Once the staging directory has been built with all of the components above, it can be copied to the DSHOST and all DSGP computers. Copy the C:\\OpenSpace\\ directory directly into the C:\\ location on all DSGPs.
After all copying, each DSGP will need to be configured so that it runs the C-Troll Tray.exe on startup. Do this by remote-desktop'ing into each DSGP, pressing the windows logo + R keys, typing `shell:startup` at the prompt, and then pressing Enter. This will open a file browser window in the auto-startup directory. Browse to where OpenSpace.exe resides, then right-click and create a shortcut. Finally, copy that shortcut icon to the auto-startup directory.

### Running OpenSpace on the Entire System
Open C-Troll on the DSHOST and click the OpenSpace application.

