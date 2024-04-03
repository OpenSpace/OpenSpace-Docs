import argparse # reading the command line parameters
import json # reading the input file
import os # file path magic
import re

from jinja2 import Environment, FileSystemLoader # template magic

# Find all .asset files in the root dir and subdirs
def allAssetExamplePaths():
    root = "C:/Users/Ylva/Documents/OpenSpace/OpenSpace/data/assets/examples"
    filenames = []

    for path, subdirs, files in os.walk(root):
        for file in files:
            if file.endswith(".asset"):
                filenames.append(os.path.join(path, file))

    return filenames

# Search through all example assets for the component name
# Returns file content and line numbers for where the name occurs
def findAssetExample(name):
    filenames = allAssetExamplePaths()

    # Find example for the asset component
    example = None
    lines = []
    for assetExample in filenames:   
        # Only find one example
        if example:
            break      
        with open(assetExample, 'r') as file:
            content = ""
            for l_no, line in enumerate(file, 1):
                content += line
                # Search for the exact name or name with quotation marks
                regex = r'\b' + name + r'\b|\b\"' + name + r'\"\b'
                if re.search(regex, line):
                    lines.append(l_no)
            # If there were any matches, set the content as the example
            if len(lines) > 0:
                example = content

    return [example, lines]

# Load jinja templates folder
environment = Environment(loader=FileSystemLoader("../templates/"))

################################################################################
#                              ASSET COMPONENTS                                #
################################################################################

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

# Create target folder
folderNameAssets = "assetComponents"
if not os.path.exists("./" + folderNameAssets):
    os.mkdir("./" + folderNameAssets)

# Opening JSON file
f = open('assetComponents.json')

# Convert JSON String to Python Dictionary
documentation_data = json.load(f)
assetCategories = documentation_data["data"]

# Create pages for the asset component pages
assetComponentTemplate = environment.get_template("assetComponentTemplate.txt")
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
    for assetComponent in category["classes"]:
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
        example = None
        lines = []
        if not isBaseClass:
            [example, lines] = findAssetExample(assetComponent["name"])
        
        # Render component page with jinja
        outputAssetComponent = assetComponentTemplate.render(
            data=assetComponent, 
            baseClassName=baseClassName,
            baseClassIdentifier=baseClassIdentifier,
            baseClassMembers=baseClassMembers, 
            members=groupedMembers,
            example=example,
            lines=lines
            )
        with open(folderNameAssets + '/' + assetComponent["name"]+'.md', 'w') as f:
            f.write(outputAssetComponent)

# Create index file
indexAssetComponentsTemplate = environment.get_template("indexAssetComponentsTemplate.txt")
outputIndex = indexAssetComponentsTemplate.render(assetCategories=assetCategories)
with open(folderNameAssets + '/index.md', 'w') as f:
    f.write(outputIndex)


################################################################################
#                                 SCRIPTING API                                #
################################################################################

# This function modifies the library so that the doxygen comments are added to the 
# arguments
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

# Create target folder
folderNameScripting = "scriptingApi"
if not os.path.exists("./" + folderNameScripting):
    os.mkdir("./" + folderNameScripting)

# Opening JSON file
f = open('scriptingApi.json')

# Convert JSON String to Python Dictionary
documentation_data = json.load(f)
scriptingApi = documentation_data["data"]
parseDoxygenComments(scriptingApi[0])

# Create the pages for the scripting libraries
scriptingApiTemplate = environment.get_template("scriptingApiTemplate.txt")
for library in scriptingApi[:1]:
    # Go through all the functions in that library and print out a md file
    library = parseDoxygenComments(library)
    outputLibrary = scriptingApiTemplate.render(library=library)
    with open(folderNameScripting + "/" + library["fullName"]+'.md', 'w') as f:
        f.write(outputLibrary)

# Create index file
indexScriptingTemplate = environment.get_template("indexScriptingTemplate.txt")
outputIndex = indexScriptingTemplate.render(libraries=scriptingApi)
with open(folderNameScripting + "/" + "index.md", 'w') as f:
    f.write(outputIndex)

################################################################################
#                             CREATE INDEX FILE                                #
################################################################################

indexTemplate = environment.get_template("indexTemplate.txt")

outputIndex = indexTemplate.render(folderNameScripting=folderNameScripting, folderNameAssets=folderNameAssets)
with open("index.md", 'w') as f:
    f.write(outputIndex)