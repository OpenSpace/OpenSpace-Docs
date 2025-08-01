from git import Repo # git for downloading assets
from jinja2 import Environment, FileSystemLoader # template magic
import json # reading the input file
import os # file paths
import re # regex for searching for assets files
import shutil # copytree, rmtree
from tqdm import tqdm # progress bar
from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

DATA_ASSETS_PATH = "data/assets"

##########################################################################################
#                           ASSET COMPONENTS HELPER FUNCTIONS                            #
##########################################################################################
def copy_local_folder(asset_examples_output, local_openspace_folder):
  print(f"Using local OpenSpace folder {local_openspace_folder}")
  print(f"Copying {DATA_ASSETS_PATH} to {asset_examples_output}...")

  # If a local folders was provided, we don't have to do any of the cloning work, but we
  # must copy the files for any potential `literalinclude` directive to work
  os.makedirs(os.path.join(asset_examples_output, "data"), exist_ok=True)
  source_path = os.path.join(local_openspace_folder, DATA_ASSETS_PATH)
  destination_path = os.path.join(asset_examples_output, DATA_ASSETS_PATH)
  if os.path.exists(destination_path):
    shutil.rmtree(destination_path)
  shutil.copytree(source_path, destination_path)
  print(f"Done copying asset files")

  return os.path.abspath(destination_path)

def clone_github_release(asset_examples_output, tag_or_branch):
  """
  Clones asset directory from OpenSpace git repository
  Can check out a release tag or branch. Default is latest master.
  Returns absolute path to the asset folder
  """

  def print_progress(op_code, cur_count, max_count=None, message=""):
    print(message)

  # Initialize the git repo of OpenSpace repo in the output folder
  repo = Repo.init(asset_examples_output)
  # Create a new remote if there isn't one already created
  origin = repo.remotes[0] if len(repo.remotes) > 0 else None
  if not origin:
    print("No remote origin found. Creating OpenSpace remote...")
    origin = repo.create_remote("origin", "https://github.com/OpenSpace/OpenSpace")

  print(f"Fetching OpenSpace... this might take a while")
  origin.fetch(progress=print_progress, depth=1, tags=True)

  # See if the tag or branch exists. Else, default to origin/master

  # Get all tags on remote
  ref = None
  # Check if the release tag exists first in the repository
  if repo.tag(tag_or_branch) in repo.tags:
    ref = repo.tag(tag_or_branch)
  # If no release exists, check for branch name in the repository
  elif tag_or_branch in repo.references:
    ref = tag_or_branch
  # Neither branch nor release exists: default to origin/master
  else:
    print(f"Could not find tag {tag_or_branch}. Defaulting to origin/master")
    ref = "origin/master"

  # Clone the assets folder from the selected tag or branch
  print(f"Downloading assets examples from '{ref}'...")
  print(f"Cloning OpenSpace... this might take a while")
  # Only clone the assets from the repository to speed up the build time
  git = repo.git()
  git.checkout(ref, "--", DATA_ASSETS_PATH)
  print("Done cloning assets folder from OpenSpace repository")

  assets_folder_path = os.path.abspath(os.path.join(asset_examples_output, DATA_ASSETS_PATH))
  return assets_folder_path

def assets_in_path_recursive(root):
  """
  Find all .asset files in the root dir and subdirs
  """
  filenames = []

  for path, subdirs, files in os.walk(root):
    for file in files:
      if file.endswith(".asset"):
        filenames.append(os.path.join(path, file))
  return filenames

def assets_in_path(path):
  """
  Find all .assets in directory - no subdirs
  """
  filenames = [filename for filename in os.listdir(path) if filename.endswith(".asset")]
  # Prepend the path to the filename
  return list(map(lambda filename: os.path.join(path, filename), filenames))

