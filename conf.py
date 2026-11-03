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
generate_reference = True

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

# If we are on Read the Docs, get the name of the current OpenSpace-Docs branch and try to
# find a OS release tag that matches. Also, always generate the reference and use GitHub
# for the asset files
if (os.environ.get("READTHEDOCS")):
  generate_reference = True
  assets_examples_use_github = True
  print(f"Read the docs will look for the OpenSpace tag: {assets_release_tag_or_branch}")




###
# Global Settings
###
needs_sphinx = "9.1.0"

project = "OpenSpace"
author = "OpenSpace community"
project_copyright = "2014-2026, OpenSpace community"

# Update with every new release
version = release = os.getenv("READTHEDOCS_VERSION", "0.22.0")

extensions = [
  "myst_parser",
  "notfound.extension",
  "sphinx_copybutton",
  "sphinx_design",
  "sphinx.ext.autosectionlabel",
  "sphinx.ext.duration",
  "sphinxcontrib.mermaid",
  "generate_docs", # Custom extension, lives in _ext
  "custom_directives" # Custom extension, lives in _ext
]



###
# Content
###
source_encoding = "utf-8"
exclude_patterns = [
  "README.md",
  ".venv",
  "build"
]
root_doc = "index"
autosectionlabel_prefix_document = True
pygments_style = "friendly"
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
html_theme = "furo"
html_theme_options = {
  # The logo carries the name, so there is no need to repeat it as text. The colors,
  # fonts and layout of the theme live in the CSS files listed in html_css_files
  "light_logo": "logo-light.webp",
  "dark_logo": "logo-dark.webp",
  "sidebar_hide_name": True,
  "navigation_with_keys": True,
  "source_repository": "https://github.com/OpenSpace/OpenSpace-Docs/",
  "source_branch": "master",
  "source_directory": "",
  "top_of_page_buttons": ["view", "edit"],
  "footer_icons": [
    {
      "name": "GitHub",
      "url": "https://github.com/OpenSpace/OpenSpace-Docs",
      "html": """
        <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
        </svg>
      """,
      "class": "",
    },
  ],
}

html_title = f"OpenSpace documentation ({version})"
html_short_title = "OpenSpace"

html_favicon = "_static/icon.png"

# CSS files that are added into the generated documentation. The order matters: later
# files override earlier ones
html_css_files = [
  "fonts.css",
  "theme-colors.css",
  "theme-layout.css",
  "required-reading.css",
  "custom.css"
]

# These folders are copied to the documentation's HTML output
html_static_path = [ "_static" ]

# Template overrides for the theme, currently the breadcrumbs in _templates/page.html
templates_path = [ "_templates" ]

# html_extra_path = ["robots.txt"]

