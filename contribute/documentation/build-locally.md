# How to build the documentation locally

If you would like to contribute to the documentation, it can be a good idea to try out how the additions will look. This can be done by building the documentation locally. The documentation repository is [OpenSpace-Docs](https://github.com/OpenSpace/OpenSpace-Docs). It uses [Sphinx](https://www.sphinx-doc.org) to build the documentation that is hosted on [Read the docs](https://about.readthedocs.com/). 

The documentation uses two `JSON` files for the reference section. These `JSON` files are generated from the OpenSpace engine with an application called `DocsWriter`. These JSON files are updated manually to the `OpenSpace-Docs/json` folder. It is possible to build the documentation locally without generating new `JSON` files for the reference section.

## Build the documentation locally

1. Clone the [`OpenSpace-Docs`](https://github.com/OpenSpace/OpenSpace-Docs) repository.

2. Open the `OpenSpace-Docs` folder in a command prompt. Run the command `python -m venv .venv` to set up a virtual environment for python. If you wish, you may rename your environment to something else than `.venv`.

3. Run the command `.\.venv\Scripts\activate` to activate your python virtual environment.

4. Run the command `pip install sphinx`. This will install Sphinx, which is the documentation package used to generate the documentation.

5. Run the command `pip install -U sphinx`. This will install all dependencies. Now we have set up our environment. 

6. (optional) If you generated the JSON files for the OpenSpace reference, move the two generated files `assetComponents.json` and `scriptingApi.json` to the `OpenSpace-Docs/json` folder.

7. Run the command `make html` to generate the documentation webpage. To view it, open the `build` folder and open the `html/index.html` file in a browser.

:::{note} Note about the asset examples
The documentation uses the assets folder in OpenSpace to create examples for the `Asset Components` reference section. Per default, the script `make html` will download a partial clone of the OpenSpace repository (only the assets folder) from the _latest master_ and then generate the documentation.

* **Remote branch**
  If you wish to configure the asset examples to be created from another remote Git branch, you may change the name of the `OPENSPACE_BRANCH` variable in the `conf.py`-file. Whatever branch name you write here will be downloaded and used for the assets examples. The only requirement is that the branch has to be on `origin`. 

* **Local branch**
  If you instead wish to use a local copy of OpenSpace for the assets examples, you may use the variable called `LOCAL_OPENSPACE_FOLDER` in `conf.py`. If this variable is set, it will not use the branch from `origin`, but instead use a local copy of OpenSpace for the asset examples. The variable should be an absolute path.
:::

## Generate OpenSpace reference (optional)
If you have updated documentation for the Scripting API or the Asset Components in the engine, you might want to view these changes in the documentation. The following steps describe how to do this.

1. Open your OpenSpace project in CMake and enable the `OPENSPACE_APPLICATION_DOCSWRITER` checkbox in CMake. Re-generate the project.

![Enable the Cmake checkbox for the DocWriter](./cmake_docswriter.png) 

3. Once we have a project where the DocsWriter is generated, make the DocsWriter your startup project in Visual Studio.

4. Build and run the DocsWriter project. This will generate two JSON files in the `documentation` folder: `assetComponents.json` and `scriptingApi.json`.

5. If you wish to update the reference data for your locally built documentation webpage, replace the files with the same names in your `OpenSpace-Docs/json` folder with these two files (see step 6 in "Build the documentation locally").

Done!

