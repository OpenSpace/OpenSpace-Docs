# Configuration

OpenSpace uses a configuration file which is called `openspace.cfg`. This file is located in the OpenSpace folder. This file determines:

- The SGCT configuration (the type of projection and number of windows)

- The profile set on startup

- The paths where OpenSpace can find files

- The default visibility level for properties

- Configurations for modules

- Fonts and font sizes

- Log and script log outputs

...and a number of other configurations. For complete documentation with regards to the config file, please refer to [this page](#core_configuration).

## Environment variables

Some of the configurations in the config file can use environment variables. These can be very handy if you use OpenSpace a lot, as they will speed up and / or customize your setup automatically. The environment variables are set as Path variables in a Windows environment. The environment variables are:

- `OPENSPACE_SYNC`: The `sync` folder is where OpenSpace stores all downloaded data, such as models, maps, textures, etc. If this environment variable is set, the `sync` folder (which normally is placed inside the OpenSpace folder) can be placed anywhere on your computer. This is very handy if you are using multiple versions of OpenSpace, for the following reasons:

  - If you get a fresh build of OpenSpace you don’t need to download the data again, if you already have the data on disk. This will save you time on startup.

  - If you have multiple instances of OpenSpace, the required storage space on your disk will lessen as you only need to store the data once as the `sync` folder can be reused across multiple OpenSpace versions.

- `OPENSPACE_USER`: The `user` folder is meant to be used for all user created files. These include webpanels, bookmarks, recordings, screenshots, data, and configs. If this environment variable is set, the `user` folder which normally is placed inside the OpenSpace folder, can be placed anywhere on your computer. This is very handy if you are using multiple versions of OpenSpace, for the following reasons:

  - You can have one "global" folder for all your OpenSpace data, and all your OpenSpace instances will find it.

  - It might save you space as you don't have to store data in multiple places.

- `OPENSPACE_GLOBEBROWSING` If this environment variable is set, the OpenSpaceData folder which normally is placed one level above the OpenSpace folder, can be placed anywhere on your computer. This folder stored all the map data from planets. This is very handy if you are using multiple versions of OpenSpace, for the following reasons:

  - Faster loading of map tiles that you have already visited.

  - Less storage space as all instances of OpenSpace will use the same data.

- `OPENSPACE_LEVEL` If this environment variable is set, the Property Visibility level will be determined on startup. The property visibility level is a setting that determines how complex the user interface should be. If you select `User`, for example, it means you won't see the more advanced properties that will be visible if you select `AdvancedUser`. The levels are:

  - `NoviceUser`

  - `User`

  - `AdvancedUser`

  - `Developer`
