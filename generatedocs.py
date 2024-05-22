from git import Repo # git for downloading assets
from jinja2 import Environment, FileSystemLoader # template magic
import json # reading the input file
import os # file paths
import re # regex for searching for assets files
from tqdm import tqdm # progress bar

################################################################################
#                      ASSET COMPONENTS HELPER FUNCTIONS                       #
################################################################################

# Clones asset directory from OpenSpace git repository
# Uses the latest master
# Returns absolute path to the asset folder
def cloneAssetsFolderGit(folderName):
    def printProgress(op_code, cur_count, max_count=None, message=''):
        print(message)

    print("Cloning assets examples...")
    repo = Repo.init(folderName)
    branchName = "origin/master"

    # Create a new remote if there isn't one already created
    origin = repo.remotes[0] if len(repo.remotes) > 0 else None 
    if not origin:
        print("No remote origin found. Creating OpenSpace remote...")
        origin = repo.create_remote("origin", "https://github.com/OpenSpace/OpenSpace")

    print("Fetching OpenSpace on branch {}... this might take a while".format(branchName))
    origin.fetch(progress=printProgress)

    dataAssetsPath = "data/assets" 
    git = repo.git()
    git.checkout(branchName, "--", dataAssetsPath)
    print("Done cloning assets folder from OpenSpace repository")
    assetsFolderPath = os.path.abspath(os.path.join(folderName, dataAssetsPath))
    return assetsFolderPath

# Returns the number of lines in a file
def getFileLength(path):
    try:
        # Read binary file as it is faster and we only want to know the length
        with open(path, 'rb') as fp:
            if fp.readable():
                length = len(fp.read()) 
                return length
            else:
                return None
    except IOError:
        input("Could not open file path ", path)
        return None

# Find all .asset files in the root dir and subdirs
def assetsInPathRecursive(root):
    filenames = []

    for path, subdirs, files in os.walk(root):
        for file in files:
            if file.endswith(".asset"):
                filenames.append(os.path.join(path, file))

    return filenames 

# Find all .assets in directory - no subdirs
def assetsInPath(path):    
    filenames = [filename for filename in os.listdir(path) if filename.endswith(".asset")]
    # Prepend the path to the filename
    return list(map(lambda filename: os.path.join(path, filename), filenames))

# Matches an asset component name with the words in a file
# Returns the content of the file and the lines where the 
# matches occured, as well as the header if specified
def getLinesAndContentFromFile(assetFile, regex, lookForHeader = False):
    lines = []
    isHeaderComment = True
    header = ""
    content = ""
    description = ""
    luaComment = "-- "
    headerFinished = 0
    with open(assetFile, 'r', encoding='utf8') as file:
        if not file.readable():
            return None
        # Read file line by line
        for l_no, line in enumerate(file, 1):
            # Check for header comment at top of file 
            if not line.startswith(luaComment):
                isHeaderComment = False
            
            # If we are in header comment, split into header 
            # and description
            if lookForHeader and isHeaderComment:
                comment = line.split(luaComment)[1]
                if l_no == 1:
                    header = comment
                else:
                    description += comment
                    headerFinished = l_no + 1
            # Else, get the content of the example
            else:
                content += line
                # Search for the regex pattern
                if re.search(regex, line):
                    # If the header has been removed we need to adjust the line number
                    lines.append(l_no - headerFinished)

    # If there were any matches to regex, set the content as the example
    if len(lines) > 0:
        return { "header": header, "description": description, "content": content, "lines": lines }
    else: 
        return None

# Takes an asset component name and matches it to all files in a 
# path, and return the shortest asset with matches.
def findShortestAssetInPath(path, name):
    assetFiles = assetsInPathRecursive(path)
    # Sort by shortest asset file first                
    # This will ensure the simplest asset is displayed
    assetFiles.sort(key=getFileLength)

    # Find first example matching the asset component (files are sorted by length)
    for assetFile in assetFiles:   
        # Search for Type = "<name>"
        regex = r'Type = \"' + name + r'\"'
        example = getLinesAndContentFromFile(assetFile, regex)
        if example:
            return example
    # If nothing found, return None
    return None

# Search through all example assets for the component name
# Returns file content and line numbers for where the name occurs
def findAssetExample(assetsFolder, category, name):
    examplesFolder = os.path.join(assetsFolder, "examples")
    
    # Search pass 1: look up folder “assets/<category>/<assetcomponentname>/”
    # and see if it exists. If it does, add all files in that folder (no subdirectories)
    assetDirectory = os.path.join(examplesFolder, (os.path.join(category, name)).lower())
    if os.path.exists(assetDirectory):
        filenames = assetsInPath(assetDirectory)
        examples = []
        for filename in filenames:
            # We search for the asset component <name> or "<name>"
            regex = r'\b' + name + r'\b|\b\"' + name + r'\"\b'
            example = getLinesAndContentFromFile(filename, regex, True)
            examples.append(example)
        return examples

    # Search pass 2: search through all assets in the **examples** folder and add the 
    # shortest asset
    example = findShortestAssetInPath(examplesFolder, name)
    if example:
        return [example]
    
    # Search pass 3: search through all assets in the **assets** folder and add the 
    # shortest asset
    example = findShortestAssetInPath(assetsFolder, name)
    if example:
        return [example]
    
    # If nothing found, return empty array
    return []

