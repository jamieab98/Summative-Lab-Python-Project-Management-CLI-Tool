import json

def addproject(title, description, due_date):
    projectdata = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'tasks': []
    }

    with open("data/data.json", "r") as f:
        content = json.load(f)
    content["projects"].append(projectdata)
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)