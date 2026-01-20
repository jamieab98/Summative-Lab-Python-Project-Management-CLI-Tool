import json

def adduser(name, email):
    userdata = {
        'name': name,
        'email': email,
        'projects': []
    }
    with open("data/data.json", "r") as f:
        content = json.load(f)
    content["users"].append(userdata)
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)