def get_lines_and_content_from_file(asset_file, regex, look_for_header = False):
  """
  Matches an asset component name with the words in a file
  Returns the content of the file and the lines where the
  matches occured, as well as the header if specified
  """
  lines = []
  is_header_comment = True
  header = ""
  content = ""
  description = ""
  LUA_COMMENT = "--"
  LITERAL_INCLUDE = "```{literalinclude} "
  header_finished = 0
  with open(asset_file, "r", encoding="utf8") as file:
    if not file.readable():
      return None

    # Read file line by line
    for l_no, line in enumerate(file, 1):
      # Check for header comment at top of file
      if not line.startswith(LUA_COMMENT):
        is_header_comment = False

      # If we are in header comment, split into header and description
      if look_for_header and is_header_comment:
        # Remove the beginning of the line that marks it being a Lua comment
        comment = line[len(LUA_COMMENT):].lstrip()

        # If the comment is empty after stipping the comment marker and whitespace, it
        # was an empty line, which we want to keep to preserve paragraph separation. So
        # add it again
        if len(comment) == 0:
            description += "\n\n"

        if l_no == 1:
          # The first line becomes the header
          header = comment
        else:
          if comment.startswith(LITERAL_INCLUDE):
            # Literal includes have to be handled a bit separately. While writing examples
            # we want to pretend that the file we are including is relative to the Lua
            # file, but for Sphinx, it is relative to the Markdown file. To solve this, we
            # make use of the fact that Sphinx will treat any path to a literalinclude
            # that starts with a / as a path relative to the _base folder_. So we can
            # switch out the path at the last minute and make sure that it gets correctly
            # included
            path = comment[len(LITERAL_INCLUDE):]

            # We need to get the path to the asset file relative to the base folder
            full_folder = os.path.dirname(asset_file)
            rel_folder = os.path.relpath(full_folder)
            comment = f"{LITERAL_INCLUDE} /{rel_folder}/{path}"

          description += comment
          header_finished = l_no + 1
      # Else, get the content of the example
      else:
        content += line
        # Search for the regex pattern
        if re.search(regex, line):
          # If the header has been removed we need to adjust the line number
          lines.append(l_no - header_finished)

  # If there were any matches to regex, set the content as the example
  if len(lines) > 0:
    return {
      "header": header,
      "description": description,
      "content": content,
      "lines": lines
    }
  else:
    return None

def find_shortest_asset_in_path(asset_files, name):
  """
  Takes an asset component name and matches it to all provided files and then return the
  shortest asset with matches.
  """
  # Find first example matching the asset component (files are sorted by length)
  for asset_file in asset_files:
    # Search for Type = "<name>"
    regex = r"Type = \"" + name + r"\""
    example = get_lines_and_content_from_file(asset_file, regex)
    if example:
      return example
  # If nothing found, return None
  return None

# Returns the list of examples and as a second argument whether there are hand-written
# dedicated examples
def find_asset_examples(assets_folder, category, name, folder_asset_files, example_asset_files):
  """
  Search through all example assets for the component name
  Returns file content and line numbers for where the name occurs
  """
  examples_folder = os.path.join(assets_folder, "examples")

  # Search pass 1
  # Look up folder "assets/<category>/<assetcomponentname>/" and see if it exists. If it
  # does, add all files in that folder (no subdirectories)
  asset_directory = os.path.join(examples_folder, os.path.join(category, name).lower())
  if os.path.exists(asset_directory):
    filenames = assets_in_path(asset_directory)
    examples = []
    for filename in filenames:
      # We search for the asset component <name> or "<name>"
      regex = r"\b" + name + r"\b|\b\"" + name + r"\"\b"
      example = get_lines_and_content_from_file(filename, regex, True)
      examples.append(example)
    return examples, True

  # Search pass 2
  # Search through all assets in the **examples** folder and add the shortest asset
  example = find_shortest_asset_in_path(example_asset_files, name)
  if example:
    return [ example ], False

  # Search pass 3
  # Search through all assets in the **assets** folder and add the shortest asset
  example = find_shortest_asset_in_path(folder_asset_files, name)
  if example:
    return [ example ], False

  # If nothing found, return empty array
  return [], False

def group_members_by_optionality(members):
  """
  Group members by optionality while preserving the alphabetical order
  """
  non_optional_indices = []
  optional_indices = []
  for i, member in enumerate(members):
    if member["optional"]:
      optional_indices.append(i)
    else:
      non_optional_indices.append(i)
  indices = non_optional_indices + optional_indices
  return [ members[i] for i in indices ]

def find_asset_screenshot(name):
  """
  Find a screenshot in the images folder with the exact same name as the component
  """
  img_path = f"_static/images/renderables/{name}.png"
  return img_path if os.path.exists(img_path) else None

##########################################################################################
#                              SCRIPTING API HELPER FUNCTIONS                            #
##########################################################################################

