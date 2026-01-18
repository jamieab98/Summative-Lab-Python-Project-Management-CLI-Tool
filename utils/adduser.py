import json

def add_user(userdata):
    with open("data/data.json", "r") as f:
        content = json.load(f)
    content["users"].append(userdata)
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)