# Group members by optionality while preserving the alphabetical order
def groupMembersByOptionality(members):
    nonOptionalIndices = []
    optionalIndices = []
    for i, member in enumerate(members):
        if member["optional"]:
            optionalIndices.append(i)
        else:
            nonOptionalIndices.append(i)
    indices = nonOptionalIndices + optionalIndices
    return [members[i] for i in indices]

def findAssetScreenshot(name):
    imageDirectory = "_static/images/renderables"
    imgPath = imageDirectory + '/' + name + '.png'
    if os.path.exists(imgPath):
        return imgPath
    return None

################################################################################
#                         SCRIPTING API HELPER FUNCTIONS                       #
################################################################################

# This function modifies the scripting library so that the doxygen 
# comments are added to the arguments
# Supported doxygen parameters: \param \return \code
def parseDoxygenComments(library):
    for function in library["functions"]:
        [helpText, p, returnDescription] = function["help"].partition('\\\\return')
        
        # Parse code blocks
        helpText = helpText.replace('\\\\code', '\n:::{code-block} lua\n')
        helpText = helpText.replace('\\\\endcode', '\n:::')

        # Split help text into parameters and return type
        helpText = helpText.split('\\\\param ')
        # First substring will be the description
        description = helpText[0].strip()
        # Add to the dictionary
        function["help"] = description
        # Collect the params, everything after the 1st
        params = helpText[1:]
        identifiers = []
        argumentDescriptions = []
        for param in params:
            [identifier, ws, paramsDescription] = param.partition(" ")
            identifiers.append(identifier)
            argumentDescriptions.append(paramsDescription)
        
        # Add params to the dictionary
        for argument in function["arguments"]:
            if argument["name"] in identifiers:
                index = identifiers.index(argument["name"])
                argument["description"] = argumentDescriptions[index]
        # Add return type to the dictionary, if there is one
        if returnDescription:
            function["returnDescription"] = returnDescription
        
    return library

################################################################################
#                            CREATE ASSET COMPONENTS                           #
################################################################################

def generateAssetComponents(environment, outputFolder, folderNameAssets, jsonLocation):
    assetsExamplesFolderName = "assetExamples"
    # Download assets files from OpenSpace repository
    assetsFolder = cloneAssetsFolderGit(os.path.join(outputFolder, assetsExamplesFolderName))

    # Create target folder
    assetsOutputPath = os.path.join(outputFolder, folderNameAssets)
    if not os.path.exists(assetsOutputPath):
        os.mkdir(assetsOutputPath)

    # Open JSON file
    f = open(os.path.join(jsonLocation, 'assetComponents.json'))

    # Convert JSON String to Python Dictionary
    assetCategories = json.load(f)

    # Create pages for the asset component pages
    assetComponentTemplate = environment.get_template("assetComponentTemplate.txt")

    # Missing and found asset files
    componentsMissingAssets = []
    noOfFoundAssets = 0
    for category in assetCategories:
        # Find base class to add its members to each derived class
        baseclassName = category["name"]
        baseClass = None
        hasBaseClass = False
        for assetComponent in category["classes"]:
            if assetComponent["name"] == baseclassName:
                baseClass = assetComponent
                hasBaseClass = True
                break
        
        # Go through all the components in that category and print out a md file
        for assetComponent in tqdm(category["classes"], desc="Generating asset components for " + category["name"]):
            isBaseClass = hasBaseClass and assetComponent["name"] == baseClass["name"]
            baseClassName = baseClass["name"] if hasBaseClass and not isBaseClass else ""
            baseClassIdentifier = baseClass["identifier"] if hasBaseClass and not isBaseClass else ""
            baseClassMembers = []

            # Add the base class members to each derived class
            # If the component is the base class
            if hasBaseClass and not isBaseClass:
                baseClassMembers = groupMembersByOptionality(baseClass["members"])
            
            groupedMembers = groupMembersByOptionality(assetComponent["members"])

            # Find example for the asset component, if it is not a baseclass component
            examples = []
            if not isBaseClass:
                examples = findAssetExample(assetsFolder, category["name"], assetComponent["name"])
                if len(examples) == 0:
                    componentsMissingAssets.append(assetComponent["name"])
                else:
                    noOfFoundAssets += 1
            


            # Render component page with jinja
            outputAssetComponent = assetComponentTemplate.render(
                data=assetComponent, 
                baseClassName=baseClassName,
                baseClassIdentifier=baseClassIdentifier,
                baseClassMembers=baseClassMembers, 
                members=groupedMembers,
                examples=examples
                )
            with open(os.path.join(assetsOutputPath, assetComponent["name"]+'.md'), 'w') as f:
                f.write(outputAssetComponent)

    # Create index file
    indexAssetComponentsTemplate = environment.get_template("indexAssetComponentsTemplate.txt")
    outputIndex = indexAssetComponentsTemplate.render(assetCategories=assetCategories)
    with open(assetsOutputPath + '/index.md', 'w') as f:
        f.write(outputIndex)

    # Print out missing assets
    total = noOfFoundAssets + len(componentsMissingAssets)
    percentFound = noOfFoundAssets / (total) * 100
    print('\n\n')
    print("Number of found asset examples (ignoring base classes):")
    print(noOfFoundAssets, "of", total, "or", "%.1f" % percentFound, "%\n")
    line = "-" * 80 
    print(line)
    print(len(componentsMissingAssets), "asset components are missing example files:")
    print(line) 
    print('\n'.join(componentsMissingAssets).join("\n\n\n"))


