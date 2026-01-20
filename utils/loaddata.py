import json
from models.usermodel import User
from models.projectmodel import Project
from models.taskmodel import Task

def loaddata():
    with open("data/data.json", "r") as f:
        content = json.load(f)
    usercontent = content['users']
    for user in usercontent:
        User(user['name'], user['email'])
    projectcontent = content['projects']
    for project in projectcontent:
        Project(project['title'], project['description'], project['due_date'])
    taskcontent = content['tasks']
    for task in taskcontent:
        Task(task['title'])

loaddata()
print(Task.tasks)