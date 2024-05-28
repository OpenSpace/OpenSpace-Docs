from git import Repo # git for downloading assets
from jinja2 import Environment, FileSystemLoader # template magic
import json # reading the input file
import os # file paths
import re # regex for searching for assets files
from tqdm import tqdm # progress bar

##########################################################################################
#                           ASSET COMPONENTS HELPER FUNCTIONS                            #
##########################################################################################

def clone_assets_folder(folder_name):
  """
  Clones asset directory from OpenSpace git repository
  Uses the latest master
  Returns absolute path to the asset folder
  """
  def print_progress(op_code, cur_count, max_count=None, message=""):
    print(message)

  print("Cloning assets examples...")
  repo = Repo.init(folder_name)

  # Create a new remote if there isn't one already created
  origin = repo.remotes[0] if len(repo.remotes) > 0 else None
  if not origin:
    print("No remote origin found. Creating OpenSpace remote...")
    origin = repo.create_remote("origin", "https://github.com/OpenSpace/OpenSpace")

  print(f"Fetching OpenSpace... this might take a while")
  origin.fetch(progress=print_progress, depth=1)

  data_assets_path = "data/assets"
  git = repo.git()
  git.checkout("origin/master", "--", data_assets_path)
  print("Done cloning assets folder from OpenSpace repository")
  assets_folder_path = os.path.abspath(os.path.join(folder_name, data_assets_path))
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
  LUA_COMMENT = "-- "
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
        comment = line.split(LUA_COMMENT)[1]
        if l_no == 1:
          header = comment
        else:
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
    return { "header": header, "description": description, "content": content, "lines": lines }
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

def find_asset_example(assets_folder, category, name, folder_asset_files, example_asset_files):
  """
  Search through all example assets for the component name
  Returns file content and line numbers for where the name occurs
  """
  examples_folder = os.path.join(assets_folder, "examples")

  # Search pass 1: look up folder “assets/<category>/<assetcomponentname>/”
  # and see if it exists. If it does, add all files in that folder (no subdirectories)
  asset_directory = os.path.join(examples_folder, (os.path.join(category, name)).lower())
  if os.path.exists(asset_directory):
    filenames = assets_in_path(asset_directory)
    examples = []
    for filename in filenames:
      # We search for the asset component <name> or "<name>"
      regex = r"\b" + name + r"\b|\b\"" + name + r"\"\b"
      example = get_lines_and_content_from_file(filename, regex, True)
      examples.append(example)
    return examples

  # Search pass 2: search through all assets in the **examples** folder and add the
  # shortest asset
  example = find_shortest_asset_in_path(example_asset_files, name)
  if example:
    return [ example ]

  # Search pass 3: search through all assets in the **assets** folder and add the
  # shortest asset
  example = find_shortest_asset_in_path(folder_asset_files, name)
  if example:
    return [ example ]

  # If nothing found, return empty array
  return []

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

def generate_asset_components(environment, output_folder, folder_name_assets, json_location):
  """
  Creates the Markdown files for the asset components, as well as an index file which
  links to them
  """
  assets_examples_folder_name = "asset_examples"
  # Download assets files from OpenSpace repository
  assets_folder = clone_assets_folder(os.path.join(output_folder, assets_examples_folder_name))

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
  if not os.path.exists(assets_output_path):
    os.mkdir(assets_output_path)

  f = open(os.path.join(json_location, "assetComponents.json"))
  asset_categories = json.load(f)

  # Create pages for the asset component pages
  asset_component_template = environment.get_template("asset_component.html.jinja")

  # Missing and found asset files
  components_missing_assets = []
  no_of_found_assets = 0
  for category in asset_categories:
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
    for asset_component in tqdm(category["classes"], desc="Generating asset components for " + category["name"]):
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
        examples = find_asset_example(
          assets_folder,
          category["name"],
          asset_component["name"],
          folder_asset_files,
          example_asset_files
        )
        if len(examples) == 0:
          components_missing_assets.append(asset_component["name"])
        else:
          no_of_found_assets += 1

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
      with open(os.path.join(assets_output_path, f"{name}.md"), "w") as f:
        f.write(output_asset_component)

  # Create index file
  index_asset_components_template = environment.get_template("asset_components_index.html.jinja")
  outputIndex = index_asset_components_template.render(asset_categories=asset_categories)
  with open(f"{assets_output_path}/index.md", "w") as f:
    f.write(outputIndex)

  # Print out missing assets
  total = no_of_found_assets + len(components_missing_assets)
  percent_found = no_of_found_assets / (total) * 100
  components_missing_assets.sort()
  print(f"""

Number of found asset examples (ignoring base classes):
{no_of_found_assets} of {total}, or {percent_found:.1f}%

{"-" * 80}
{len(components_missing_assets)} asset components are missing example files:
{",".join(components_missing_assets)}
{"-" * 80}


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
  if not os.path.exists(scripting_output_path):
    os.mkdir(scripting_output_path)

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

json_location = "json"
output_folder = "generated"
folder_name_assets = "asset-components"
folder_name_scripting = "scripting-api"

# Load jinja templates folder
environment = Environment(loader=FileSystemLoader("templates"))

# Generate documentation
generate_asset_components(environment, output_folder, folder_name_assets, json_location)
generate_scripting_api(environment, output_folder, folder_name_scripting, json_location)
generate_renderable_overview(environment, output_folder, json_location)

