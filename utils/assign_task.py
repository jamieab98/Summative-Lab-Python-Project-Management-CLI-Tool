import json

#function to make a specific project object own a task object
def assigntask(task, project):
    with open("data/data.json", "r") as f:
        content = json.load(f)
    projectcontent = [content for content in content['projects'] if content['title'] == project][0]
    projectcontent['tasks'].append(task)
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)