import sphinx_rtd_theme


###
# Global Settings
###
needs_sphinx = "4.0"

project = "OpenSpace"
author = "OpenSpace community"
project_copyright = "2014-2023, OpenSpace community"
version = "0.19.1"
release = version

# Installed extensions (synced with `requirements.txt`)
extensions = [
  "notfound.extension",
  "sphinx_copybutton",
  "sphinx.ext.duration",
  "sphinxcontrib.luadomain"
]

keep_warnings = True


###
# Content
###
source_suffix = ".rst"
source_encoding = "utf-8-sig"

root_doc = "index"

rst_prolog = """
"""
rst_epilog = """
"""

primary_domain = "lua"

pygments_style = "sphinx"
highlight_language = "lua"


###
# HTML output
###
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
using_rtd_theme = True

html_theme_options = {
  "logo_only": True,            # No title text
  "collapse_navigation": False, # Collapse navigation tree
  "display_version": False      # Hide documentation version name beneath the logo
}
html_title = f'OpenSpace documentation ({version})'
html_short_title = "OpenSpace"

# VCS options: https://docs.readthedocs.io/en/stable/guides/edit-source-links-sphinx.html
html_context = {
  "display_github": True,
  "github_user": "OpenSpace",
  "github_repo": "OpenSpace-Docs",
  "github_version": "master",
  "conf_py_path": "/"
}

html_logo = "img/logo.png"
html_favicon = "img/icon.png"

# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

# html_extra_path = ["robots.txt"]


