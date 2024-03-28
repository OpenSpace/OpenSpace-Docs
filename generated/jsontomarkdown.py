import argparse # reading the command line parameters
import json # reading the input file
import os # file path magic

from jinja2 import Environment, FileSystemLoader # template magic

# Load jinja templates folder
environment = Environment(loader=FileSystemLoader("../templates/"))

################################################################################
#                              ASSET COMPONENTS                                #
################################################################################

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
        members = []
        # Add the base class members to each derived class
        if not hasBaseClass:
            members = assetComponent["members"]
        # If the component is the base class, don't add the base class members on top of it
        # (it would be duplicates)
        elif hasBaseClass and assetComponent["name"] == baseClass["name"]:
            members = baseClass["members"]
        # For derived classes, add the base class members first
        else:
            members = baseClass["members"] + assetComponent["members"]
        

        outputAssetComponent = assetComponentTemplate.render(data=assetComponent, members=members)
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

# Create target folder
folderNameScripting = "scriptingApi"
if not os.path.exists("./" + folderNameScripting):
    os.mkdir("./" + folderNameScripting)

# Opening JSON file
f = open('scriptingApi.json')

# Convert JSON String to Python Dictionary
documentation_data = json.load(f)
scriptingApi = documentation_data["data"]

# Create the pages for the scripting libraries
scriptingApiTemplate = environment.get_template("scriptingApiTemplate.txt")
for library in scriptingApi:
    # Go through all the functions in that library and print out a md file
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