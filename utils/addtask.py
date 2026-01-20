import json

def addtask(title):
    taskdata = {
        'title': title,
        'status': 'incomplete'
    }
    with open("data/data.json", "r") as f:
        content = json.load(f)
    content["tasks"].append(taskdata)
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)