################################################################################
#                            CREATE SCRIPTING API                              #
################################################################################

def generateScriptingApi(environment, outputFolder, folderNameScripting, jsonLocation):
    # Create target folder
    scriptingOutputPath = os.path.join(outputFolder, folderNameScripting)
    if not os.path.exists(scriptingOutputPath):
        os.mkdir(scriptingOutputPath)

    # Opening JSON file
    f = open(os.path.join(jsonLocation, 'scriptingApi.json'))

    # Convert JSON String to Python Dictionary
    scriptingApi = json.load(f)

    # Create the pages for the scripting libraries
    scriptingApiTemplate = environment.get_template("scriptingApiTemplate.txt")
    for library in scriptingApi:
        # Go through all the functions in that library and print out a md file
        library = parseDoxygenComments(library)
        outputLibrary = scriptingApiTemplate.render(library=library)
        with open(os.path.join(scriptingOutputPath, library["fullName"]+'.md'), 'w') as f:
            f.write(outputLibrary)

    # Create index file
    indexScriptingTemplate = environment.get_template("indexScriptingTemplate.txt")
    outputIndex = indexScriptingTemplate.render(libraries=scriptingApi)
    with open(os.path.join(scriptingOutputPath, "index.md"), 'w') as f:
        f.write(outputIndex)

################################################################################
#                         CREATE RENDERABLE OVERVIEW                           #
################################################################################

def generateRenderableOverview(environment, outputFolder, folderNameAssets, jsonLocation):
    # Open JSON file
    f = open(os.path.join(jsonLocation, 'assetComponents.json'))

    # Convert JSON String to Python Dictionary
    assetCategories = json.load(f)
    
    images = {}
    renderables = []
    for category in assetCategories:
        if category["name"] == "Renderable" or category["name"] == "ScreenSpaceRenderable":
            for assetComponent in category["classes"]:
                if assetComponent["name"] == category["name"]:
                    # Base class - ignore
                    continue
                                                      
                # Find example image
                image = findAssetScreenshot(assetComponent["name"])
                if image:
                    images[assetComponent["name"]] = image
                renderables.append(assetComponent)

    # Create overview file
    renderableOverviewTemplate = environment.get_template("renderableOverviewTemplate.txt")
    outputOverview = renderableOverviewTemplate.render(folderNameAssets=folderNameAssets,
                                                       renderables=renderables, 
                                                       images=images
                                                       )
    with open(os.path.join(outputFolder, "renderableOverview.md"), "w") as f:
        f.write(outputOverview)

################################################################################
#                             CREATE INDEX FILE                                #
################################################################################

def generateIndexFile(environment, outputFolder, folderNameScripting, folderNameAssets):
    indexTemplate = environment.get_template("indexTemplate.txt")

    outputIndex = indexTemplate.render(
        folderNameScripting=folderNameScripting, 
        folderNameAssets=folderNameAssets,
        renderableOverview="renderableOverview"    
    )
    with open(os.path.join(outputFolder, "index.md"), "w") as f:
        f.write(outputIndex)

jsonLocation = "json"
outputFolder = "generated"
folderNameAssets = "assetComponents"
folderNameScripting = "scriptingApi"

# Load jinja templates folder
environment = Environment(loader=FileSystemLoader("templates"))

# Generate documentation
generateAssetComponents(environment, outputFolder, folderNameAssets, jsonLocation)
generateScriptingApi(environment, outputFolder, folderNameScripting, jsonLocation)
generateRenderableOverview(environment, outputFolder, folderNameAssets, jsonLocation)
generateIndexFile(environment, outputFolder, folderNameScripting, folderNameAssets)

