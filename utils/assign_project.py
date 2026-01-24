import json

#function to make a user object own a specific project object
def assignproject(user, project):
    with open("data/data.json", "r") as f:
        content = json.load(f)
    usercontent = [content for content in content['users'] if content['name'] == user][0]
    usercontent['projects'].append(project)
    with open("data/data.json", "w") as f:
        json.dump(content, f, indent=2)
