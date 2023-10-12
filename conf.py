import sphinx_rtd_theme
import os


###
# Global Settings
###
needs_sphinx = "4.0"

project = "OpenSpace"
author = "OpenSpace community"
project_copyright = "2014-2023, OpenSpace community"

# Update with every new release
version = release = os.getenv("READTHEDOCS_VERSION", "0.19.1")

extensions = [
  "myst_parser",
  "notfound.extension",
  "sphinx_copybutton",
  "sphinx_design",
  "sphinx.ext.autosectionlabel",
  "sphinx.ext.duration",
  "sphinxcontrib.jquery",
  "sphinxcontrib.luadomain",
  "sphinxcontrib.mermaid"
]

keep_warnings = True



###
# Content
###
source_encoding = "utf-8-sig"
exclude_patterns = [
  "README.md"
]
root_doc = "index"
primary_domain = "lua"
autosectionlabel_prefix_document = True
pygments_style = "sphinx"

myst_enable_extensions = {
  "colon_fence",
  "fieldlist"
}
myst_heading_anchors = 3



###
# HTML output
###
html_theme = "furo"
html_theme_options = {
  "sidebar_hide_name": True,      # No project title in the sidebar
  "source_repository": "https://github.com/OpenSpace/OpenSpace-Docs/",
  "source_branch": "master",
  "source_directory": "/",
}
html_title = f'OpenSpace documentation ({version})'
html_short_title = "OpenSpace"

html_logo = "img/logo.png"
html_favicon = "img/icon.png"

# JavaScript files that are added into the generated documentation
html_js_files = [

]

# CSS files that are added into the generated documentation
html_css_files = [

]

# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

# html_extra_path = ["robots.txt"]
