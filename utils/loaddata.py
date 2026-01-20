import json
from models.usermodel import User
from models.projectmodel import Project
from models.taskmodel import Task

def loaddata():
    with open("data/data.json", "r") as f:
        content = json.load(f)

    taskcontent = content['tasks']
    for task in taskcontent:
        Task(task['title'], task['status'])

    projectcontent = content['projects']
    for project in projectcontent:
        Project(project['title'], project['description'], project['due_date'], project['tasks'])

    usercontent = content['users']
    for user in usercontent:
        User(user['name'], user['email'], user['projects'])
    
    print('Data loaded')