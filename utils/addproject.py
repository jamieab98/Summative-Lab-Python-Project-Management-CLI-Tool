import json

def addproject(projectdata):
    with open("data/projectdata.json", "r") as f:
        content = json.load(f)
    content.append(projectdata)
    with open("data/projectdata.json", "w") as f:
        json.dump(content, f, indent=2)