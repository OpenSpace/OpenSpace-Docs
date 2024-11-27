



(core_configuration)=
# Configuration




## Members


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `FontSize`
    - Information about the hardcoded fontsizes used by the rendering engine itself
    - `Table`
    
    -   [Table parameters](#ConfigurationFontSize-target) 
    
    - {bdg-info}`No`
    
*   - `Paths`
    - A list of paths that are automatically registered with the file system. If a key X is used in the table, it is then useable by referencing ${X} in all other configuration files or scripts
    - `Table`
    
    -   [Table parameters](#ConfigurationPaths-target) 
    
    - {bdg-info}`No`
    
*   - `Asset`
    - The scene description that is used to populate the application after startup. The scene determines which objects are loaded, the startup time and other scene-specific settings. More information is provided in the Scene documentation. If the 'Asset' and the 'Profile' values are specified, the asset is silently ignored
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `BypassLauncher`
    - If this value is set to 'true', the launcher will not be shown and OpenSpace will start with the provided configuration options directly. Useful in multiprojector setups where a launcher window would be undesired
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `CheckOpenGLState`
    - Determines whether the OpenGL state is checked after each OpenGL function call. This will dramatically slow down the rendering, but will make finding OpenGL errors easier. This defaults to 'false'
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ConsoleKey`
    - / Determines which key opens the in-game console. The value passed in must be a / valid key (see keys.h for a list)
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `DisableInGameConsole`
    - If this value is set to 'true' the ingame console is disabled, locking the system down against random access
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `DisableRenderingOnMaster`
    - Toggles whether the master in a multi-application setup should be rendering or just managing the state of the network. This is desired in cases where the master computer does not have the resources to render a scene
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Documentation`
    - Right now only contains the path where the documentation is written to
    - `Table`
    
    -   [Table parameters](#ConfigurationDocumentation-target) 
    
    - Yes
    
*   - `Fonts`
    - A list of all fonts that will automatically be loaded on startup. Each key-value pair contained in the table will become the name and the file for a font
    - `Table`
    
    -   [Table parameters](#ConfigurationFonts-target) 
    
    - Yes
    
*   - `GlobalCustomizationScripts`
    - This value names a list of scripts that get executed after initialization of any scene. These scripts can be used for user-specific customization, such as a global rebinding of keys from the default
    - `Table`
    
    -   [Table parameters](#ConfigurationGlobalCustomizationScripts-target) 
    
    - Yes
    
*   - `GlobalRotation`
    - Applies a global view rotation. Use this to rotate the position of the focus node away from the default location on the screen. This setting persists even when a new focus node is selected. Defined using roll, pitch, yaw in radians
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `HttpProxy`
    - This defines the use for a proxy when fetching data over http. No proxy will be used if this is left out
    - `Table`
    
    -   [Table parameters](#ConfigurationHttpProxy-target) 
    
    - Yes
    
*   - `LayerServer`
    - Set which layer server should be preferd to be used, the options are "All", "NewYork", "Sweden", "Utah" and "None".
    - `String`
    
    - In list { All, NewYork, Sweden, Utah, None } 
    
    - Yes
    
*   - `LoadingScreen`
    - Values in this table describe the behavior of the loading screen that is displayed while the scene graph is created and initialized
    - `Table`
    
    -   [Table parameters](#ConfigurationLoadingScreen-target) 
    
    - Yes
    
*   - `LogEachOpenGLCall`
    - Determines whether each OpenGL call that happens should be logged using the 'TRACE' loglevel. This will bring the rendering to a crawl but provides useful debugging features for the order in which OpenGL calls occur. This defaults to 'false'
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Logging`
    - Configurations for the logging of messages that are generated throughout the code and are useful for debugging potential errors or other information
    - `Table`
    
    -   [Table parameters](#ConfigurationLogging-target) 
    
    - Yes
    
*   - `MasterRotation`
    - Applies a view rotation for only the master node, defined using roll, pitch yaw in radians. This can be used to compensate the master view direction for tilted display systems in clustered immersive environments
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `ModuleConfigurations`
    - Configurations for each module
    - `Table`
    
    -   [Table parameters](#ConfigurationModuleConfigurations-target) 
    
    - Yes
    
*   - `OnScreenTextScaling`
    - The method for scaling the onscreen text in the window. As the resolution of the rendering can be different from the size of the window, the onscreen text can either be scaled according to the window size ('window'), or the rendering resolution ('framebuffer'). This value defaults to 'window'
    - `String`
    
    - In list { window, framebuffer } 
    
    - Yes
    
*   - `OpenGLDebugContext`
    - Determines the settings for the creation of an OpenGL debug context
    - `Table`
    
    -   [Table parameters](#ConfigurationOpenGLDebugContext-target) 
    
    - Yes
    
*   - `PerProfileCache`
    - If this is set to 'true', the name of the profile will be appended to the cache directory, thus not reusing the same directory. This is useful in cases where the same instance of OpenSpace is run with multiple profiles, but the caches should be retained. This value defaults to 'false'
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `PrintEvents`
    - Determines whether events are printed as debug messages to the console each frame. If this value is set it determines the default value of the property of the OpenSpaceEngine with the same name
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Profile`
    - The profile that should be loaded at the startup. The profile determines which assets are loaded, the startup time, keyboard shortcuts, and other settings.
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `PropertyVisibility`
    - Determines the property visibility level that is selected when starting up OpenSpace. If it is not provided, it defaults to 'User'
    - `String`
    
    - In list { NoviceUser, User, AdvancedUser, Developer } 
    
    - Yes
    
*   - `ScreenshotUseDate`
    - Toggles whether screenshots generated by OpenSpace contain the date when the concrete OpenSpace instance was started. This value is enabled by default, but it is advised to disable this value if rendering sessions of individual frames pass beyond local midnight
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ScreenSpaceRotation`
    - Applies a global rotation for all screenspace renderables. Defined using roll, pitch, yaw in radians
    - `Vector3<double>`
    
    - Value of type 'Vector3<double>' 
    
    - Yes
    
*   - `ScriptLog`
    - The file that will be created on startup containing the log of all Lua scripts that are executed in the last session. Any existing file (including the results from previous runs) will be silently overwritten
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `ScriptLogRotation`
    - If this value is specified, this many number of script log files are being retained before overwriting any
    - `Integer`
    
    - Value of type 'Integer' 
    
    - Yes
    
*   - `SGCTConfig`
    - The SGCT configuration file that determines the window and view frustum settings that are being used when OpenSpace is started
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `ShutdownCountdown`
    - The countdown that the application will wait between pressing ESC and actually shutting down. If ESC is pressed again in this time, the shutdown is aborted
    - `Double`
    
    - Greater than: 0 
    
    - Yes
    
*   - `UseMultithreadedInitialization`
    - This value determines whether the initialization of the scene graph should occur multithreaded, that is, whether multiple scene graph nodes should initialize in parallel. The only use for this value is to disable it for debugging support
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `VersionCheckUrl`
    - The URL that is pinged to check which version of OpenSpace is the most current if you don't want this request to happen, this value should not be set at all
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::







(ConfigurationFontSize-target)=
::::{dropdown} Table parameters for `FontSize`
Information about the hardcoded fontsizes used by the rendering engine itself


* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `CameraInfo`
    - The font size (in pt) used for printing the camera friction state
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `FrameInfo`
    - The font size (in pt) used for printing optional information about the currently rendered frame
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Log`
    - The font size (in pt) used for rendering the screen log
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `Shutdown`
    - The font size (in pt) used for rendering the shutdown text
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
*   - `VersionInfo`
    - The font size (in pt) used for printing the version information
    - `Double`
    
    - Value of type 'Double' 
    
    - {bdg-info}`No`
    
:::



::::




(ConfigurationPaths-target)=
::::{dropdown} Table parameters for `Paths`
A list of paths that are automatically registered with the file system. If a key X is used in the table, it is then useable by referencing ${X} in all other configuration files or scripts


* Optional: {bdg-info}`No`


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
:::



::::
















(ConfigurationDocumentation-target)=
::::{dropdown} Table parameters for `Documentation`
Right now only contains the path where the documentation is written to


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Path`
    - The path where the documentation files will be stored
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::




(ConfigurationFonts-target)=
::::{dropdown} Table parameters for `Fonts`
A list of all fonts that will automatically be loaded on startup. Each key-value pair contained in the table will become the name and the file for a font


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
:::



::::




(ConfigurationGlobalCustomizationScripts-target)=
::::{dropdown} Table parameters for `GlobalCustomizationScripts`
This value names a list of scripts that get executed after initialization of any scene. These scripts can be used for user-specific customization, such as a global rebinding of keys from the default


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::






(ConfigurationHttpProxy-target)=
::::{dropdown} Table parameters for `HttpProxy`
This defines the use for a proxy when fetching data over http. No proxy will be used if this is left out


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Activate`
    - Determines whether the proxy is being used
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Address`
    - The address of the http proxy
    - `String`
    
    - Value of type 'String' 
    
    - {bdg-info}`No`
    
*   - `Authentication`
    - The authentication method of the http proxy
    - `String`
    
    - In list { basic, ntlm, digest, any } 
    
    - Yes
    
*   - `Password`
    - The password of the http proxy
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
*   - `Port`
    - The port of the http proxy
    - `Integer`
    
    - In range: ( 0,65536 ) 
    
    - {bdg-info}`No`
    
*   - `User`
    - The user of the http proxy
    - `String`
    
    - Value of type 'String' 
    
    - Yes
    
:::



::::






(ConfigurationLoadingScreen-target)=
::::{dropdown} Table parameters for `LoadingScreen`
Values in this table describe the behavior of the loading screen that is displayed while the scene graph is created and initialized


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `ShowLogMessages`
    - If this value is set to 'true', the loading screen will display a list of warning and error messages
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ShowMessage`
    - If this value is set to 'true', the loading screen will display a message information about the current phase the loading is in
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `ShowNodeNames`
    - If this value is set to 'true', the loading screen will display a list of all of the nodes with their respective status (created, loaded, initialized)
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



::::






(ConfigurationLogging-target)=
::::{dropdown} Table parameters for `Logging`
Configurations for the logging of messages that are generated throughout the code and are useful for debugging potential errors or other information


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `CapabilitiesVerbosity`
    - At startup, a list of system capabilities is created and logged. This value determines how verbose this listing should be
    - `String`
    
    - In list { None, Minimal, Default, Full } 
    
    - Yes
    
*   - `ImmediateFlush`
    - Determines whether error messages will be displayed immediately or if it is acceptable to have a short delay, but being more performant. If the delay is allowed ('true'), messages might get lost if the application crashes shortly after a message was logged
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `LogLevel`
    - The severity of log messages that will be displayed. Only messages of the selected level or higher will be displayed. All levels below will be silently discarded. The order of severities is: Debug < Info < Warning < Error < Fatal < None.
    - `String`
    
    - In list { Trace, Debug, Info, Warning, Error, Fatal, None } 
    
    - Yes
    
*   - `Logs`
    - Per default, log messages are written to the console, the onscreen text, and (if available) the Visual Studio output window. This table can define other logging methods that will be used additionally
    - `Table`
    
    -   [Table parameters](#ConfigurationLoggingLogs-target) 
    
    - Yes
    
:::



(ConfigurationLoggingLogs-target)=
#### Table parameters for `Logs`
Per default, log messages are written to the console, the onscreen text, and (if available) the Visual Studio output window. This table can define other logging methods that will be used additionally


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Table`
    
    - [LogFactory](#core_logfactory)
    
    - Yes
    
:::




::::






(ConfigurationModuleConfigurations-target)=
::::{dropdown} Table parameters for `ModuleConfigurations`
Configurations for each module


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `Table`
    
    -  
    
    - {bdg-info}`No`
    
:::



::::






(ConfigurationOpenGLDebugContext-target)=
::::{dropdown} Table parameters for `OpenGLDebugContext`
Determines the settings for the creation of an OpenGL debug context


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Activate`
    - Determines whether the OpenGL context should be a debug context
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - {bdg-info}`No`
    
*   - `FilterIdentifier`
    - A list of OpenGL debug messages identifiers that are filtered
    - `Table`
    
    -   [Table parameters](#ConfigurationOpenGLDebugContextFilterIdentifier-target) 
    
    - Yes
    
*   - `FilterSeverity`
    - Determines the settings for the creation of an OpenGL debug context
    - `Table`
    
    -   [Table parameters](#ConfigurationOpenGLDebugContextFilterSeverity-target) 
    
    - Yes
    
*   - `PrintStacktrace`
    - If this is set to 'true', everytime an OpenGL error is logged, the full stacktrace leading to the error is printed as well, making debugging under production situations much easier
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
*   - `Synchronous`
    - Determines whether the OpenGL debug callbacks are performed synchronously. If set to 'true' the callbacks are in the same thread as the context and in the scope of the OpenGL function that triggered the message. The default value is 'true'
    - `Boolean`
    
    - Value of type 'Boolean' 
    
    - Yes
    
:::



(ConfigurationOpenGLDebugContextFilterIdentifier-target)=
#### Table parameters for `FilterIdentifier`
A list of OpenGL debug messages identifiers that are filtered


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - Individual OpenGL debug message identifiers
    - `Table`
    
    -   [Table parameters](#ConfigurationFilterIdentifier*-target) 
    
    - Yes
    
:::



(ConfigurationFilterIdentifier*-target)=
#### Table parameters for `*`
Individual OpenGL debug message identifiers


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `Identifier`
    - The identifier that is to be filtered
    - `Integer`
    
    - Value of type 'Integer' 
    
    - {bdg-info}`No`
    
*   - `Source`
    - The source of the identifier to be filtered
    - `String`
    
    - In list { API, Window System, Shader Compiler, Third Party, Application, Other, Don't care } 
    
    - {bdg-info}`No`
    
*   - `Type`
    - The type of the identifier to be filtered
    - `String`
    
    - In list { Error, Deprecated, Undefined, Portability, Performance, Marker, Push group, Pop group, Other, Don't care } 
    
    - {bdg-info}`No`
    
:::





(ConfigurationOpenGLDebugContextFilterSeverity-target)=
#### Table parameters for `FilterSeverity`
Determines the settings for the creation of an OpenGL debug context


* Optional: Yes


:::{list-table}
:width: 100%
:widths: 3 16 1 4 1
:header-rows: 1
*   - Name
    - Documentation
    - Type
    - Description
    - Optional

*   - `*`
    - 
    - `String`
    
    - In list { High, Medium, Low, Notification } 
    
    - Yes
    
:::




::::



























