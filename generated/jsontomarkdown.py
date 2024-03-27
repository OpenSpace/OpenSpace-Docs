import argparse # reading the command line parameters
import json # reading the input file
import os # file path magic

from jinja2 import Environment, FileSystemLoader # template magic

# Opening JSON file
f = open('assetComponents.json')

# Convert JSON String to Python Dictionary
documentation_data = json.load(f)

assetCategories = documentation_data["data"]

environment = Environment(loader=FileSystemLoader("../templates/"))
assetComponentTemplate = environment.get_template("assetComponentTemplate.txt")
indexTemplate = environment.get_template("indexTemplate.txt")

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
        with open(assetComponent["name"]+'.md', 'w') as f:
            f.write(outputAssetComponent)

outputIndex = indexTemplate.render(assetCategories=assetCategories)
with open('index.md', 'w') as f:
    f.write(outputIndex)


# Print Dictionary
# print(documentation_data)