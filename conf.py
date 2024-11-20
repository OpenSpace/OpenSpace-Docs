import os
import sys
from pathlib import Path
sys.path.append(str(Path('_ext').resolve()))

##########################################################################################
#                               Generate asset examples                                  #
##########################################################################################

# If we are on Read the docs, always build from github master
if (os.environ.get("READTHEDOCS")):
  generate_assets_examples = True
  assets_examples_use_github = True
  assets_branch = "master" # Use the environment variable READTHEDOCS_VERSION here?
# If we are working on our local machine
else:
  generate_assets_examples = False # Generates asset examples if true
  assets_examples_use_github = True # Use github for the examples? Else, local folder
  assets_branch = "master" # Branch name for github option
  assets_folder = "" # Folder path for local folder option
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
  "generate_docs",
  "custom_directives"
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
  "fieldlist"
}
myst_heading_anchors = 3



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
  "profile.css"
]

# These folders are copied to the documentation's HTML output
html_static_path = [ "_static" ]

templates_path = [ "_templates" ]

# html_extra_path = ["robots.txt"]

