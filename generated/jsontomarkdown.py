import argparse # reading the command line parameters
import json # reading the input file
import os # file path magic

from jinja2 import Environment, FileSystemLoader # template magic

# Opening JSON file
f = open('documentationData.json')

# Convert JSON String to Python Dictionary
documentation_data = json.load(f)

assetCategories = documentation_data["documentation"][7]["data"]

environment = Environment(loader=FileSystemLoader("../templates/"))
assetComponentTemplate = environment.get_template("assetComponentTemplate.txt")
indexTemplate = environment.get_template("indexTemplate.txt")

for category in assetCategories:
    # Find base class to add its members to each derived class
    baseclassName = category["name"]
    baseClass = None
    for x in category["classes"]:
        if x["name"] == baseclassName:
            baseClass = x
            break
    for assetComponent in category["classes"]:
        members = []
        if baseClass != None and "members" in baseClass.keys() and assetComponent["name"] != baseclassName:
            members += baseClass["members"] 
        if  "members" in assetComponent.keys():
            members += assetComponent["members"]

        outputAssetComponent = assetComponentTemplate.render(data=assetComponent, members=members)
        with open(assetComponent["name"]+'.md', 'w') as f:
            f.write(outputAssetComponent)

outputIndex = indexTemplate.render(assetCategories=assetCategories)
with open('index.md', 'w') as f:
    f.write(outputIndex)

# Print Dictionary
# print(documentation_data)