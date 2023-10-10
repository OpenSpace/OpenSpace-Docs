import sphinx_rtd_theme


###
# Global Settings
###
needs_sphinx = "4.0"

project = "OpenSpace"
author = "OpenSpace community"
project_copyright = "2014-2023, OpenSpace community"

# Update with every new release
version = release = "0.19.1"

extensions = [
  "myst_parser",
  "notfound.extension",
  "sphinx_copybutton",
  "sphinx_design",
  "sphinx.ext.autosectionlabel",
  "sphinx.ext.duration",
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
highlight_language = "lua"

myst_enable_extensions = {
  "colon_fence",
  "fieldlist"
}



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
