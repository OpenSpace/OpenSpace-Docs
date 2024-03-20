import os


###
# Global Settings
###
needs_sphinx = "4.0"

project = "OpenSpace"
author = "OpenSpace community"
project_copyright = "2014-2023, OpenSpace community"

# Update with every new release
version = release = os.getenv("READTHEDOCS_VERSION", "0.19.2")

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
pygments_style = "default"
pygments_dark_style = "monokai"

myst_enable_extensions = {
  "attrs_inline",
  "colon_fence",
  "fieldlist"
}
myst_heading_anchors = 3



###
# HTML output
###
html_theme = "sphinx_rtd_theme"
html_theme_options = {
  "logo_only" : True, 
  "prev_next_buttons_location" : "None",
  "display_version": False,
  "collapse_navigation": False,
}

html_logo = "_static/logo.png"
html_title = f'OpenSpace documentation ({version})'
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
  "sidebar.css"
]

# These folders are copied to the documentation's HTML output
html_static_path = [ "_static" ]

templates_path = [ "_templates" ]

# html_extra_path = ["robots.txt"]