def parse_doxygen_comments(library):
  """
  This function modifies the scripting library so that the doxygen comments are added to
  the arguments.
  Supported doxygen parameters: \\param \\return \\code
  """
  for function in library["functions"]:
    [help_text, p, return_description] = function["help"].partition("\\\\return")

    # Parse code blocks
    help_text = help_text.replace("\\\\code", "\n:::{code-block} lua\n")
    help_text = help_text.replace("\\\\endcode", "\n:::")

    # Split help text into parameters and return type
    help_text = help_text.split("\\\\param ")
    # First substring will be the description
    description = help_text[0].strip()
    # Add to the dictionary
    function["help"] = description
    # Collect the params, everything after the 1st
    params = help_text[1:]
    identifiers = []
    argument_descriptions = []
    for param in params:
      [identifier, ws, params_description] = param.partition(" ")
      identifiers.append(identifier)
      argument_descriptions.append(params_description)

      # Add params to the dictionary
      for argument in function["arguments"]:
        if argument["name"] in identifiers:
          index = identifiers.index(argument["name"])
          argument["description"] = argument_descriptions[index]
      # Add return type to the dictionary, if there is one
      if return_description:
        function["returnDescription"] = return_description

  return library

##########################################################################################
#                                 CREATE ASSET COMPONENTS                                #
##########################################################################################

def generate_asset_components(environment, assets_folder, output_folder, folder_name_assets, json_location):
  """
  Creates the Markdown files for the asset components, as well as an index file which
  links to them
  """
  # List all of the assets in the asset and the dedicated example folders
  examples_folder = os.path.join(assets_folder, "examples")
  example_asset_files = assets_in_path_recursive(examples_folder)
  # Sort by shortest asset file first
  example_asset_files.sort(key=lambda file: os.stat(file).st_size)

  folder_asset_files = assets_in_path_recursive(assets_folder)
  # Sort by shortest asset file first
  folder_asset_files.sort(key=lambda file: os.stat(file).st_size)


  # Create target folder
  assets_output_path = os.path.join(output_folder, folder_name_assets)
  os.makedirs(assets_output_path, exist_ok=True)

  f = open(os.path.join(json_location, "assetComponents.json"))
  asset_categories = json.load(f)

  # Create pages for the asset component pages
  asset_component_template = environment.get_template("asset_component.html.jinja")
  asset_component_category_index_template = environment.get_template("asset_component_category_index.html.jinja")

  # Missing and found asset files
  components_info = []
  print("Handle individual components")
  for category in asset_categories:
    # Create a folder for the category
    asset_category_output_path = os.path.join(assets_output_path, category["name"])
    os.makedirs(asset_category_output_path, exist_ok=True)

    # Create a category index file
    output_category_index = asset_component_category_index_template.render(category=category)
    with open(os.path.join(asset_category_output_path, f"index.md"), "w") as f:
      f.write(output_category_index)

    # Find base class to add its members to each derived class
    base_class_name = category["name"]
    base_class = None
    has_base_class = False
    for asset_component in category["classes"]:
      if asset_component["name"] == base_class_name:
        base_class = asset_component
        has_base_class = True
        break

    # Go through all the components in that category and print out a md file
    for asset_component in tqdm(category["classes"], desc=category["name"]):
      is_base_class = has_base_class and asset_component["name"] == base_class["name"]
      base_class_name = base_class["name"] if has_base_class and not is_base_class else ""
      base_class_identifier = base_class["identifier"] if has_base_class and not is_base_class else ""

      # Add the base class members to each derived class
      # If the component is the base class
      base_class_members = group_members_by_optionality(base_class["members"]) if has_base_class and not is_base_class else []

      grouped_members = group_members_by_optionality(asset_component["members"])

      # Find example for the asset component, if it is not a baseclass component
      examples = []
      if not is_base_class:
        examples, has_hand_written = find_asset_examples(
          assets_folder,
          category["name"],
          asset_component["name"],
          folder_asset_files,
          example_asset_files
        )

        components_info.append({
          "name": asset_component["name"],
          "category": category["name"],
          "has_example": has_hand_written
        })


      # Render component page with jinja
      output_asset_component = asset_component_template.render(
        data=asset_component,
        base_class_name=base_class_name,
        base_class_identifier=base_class_identifier,
        base_class_members=base_class_members,
        members=grouped_members,
        examples=examples
      )
      name = asset_component["name"]
      with open(os.path.join(asset_category_output_path, f"{name}.md"), "w") as f:
        f.write(output_asset_component)

  # Create index file
  index_asset_components_template = environment.get_template("asset_components_index.html.jinja")
  outputIndex = index_asset_components_template.render(asset_categories=asset_categories)
  with open(f"{assets_output_path}/index.md", "w") as f:
    f.write(outputIndex)

  # Create table for the Wiki
  components_info.sort(key=lambda component: component["name"])
  comps = ""
  for c in components_info:
    name = c["name"]
    category = c["category"]
    has_example = "Yes" if c["has_example"] else ""
    comps = f"{comps}| {name} | {category} | {has_example} |\n"

  print(f"""
Documentation Writing Overview
https://internal.openspaceproject.com/e/en/documentation-writing

| Name | Type | Has Example |
| ---- | ---- | ----------- |
{comps}
""")

