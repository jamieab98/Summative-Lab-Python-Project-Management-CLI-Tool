import json

def add_user(userdata):
    with open("data/userdata.json", "r") as f:
        content = json.load(f)
    content.append(userdata)
    with open("data/userdata.json", "w") as f:
        json.dump(content, f, indent=2)