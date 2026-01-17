import json
class User:
    users = []

    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.projects = []
        User.users.append(self)
        userdata = {
            "name": self.name,
            "email": self.email,
            "projects": self.projects
        }
        with open("data/userdata.json", "r") as f:
            data = json.load(f)
        with open("data/userdata.json", "w") as f:
            data.append(userdata)
            json.dump(data, f, indent=2) 

    def assign_project(self, project):
        self.projects.append(project)

    '''def __repr__(self):
        return(self.name)'''

user1 = User("jamie", "jamieab98@gmail.com")