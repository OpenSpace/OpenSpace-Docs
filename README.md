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
  5. Run `make html`.

This will create a `build/html` folder structure that contains a `index.html` which you can open in a webbrowser to view the documentation.

Before committing to the repository it can also be beneficial to run `./make.bat linkcheck` which checks whether all links referenced in the document are actually correct or if we have links that are now dead.

## Make commands

- `make html` will build the documentation locally
- `make clean` will clean out the build folder and remove everything built previously.
- `make linkcheck` will check so that all links are correct

## File Structure
  - Each major grouping in the documentation should have a separate folder in the repository that collects all of the files describing things belonging to that major category
  - `generated`: The directory where all generated markdown files will be placed. These will be shown in the `Reference` section of the documentation.
  - `templates`: This is where the jinja templates are stored that are used to structure the markdown files. 
  - `_static`: Files placed in this folder are automatically copied into the resulting documentation. In general, it is not necessary to manually place files in here as Sphinx is copying required files from other places automatically
  - `.readthedocs.yml`: A configuration file that sets up the build environment to build the documentation. Documentation for this file can be found [here](https://docs.readthedocs.io/en/stable/config-file/v2.html)
  - `conf.py`: A Python script that configures the actual Sphinx instance that builds the documentation page. Documentation for this file can be found [here](https://www.sphinx-doc.org/en/master/usage/configuration.html) and [here](https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html)
  - `requirements.txt`: A PIP requirements file that describes all of the Python package requirements that need to be installed
  - `make.bat` / `Makefile`: A batch script for Windows or bash script for Linux to build the documentation. The script needs a second parameter that describes the output type, by default we use `html` for our documentation or `linkcheck` to check whether links in the files are correct. `clean` can be used to remove existing files to build the documentation from scratch, for example via `make.bat clean && make.bat html`.

When adding images that require different files for light-mode and dark-mode, the file should be named normally for the light version and have the suffix `_dark` for the dark-mode version of the images. Example:
  - `scenemenu.png`: Light-mode version
  - `scenemenu_dark.png`: Dark-mode version
If the same image can be used for both light and dark mode, the normal name would be used: `scenemenu.png`
