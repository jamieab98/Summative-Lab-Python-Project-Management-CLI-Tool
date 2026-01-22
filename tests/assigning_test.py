from utils.assign_project import assignproject
import json

mockdata = {
    "users": [
        {
        "name": "Ashley",
        "email": "ashleyjones@gmail.com",
        "projects": []
        }
    ],
    "projects": [
        {
        "title": "project49",
        "description": "Run a marathon in less than 4 hours",
        "due_date": "12/31/2027",
        "tasks": []
        }
    ]
}

def fakeload(f):
    return mockdata.copy()
def fakedump(data, f, indent=2):
    global mockdata
    mockdata = data

json.load = fakeload
json.dump = fakedump

assignproject("Ashley", "project49")
assert mockdata['users'][0]['projects'][0] == 'project49'
