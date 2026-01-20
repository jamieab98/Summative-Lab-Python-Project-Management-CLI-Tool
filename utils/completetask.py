import json

def completetask(task):
    with open("data/data.json", "r") as f:
        content = json.load(f)
    taskcontent = [content for content in content['tasks'] if content['title'] == task][0]
    taskcontent['status'] = 'complete'
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)
