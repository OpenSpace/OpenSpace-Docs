# Windows
This page contains specific information necessary to compile OpenSpace on Windows. This page has the [general instructions](index) as a required reading.

## Development Tools
[Visual Studio 2022](http://www.visualstudio.com) is the standard Interactive Development Environment (IDE) for Windows. The "community" version is a free download for open-source projects. When you install it, be sure to select "Custom" configuration and select the C++ compiler -- it might not be included by default. You can also select a git client here ("Git GUI"). Installation could take a while (like an hour or so, depending on the machine). We are following the development of the C++ language quite closely, so there are more and more features that are no longer supported in Visual Studio 2019 or earlier versions.

## Dependencies
### Qt
Make sure to install the [Qt](https://www.qt.io/download) version that is called `MSVC 2019 64-bit`. After installing you should add the `bin` folder from the installation to your `PATH` environment variable, and it is highly recommended to have only one Qt `bin` folder in this variable (e.g. no different versions). It is possible to copy specific Qt .dll files from the Qt `bin` folder to the OpenSpace `bin` folder, but this is discouraged. Having both the Qt `bin` folder set in path **and** the dll files copied to OpenSpace `bin` might cause the program to crash.


## Notes
### Git
You might find it easier to [use SSH](https://help.github.com/articles/generating-an-ssh-key/) instead of HTTPS, especially if you're using Two-Factor Authentication with GitHub.

If you use the command line interface for `git`, remember that OpenSpace has many submodules. You'll need to use `git clone --recursive` and/or use the `git submodule` commands. The `submodule` commands will need to be run in both the main repository and `ext/ghoul`.

### Visual Studio
The `Release` mode currently does not run correctly due to an [issue](https://github.com/OpenSpace/OpenSpace/issues/1657) with dependent libraries. Instead, use the `RelWithDebInfo` which has almost identical performance as the `Release` mode, but also provides information to debug potential crashes.

### Deploying
If you want to build OpenSpace to deploy to a third party that does not have a development environment, you can use the `deploy.bat` file found in the `support` folder. When starting this batch file, it will automatically build a fresh version of OpenSpace that includes the `sync` and `user` folder. The result of the deployment is a `.zip` file that can be shared with other computers that are then able to extract the file and run the application directly.

### FAQ
If Windows is complaining that it cannot find the `VCOMP120.dll`, download the [Visual Studio Redistributable](https://aka.ms/vs/16/release/vc_redist.x64.exe). On Windows 10 and up, this is not installed by default anymore. In general, this shouldn't be an issue if you have Visual Studio installed correctly, but it will be necessary to install on other computers that do not have the IDE installed.
