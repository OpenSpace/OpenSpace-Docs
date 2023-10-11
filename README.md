# OpenSpace Documentation
This repository contains the source of the documentation for OpenSpace. The documentation is written in [MyST](https://myst-parser.readthedocs.io/en/latest/index.html), a Markdown syntax extension, converted into an HTML page using [Sphinx](https://www.sphinx-doc.org/en/master/), and then finally hosted by [Read the Docs](https://about.readthedocs.com/?ref=readthedocs.com) at https://docs.openspaceproject.com.

Every commit and pull request to this repository will trigger a new build of the documentation. The `master` will build into the "latest" version and each versioned tag is selectedable in the flyout menu, with the last version being marked as "stable".

## Building the documentation locally
During the development it is beneficial to build the documentation page locally to see the results before committing something into the repository that fails to build or that produces warnings.

1. In a shell, move to this directory
1. `pip install -r requirements.txt` (this is technically only necessary for the first time or when the dependencies change, but it is a good habit to run this every time after a checkout)
1. `make.bat html`

This will create a `build/html` folder structure that contains a `index.html` which you can open in a webbrowser to view the documentation.

Before committing to the repository it can also be beneficial to run `./make.bat linkcheck` which checks whether all links referenced in the document are actually correct or if we have links that are now dead.

## File Structure
- Each major grouping in the documentation should have a separate folder in the repository that collects all of the files describing things belonging to that major category
- `img`: This folder contains images that are of general use for the documentation. Images used in specific documentation pages should be located alongside their respective files instead
- `support`: A folder containing additional meta files that are useful/necessary to write the documentation, but that are not documenting the software itself
- `_static`: Files placed in this folder are automatically copied into the resulting documentation. In general, it is not necessary to manually place files in here as Sphinx is copying required files from other places automatically
- `.readthedocs.yml`: A configuration file that sets up the build environment to build the documentation. Documentation for this file can be found [here](https://docs.readthedocs.io/en/stable/config-file/v2.html)
- `.conf.py`: A Python script that configures the actual Sphinx instance that builds the documentation page. Documentation for this file can be found [here](https://www.sphinx-doc.org/en/master/usage/configuration.html) and [here](https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html)
- `requirements.txt`: A PIP requirements file that describes all of the Python package requirements that need to be installed
- `make.bat` / `Makefile`: A batch script for Windows or bash script for Linux to build the documentation. The script needs a second parameter that describes the output type, by default we use `html` for our documentation or `linkcheck` to check whether links in the files are correct
