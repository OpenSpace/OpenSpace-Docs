import os
import sys
from pathlib import Path
# Resolves custom extensions that live in _ext
sys.path.append(str(Path('_ext').resolve()))

##########################################################################################
#                               Generate asset examples                                  #
##########################################################################################

###
# Settings for Local Build (Developer)
#
# These settings controls if the files for the reference should be genereated and where
# the files for the asset examples should be acquired from. When building locally, feel
# free to change these settings to your liking, but do not commit the changes.
###

# If true, always generate new files for the reference. If false, only generate if the
# generated files do not already exist, to speed up the build process
generate_reference = False

# If true, use github for getting the asset example files. The GitHub tag or branch
# is specified with assets_release_tag_or_branch
# If false, use a local OpenSpace folder path, which is specified with
# assets_local_openspace_folder
assets_examples_use_github = True

# If using github for the examples, specify the release tag name or the branch name here.
# If empty, will use origin/master
assets_release_tag_or_branch = ""

# If using a local OpenSpace version for the examples, specify the path here
assets_local_openspace_folder = ""



###
# Settings for Web Build
###

# If we are on Read the Docs, get the name of the current OpenSpace-Docs branch and try to find a
# OS release tag that matches. Also, always generate the reference and use GitHub for the asset files.
if (os.environ.get("READTHEDOCS")):
  generate_reference = True
  assets_examples_use_github = True
  assets_release_tag_or_branch = os.environ.get("READTHEDOCS_VERSION")
  print(f"Read the docs will look for the OpenSpace tag: {assets_release_tag_or_branch}")




###
# Global Settings
###
needs_sphinx = "7.4.6"

project = "OpenSpace"
author = "OpenSpace community"
project_copyright = "2014-2024, OpenSpace community"

# Update with every new release
version = release = os.getenv("READTHEDOCS_VERSION", "0.20.0")

extensions = [
  "myst_parser",
  "notfound.extension",
  "sphinx_copybutton",
  "sphinx_design",
  "sphinx.ext.autosectionlabel",
  "sphinx.ext.duration",
  "sphinxcontrib.jquery",
  "sphinxcontrib.luadomain",
  "sphinxcontrib.mermaid",
  "generate_docs", # Custom extension, lives in _ext
  "custom_directives" # Custom extension, lives in _ext
]

keep_warnings = True



###
# Content
###
source_encoding = "utf-8-sig"
exclude_patterns = [
  "README.md",
  ".venv"
]
root_doc = "index"
primary_domain = "lua"
autosectionlabel_prefix_document = True
pygments_style = "default"
pygments_dark_style = "monokai"

myst_enable_extensions = {
  "attrs_inline",
  "attrs_block",
  "colon_fence",
  "fieldlist",
  "deflist"
}
myst_heading_anchors = 4



###
# HTML output
###
html_theme = "sphinx_rtd_theme"
html_theme_options = {
  "logo_only": True,
  "display_version": False,
  "collapse_navigation": False,
  "titles_only": True,
}

html_context = {
  "display_github": True,  # Integrate GitHub
  "github_user": "OpenSpace",  # Username
  "github_repo": "OpenSpace-Docs",  # Repo name
}

# Add a transparent image as the logo
# Instead we add the logo later in the css
# This enables different logos in dark and light mode
html_logo = "_static/transparent.png"

html_title = f"OpenSpace documentation ({version})"
html_short_title = "OpenSpace"

html_favicon = "_static/icon.png"

# JavaScript files that are added into the generated documentation
html_js_files = [
  "custom.js"
]

# CSS files that are added into the generated documentation
html_css_files = [
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",

  "required-reading.css",
  "sidebar.css",
  "custom.css",
  "dark-mode-images.css"
]

# These folders are copied to the documentation's HTML output
html_static_path = [ "_static" ]

templates_path = [ "_templates" ]

# html_extra_path = ["robots.txt"]

