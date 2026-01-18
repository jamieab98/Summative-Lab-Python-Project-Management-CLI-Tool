import json

def addproject(projectdata):
    with open("data/data.json", "r") as f:
        content = json.load(f)
    content["projects"].append(projectdata)
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)