import json

def addtask(taskdata):
    with open("data/taskdata.json", "r") as f:
        content = json.load(f)
    content.append(taskdata)
    with open("data/taskdata.json", "w") as f:
        json.dump(content, f, indent = 2)