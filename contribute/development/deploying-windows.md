# Deploying Windows
You've got your Visual Studio build running smoothly on your development machine. There's a simple way to deploy OpenSpace to another machine without installing lots of libraries and building it again - you can merely copy the necessary files to a new location.


## Deploy OpenSpace
To create a distributable version of OpenSpace, you need to execute the `deploy.bat` file that you can find in the root folder of OpenSpace. This will create a fresh build and when it is done, place a `OpenSpace.zip` file in the root. You can copy that file to another machine and extract it to "install" OpenSpace there. The new machine will require the Visual C++ run-time libraries ("redistributables"). If the "redistributables" is not installed, you can download the correct libraries from [Microsoft](https://aka.ms/vs/17/release/vc_redist.x64.exe)
