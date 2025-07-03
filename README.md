# OpenSpace Documentation

This repository contains the source of the documentation for OpenSpace. The documentation is written in [MyST](https://myst-parser.readthedocs.io/en/latest/index.html), a Markdown syntax extension, converted into an HTML page using [Sphinx](https://www.sphinx-doc.org/en/master/), and then finally hosted by [Read the Docs](https://about.readthedocs.com/?ref=readthedocs.com) at https://docs.openspaceproject.com.

As of now, the documentation relies heavily of the Godot documentation page for both styling and functionality.

Part of this documentation (the `Reference` section) is generated from `json` objects that have been outputted by the engine. These `json` objects are converted to markdown files with the help of the python script `generatedocs.py`. To do this [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) is used. The jinja templates are stored in the `templates` folder. This `generatedocs.py` script is called in the `conf.py` script. It will (partially) clone the latest master of OpenSpace and download the data assets to generate the examples on the docs page.

Every commit and pull request to this repository will trigger a new build of the documentation. The `master` will build into the "latest" version and each versioned tag is selectable in the flyout menu, with the last version being marked as "stable".

## Building the documentation locally

During the development it is beneficial to build the documentation page locally to see the results before committing something into the repository that fails to build or that produces warnings.

1. In a shell, move to this directory.
2. Run `python -m venv .venv` to create a python virtual environment.
3. Run `.\.venv\Scripts\activate` to activate the python virtual environment.
4. `pip install -r requirements.txt` (this is technically only necessary for the first time or when the dependencies change, but it is a good habit to run this every time after a checkout).
5. (optional) Generate the files for the OpenSpace reference, and alternatively also the asset examples if you want to use versions different than the ones on the origin/master branch. See section "Generate OpenSpace reference" below for details.
6. Run `make html`/`.\make.bat html`.

This will create a `build/html` folder structure that contains a `index.html` which you can open in a webbrowser to view the documentation.

Before committing to the repository it can also be beneficial to run `./make.bat linkcheck` which checks whether all links referenced in the document are actually correct or if we have links that are now dead.

### Make commands

- `make html` will build the documentation locally.
- `make clean` will clean out the build folder and remove everything built previously.
- `make linkcheck` will check so that all links are correct.

### Generate OpenSpace reference (optional)

If you have updated documentation for the Scripting API or the Asset Components (including example files) in the engine, you might want to view these changes in the documentation. The following steps describe how to do this.

1. Set the `generate_reference` variable in `conf.py` to `True`. This will result in the files being regenerated when you run `make html`. Otherwise, the generation is only done if the files do not already exist.

2. (optional) If you are working on example assets, you may also want to change where the source files for those examples are acquired form. Per default, the generation script will download a partial clone of the OpenSpace repository (only the assets folder) from the _latest master_ and then generate the documentation. However, you can change this through the following setting in `conf.py`:

   - `assets_examples_use_github`: Set to `True` to use an OpenSpace repository from Github. Set to `False` to use a local copy or repository.
   - `assets_release`: If using Github, set this string to the branch name (e.g. `origin/feature/feature-branch`), or to a tag name for a specific OpenSpace release (e.g. `releases/0.20.0` for version 0.20.0). If empty, `origin/master` is used.
   - `assets_local_openspace_folder`: If using a local OpenSpace repository, set this string to the path to the OpenSpace folder, e.g. `C:/dev/OpenSpace`.

3. (optional) Generate new `.json` files needed for the documentation using Cmake and Visual Studio. This is only needed if you have made changes in the OpenSpace source code that you want to be reflected on the local build of the documentation page.

   1. Open your OpenSpace project in CMake and enable the `OPENSPACE_APPLICATION_DOCSWRITER` checkbox in CMake. Re-generate the project.

   2. Once we have a project where the DocsWriter is generated, make the DocsWriter your startup project in Visual Studio.

   3. Build and run the DocsWriter project. This will generate two JSON files in the `documentation` folder: `assetComponents.json` and `scriptingApi.json`.

   4. Move the two generated files `assetComponents.json` and `scriptingApi.json` to the `OpenSpace-Docs/json` folder. Replace any existing files.

4. Run `make html`/`.\make.bat html` to build the documentation, as usual.

## File Structure

Each major grouping in the documentation should have a separate folder in the repository that collects all of the files describing things belonging to that major category.

- `generated`: The directory where all generated markdown files will be placed. These will be shown in the `Reference` section of the documentation.
- `templates`: This is where the jinja templates are stored that are used to structure the markdown files.
- `_static`: Files placed in this folder are automatically copied into the resulting documentation. In general, it is not necessary to manually place files in here as Sphinx is copying required files from other places automatically
- `.readthedocs.yml`: A configuration file that sets up the build environment to build the documentation. Documentation for this file can be found [here](https://docs.readthedocs.io/en/stable/config-file/v2.html).
- `conf.py`: A Python script that configures the actual Sphinx instance that builds the documentation page. Documentation for this file can be found [here](https://www.sphinx-doc.org/en/master/usage/configuration.html) and [here](https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html).
- `requirements.txt`: A PIP requirements file that describes all of the Python package requirements that need to be installed.
- `make.bat` / `Makefile`: A batch script for Windows or bash script for Linux to build the documentation. The script needs a second parameter that describes the output type, by default we use `html` for our documentation or `linkcheck` to check whether links in the files are correct. `clean` can be used to remove existing files to build the documentation from scratch, for example via `make.bat clean && make.bat html`.

## Different images for dark and light mode

When adding images that require different files for light-mode and dark-mode, the file should be named normally for the light version and have the suffix `_dark` for the dark-mode version of the images. Example:

- `scenemenu.png`: Light-mode version.
- `scenemenu_dark.png`: Dark-mode version.

If the same image can be used for both light and dark mode, the normal name would be used: `scenemenu.png`.

Use the CSS classes `only-dark` and `only-light` to show an image in only dark mode or light mode, respectively. Make sure that you include both images if adding the class, as the `only-dark` images will be hidden in light mode, and vice versa. Below is an example of how to use the classes.
```md
<!-- This will only be shown in light mode -->
:::{image} image_name.png
:class: only-light
:::

<!-- This will only be shown in dark mode -->
:::{image} image_name_dark.png
:class: only-dark
:::
```

## A note about links

Links to other pages are best done with their ID rather than their path. Paths can change but IDs should stay consistent, making it easier to ensure links aren't broken over time.

✅ Great!
```md:
[RenderablePointCloud](galaxy_renderablegalaxy)
```

🙅 Try to avoid this if possible:
```md:
[RenderablePointCloud](/reference/asset-components/Renderable/RenderableGalaxy.md)
```

You find the ID of a page next to the title of the `.md` file, if you have the docs locally:
```md:
(galaxy_renderablegalaxy)=
# RenderableGalaxy
```

For all the generated documentation, that is the `codegen` ID in the OpenSpace engine repository
```cpp:
documentation::Documentation RenderableGalaxy::Documentation() {
return codegen::doc<Parameters>("galaxy_renderablegalaxy");
}
```

If you need to link to a handwritten markdown in the docs, you can add a similar ID like above to the page and refer to that.
```md:
(example_id)=
# Example Page
```
