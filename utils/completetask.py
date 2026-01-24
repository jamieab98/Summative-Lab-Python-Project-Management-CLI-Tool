import json

#function to take a task and change the status attribute
def completetask(taskid):
    with open("data/data.json", "r") as f:
        content = json.load(f)
    taskcontent = [content for content in content['tasks'] if content['id'] == taskid][0]
    taskcontent['status'] = 'complete'
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)