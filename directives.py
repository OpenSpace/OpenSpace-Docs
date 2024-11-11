from docutils.parsers.rst.directives import unchanged, choice
from jinja2 import Environment, FileSystemLoader
from sphinx.util.docutils import SphinxDirective

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
    }

    def run(self):
        notapplicable = "Not applicable"
        census = self.options.get("census", notapplicable)
        assetfile = self.options.get("assetfile", notapplicable)
        openspaceversion = self.options.get("openspaceversion", notapplicable)
        preparedby = self.options.get("preparedby", notapplicable)
        sourceversion = self.options.get("sourceversion", notapplicable)
        license = self.options.get("license", notapplicable)

        environment = Environment(loader=FileSystemLoader("templates"))

        # We can't pass free text as a parameter to the directive, so instead we
        # add the ability to add free text for the references through the content of the
        # directive. This is an array of strings.
        reference = " ".join(self.content) if len(self.content) > 0 else notapplicable
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