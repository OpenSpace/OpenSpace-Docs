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
  "colon_fence",
  "fieldlist",
  "html_image"
}
myst_heading_anchors = 3



###
# HTML output
###
html_theme = "furo"
html_theme_options = {
  # No written project title in the sidebar
  "sidebar_hide_name": True,

  # Make the edit button in the top right appear
  "source_repository": "https://github.com/OpenSpace/OpenSpace-Docs/",
  "source_branch": "master",
  "source_directory": "/",

  # Set CSS Variables. The dark theme inherits all light variables
  "light_css_variables": {
    "font-stack--monospace": "Source Code Pro Light, monospace"
  },

  # Add custom items in the footer
  "footer_icons": [
    {
        "name": "GitHub",
        "url": "https://github.com/OpenSpace/OpenSpace",
        "html": "",
        "class": "fa-brands fa-solid fa-github fa-2x"
    }
  ],

  "dark_logo": "logo.png",
  "light_logo": "logo-inverted.png"
}
html_title = f'OpenSpace documentation ({version})'
html_short_title = "OpenSpace"

html_favicon = "assets/icon.png"

# JavaScript files that are added into the generated documentation
html_js_files = [

]

# CSS files that are added into the generated documentation
html_css_files = [
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css"
]

# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

# html_extra_path = ["robots.txt"]
