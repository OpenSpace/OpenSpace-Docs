from docutils.parsers.rst.directives import unchanged, choice
from jinja2 import Environment, FileSystemLoader
from sphinx.util.docutils import SphinxDirective
from sphinx.util.typing import ExtensionMetadata
from sphinx.application import Sphinx



class Dossier(SphinxDirective):
  has_content = True

  licenses = {
    "amnh": {
      "name": "AMNH's Digital Universe",
      "link": "https://www.amnh.org/research/hayden-planetarium/digital-universe/download/digital-universe-license"
    },
    "mit": {
      "name": "MIT",
      "link": "https://github.com/OpenSpace/OpenSpace/blob/master/LICENSE.md"
    },
    "cc-by": {
      "name": "CC-BY",
      "link": "https://creativecommons.org/licenses/by/4.0/"
    },
  }

  option_spec = {
    "census": unchanged, # Expects a string
    "assetfile": unchanged, # Expects a string
    "openspaceversion": unchanged, # Expects a string
    "preparedby": unchanged, # Expects a string
    "sourceversion": unchanged, # Expects a string
    "license": lambda x: choice(x, ["amnh", "mit", "cc-by"]), # Expects a string, one of these
    "reference": unchanged
  }

  def process_reference(self, r):
    if ("=" in r):
      [name, link] = r.split("=")
      return {
        "name": name,
        "link": link
      }
    else:
      return { "name": r }

  def run(self):
    notapplicable = "Not applicable"
    census = self.options.get("census", notapplicable)
    assetfile = self.options.get("assetfile", notapplicable)
    openspaceversion = self.options.get("openspaceversion", notapplicable)
    preparedby = self.options.get("preparedby", notapplicable)
    sourceversion = self.options.get("sourceversion", notapplicable)
    license = self.options.get("license", notapplicable)
    reference = self.options.get("reference", notapplicable)

    if (reference != notapplicable):
      reference = reference.split(";")
      reference = list(map(self.process_reference, reference))

    environment = Environment(loader=FileSystemLoader("templates"))

    # We can't pass free text as a parameter to the directive, so instead we
    # add the ability to add free text for the references through the content of the
    # directive. This is an array of strings.
    license = self.licenses[license] if self.licenses.__contains__(license) else license
    assetfile = f'`{assetfile}`' if assetfile != notapplicable else assetfile
    template = environment.get_template("dossier.html.jinja")

    # Render component page with jinja
    output = template.render(
      census=census,
      assetfile=assetfile,
      openspaceversion=openspaceversion,
      preparedby=preparedby,
      sourceversion=sourceversion,
      reference=reference,
      license=license
    )

    self.content = output
    allow_headers = True
    return self.parse_content_to_nodes(allow_headers)
  


class Profile_Dossier(SphinxDirective):
  has_content = True

  licenses = {
    "amnh": {
      "name": "AMNH's Digital Universe",
      "link": "https://www.amnh.org/research/hayden-planetarium/digital-universe/download/digital-universe-license"
    },
    "mit": {
      "name": "MIT",
      "link": "https://github.com/OpenSpace/OpenSpace/blob/master/LICENSE.md"
    },
    "cc-by": {
      "name": "CC-BY",
      "link": "https://creativecommons.org/licenses/by/4.0/"
    },
  }


  option_spec = {
    "name": unchanged, # Expects a string
    "profilefile": unchanged, # Expects a string
    "anchor": unchanged, # Expects a string
    "time": unchanged, # Expects a string
    "author": unchanged, # Expects a string
    "license": lambda x: choice(x, ["amnh", "mit", "cc-by"]), # Expects a string, one of these
    "version": unchanged, # Expects a string
  }

  def process_anchor(self, r):
    if ("=" in r):
      [name, link] = r.split("=")
      return {
        "name": name,
        "link": link
      }
    else:
      return { "name": r }


  def run(self):
    notapplicable = "Not applicable"
    name = self.options.get("name", notapplicable)
    profilefile = self.options.get("profilefile", notapplicable)
    anchor = self.options.get("anchor", notapplicable)
    time = self.options.get("time", notapplicable)
    author = self.options.get("author", notapplicable)
    license = self.options.get("license", notapplicable)
    version = self.options.get("version", notapplicable)

    
    if (anchor != notapplicable):
      anchor = anchor.split(";")
      anchor = list(map(self.process_anchor, anchor))

    environment = Environment(loader=FileSystemLoader("templates"))

    # We can't pass free text as a parameter to the directive, so instead we
    # add the ability to add free text for the references through the content of the
    # directive. This is an array of strings.
    license = self.licenses[license] if self.licenses.__contains__(license) else license
    profilefile = f'`{profilefile}`' if profilefile != notapplicable else profilefile
    template = environment.get_template("dossier_profile.html.jinja")

    # Render component page with jinja
    output = template.render(
      name=name,
      profilefile=profilefile,
      anchor=anchor,
      time=time,
      author=author,
      license=license,
      version=version      
    )

    self.content = output
    allow_headers = True
    return self.parse_content_to_nodes(allow_headers)
  
  ##########################################################################################
#                                         Sphinx setup                                   #
##########################################################################################
def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_directive("dossier", Dossier)
    app.add_directive("profile_dossier", Profile_Dossier)

    return {
        'version': '1.0',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }