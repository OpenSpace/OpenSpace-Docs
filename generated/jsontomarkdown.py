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

category = assetCategories[2]
# Find base class to add its members to each derived class
baseclassName = category["name"]
baseClass = None
for x in category["classes"]:
    if x["name"] == baseclassName:
        baseClass = x
        break
for assetComponent in category["classes"]:
    members = baseClass["members"]
    if not assetComponent["name"] == baseclassName:
        members = members + assetComponent["members"]
        print(assetComponent["name"])
    outputAssetComponent = assetComponentTemplate.render(data=assetComponent, members=members)
    with open(assetComponent["name"]+'.md', 'w') as f:
        f.write(outputAssetComponent)

outputIndex = indexTemplate.render(category=category)
with open('index.md', 'w') as f:
    f.write(outputIndex)

# Print Dictionary
# print(documentation_data)