##########################################################################################
#                                 CREATE SCRIPTING API                                   #
##########################################################################################

def generate_scripting_api(environment, output_folder, folder_name_scripting, json_location):
  """
  Creates the Markdown files for the scripting libraries, as well as an index file that
  links to them
  """
  # Create target folder
  scripting_output_path = os.path.join(output_folder, folder_name_scripting)
  os.makedirs(scripting_output_path, exist_ok=True)

  f = open(os.path.join(json_location, "scriptingApi.json"))
  scripting_api = json.load(f)

  # Create the pages for the scripting libraries
  template = environment.get_template("scripting_api.html.jinja")
  for library in scripting_api:
    # Go through all the functions in that library and print out a md file
    library = parse_doxygen_comments(library)
    output_library = template.render(library=library)
    library_name = library["fullName"]
    with open(os.path.join(scripting_output_path, f"{library_name}.md"), "w") as f:
      f.write(output_library)

  # Create index file
  index_template = environment.get_template("scripting_api_index.html.jinja")
  output_index = index_template.render(libraries=scripting_api)
  with open(os.path.join(scripting_output_path, "index.md"), "w") as f:
    f.write(output_index)

##########################################################################################
#                              CREATE RENDERABLE OVERVIEW                                #
##########################################################################################

def generate_renderable_overview(environment, output_folder, json_location):
  """
  Creates a Markdown file with a grid of pictures of the renderables and
  ScreenSpaceRenderables in OpenSpace
  """
  f = open(os.path.join(json_location, "assetComponents.json"))
  asset_categories = json.load(f)

  images = {}
  renderables = []
  for category in asset_categories:
    if category["name"] == "Renderable" or category["name"] == "ScreenSpaceRenderable":
      for asset_component in category["classes"]:
        if asset_component["name"] == category["name"]:
          # Base class -> ignore
          continue

        # Find example image
        image = find_asset_screenshot(asset_component["name"])
        images[asset_component["name"]] = image
        renderables.append(asset_component)

  # Create overview file
  renderable_overview = environment.get_template("renderable_overview.html.jinja")
  output_overview = renderable_overview.render(renderables=renderables, images=images)
  with open(os.path.join(output_folder, "renderable-overview.md"), "w") as f:
    f.write(output_overview)


##########################################################################################
#                                         MAIN                                           #
##########################################################################################

def generate_docs(app, config):
  # Name variables
  json_location = "json"
  output_folder = "reference"
  folder_name_assets = "asset-components"
  folder_name_scripting = "scripting-api"
  asset_examples_output = os.path.join(output_folder, "asset_examples")

  # Check if the reference has already been generated. Note that we assume that this is
  # the case if the asset examples folder exists
  reference_already_generated = os.path.exists(asset_examples_output)

  if not config.generate_reference and reference_already_generated:
    print("Skipping generating new assets examples...")
    print("To generate set 'generate_reference' to True in the conf.py file")
    return

  print("Generating dynamic documentation (the reference)")

  # Get config values
  use_github = config.assets_examples_use_github
  release_tag_or_branch = config.assets_release_tag_or_branch
  local_openspace_folder = config.assets_local_openspace_folder

  assets_folder = None
  if use_github:
    # Download assets files from OpenSpace repository
    assets_folder = clone_github_release(asset_examples_output, release_tag_or_branch)
  else:
    if local_openspace_folder == "":
      print("You need to specify a local OpenSpace folder for 'assets_folder'")
      return
    # Copy asset files from local OpenSpace folder
    assets_folder = copy_local_folder(asset_examples_output, local_openspace_folder)

  # Load jinja templates folder
  environment = Environment(loader=FileSystemLoader("templates"))

  # Generate documentation
  generate_asset_components(
    environment,
    assets_folder,
    output_folder,
    folder_name_assets,
    json_location
  )
  generate_scripting_api(environment, output_folder, folder_name_scripting, json_location)
  generate_renderable_overview(environment, output_folder, json_location)


##########################################################################################
#                                         Sphinx setup                                   #
##########################################################################################
def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value('generate_reference', True, 'bool')
    app.add_config_value('assets_examples_use_github', True, "bool")
    app.add_config_value('assets_release_tag_or_branch', "", 'string')
    app.add_config_value('assets_local_openspace_folder', "", 'string')

    app.connect('config-inited', generate_docs)

    return {
        'version': '1.0',
        'env_version': 1,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }