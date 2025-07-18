# Multi-node Site Configuration

## Installing & Running OpenSpace in a site which uses multiple projector nodes

This page contains some notes  - pointers for getting OpenSpace to run in a multi-node setup, most commonly used in planetariums. Special thanks to Dan Tell of [Tau Immersive LLC](https://tauimmersive.com/) for sharing much of the content. The [E&S Site Configuration page](cosm) has some Digistar-specific details. Though this document is written with Windows as the operating system running OpenSpace, the same concepts would apply to all OSes.

### The OpenSpace directory and config file

#### Configuration file overview

`openspace.cfg` lives in the root directory of your OpenSpace-\[version\] folder. You can open it in any text editor of your choice. There are other folders inside the your OpenSpace-\[version\] folder which are important for synchronizing data between the nodes of your multi-node setup - these are described later in this document. 

`openSpace.cfg` is used to customize the behaviour of OpenSpace. Near the top of the file, you
can assign what the default launch configuration for your install will be, by editing the 
`SGCTConfig` property. If we comment out the default

`SGCTConfig = sgct.config.single{vsync=false}` 

we can
uncomment another configuration, say 

`SGCTConfig = sgct.config.fisheye{1024, 1024}` 

and now when we open the launcher, that will appear as our default configuration. We can also choose custom configurations we have written for our system - an example two-node configuration file is provided along with OpenSpace, in the `config/two_nodes.json` file.

Similarly, in the Profiles section of the `openSpace.cfg` file, we can comment out the profiles we don't need, and uncomment only the profile we need.

Once we have set up the profiles and configurations and the system is ready, we can also completely bypass the launcher - for this, search the `openSpace.cfg` file for "Bypass": and you’ll find the `BypassLauncher` setting. Set this to `true` to start OpenSpace without the launcher, opening the profile and configuration which you have set in `openSpace.cfg` as the default.

There are many other adjustments we can make in the configuration file. For example, we can specify the
default user level to always have the `AdvancedUser` level on a
production system. This would make all the advanced menu options visible in the OpenSpace GUI.  

We can also change the path settings for where OpenSpace looks for files, in the `Paths:` section of `openSpace.cfg`. 

There are parts in `openSpace.cfg` where we need to change settings to allow access to OpenSpace's GUI from external devices - the `Server`, `WebBrowser` and `WebGui` sections as mentioned in the [Controlling OpenSpace remotely](remote-control) page.

And we can even adjust the available map data servers, with the `LayerServer` property.

#### Other folders

On first startup, OpenSpace will create some directories like the `user` folder in locations specified by the `openSpace.cfg` - the default location uses the OpenSpace folder as the parent directory. You can start up all the nodes once using the method described in the section below, and synchronize the data between the nodes later.

### C-Troll and external launchers

Launching OpenSpace on multiple nodes simultaneously can be done with scripts, or using GUI tools like [C-Troll](https://github.com/c-toolbox/C-Troll). Detailed documentation for using C-Troll is available at the [github page](https://github.com/c-toolbox/C-Troll). The most important points to note would be the `-p` and `-c` command-line options for OpenSpace, which load the specified profile and configuration respectively, as below:

`\[directorypath\]/OpenSpace.exe -p \[profilename\] -c {$CONFIG}/\[configuration\].json`

Also, note that in case not already set up, some firewall and Windows settings would need to be done as mentioned in the [E&S Site Configuration page](cosm).

### Synchronizing data between the nodes

OpenSpace does not have a built-in data synchronization routine, but you can easily synchronize data and configuration files
across a Windows cluster with Windows Robust File Copy, [robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy). Robocopy can run about 3x faster
than copying through the Windows GUI and can be set up with additional options for improved
synchronization.

You can write a robocopy script into a Windows batch (`.bat`) file to easily automate and run it. An
example might look like this:
```
::set variables
set OPENSPACE_DIR=D:\OpenSpace\OpenSpace-0.21.0
set OPENSPACE_USER_DIR=D:\OpenSpace\OpenSpace-0.21.0\user
set OPENSPACE_DATA_DIR= D:\OpenSpace\OpenSpaceData
::start nodes
FOR %%i in (101,102,103,104,105,106) DO (
robocopy %OPENSPACE_USER_DIR%
\\192.168.1.%%i\%OPENSPACE_USER_DIR% /XO /S
)
```

In the above example, OpenSpace is located on the `D:` of all machines in a cluster with IP
addresses between 192.168.1.101 and 106 (the master would be a different IP, perhaps 100).
Running this routine will synchronize all files in the master OpenSpace user directory to the
same directory across the cluster. The `/XO` flag ensures that it only updates files that are newer
than the versions on the cluster, while the `/S` flag provides recursive sync for all subdirectories.
Make sure to carefully test any robocopy script first and back up files before the first time you
run it.

This can also be used to synchronize the main OpenSpace data directories as well, and the
OpenSpaceData folder to more quickly copy map data over. If using it to sync the default
directories, including the `/XD` flag is recommended, which will exclude directories you don’t need
to sync – excluding at least `cache` and `mrf_cache` directories is recommended.

### Generating Configuration Files and running the system

The configuration file generation and other steps needed to run a multi-node system are described in more detail in the [E&S Site Configuration page](cosm).
