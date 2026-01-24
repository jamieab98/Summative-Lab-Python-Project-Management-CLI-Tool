import json
from models.taskmodel import Task

#function to create a task object
def addtask(title):
    taskdata = {
        'title': title,
        'status': 'incomplete',
        'id': len(Task.tasks)
    }
    with open("data/data.json", "r") as f:
        content = json.load(f)
    content["tasks"].append(taskdata)
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)