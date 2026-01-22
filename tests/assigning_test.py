import utils.assign_project as ap
from utils.assign_project import assignproject

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
    return mockdata
def fakedump(data, f, indent=2):
    global mockdata
    mockdata = data

ap.json.load = fakeload
ap.json.dump = fakedump

assignproject("Ashley", "project49")