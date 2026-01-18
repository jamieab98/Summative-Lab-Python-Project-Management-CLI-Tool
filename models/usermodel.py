from utils.adduser import add_user
from utils.assign_project import assignproject
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
        add_user(userdata)

    def assign_project(self, project):
        self.projects.append(project)
        assignproject(self.name, project)

    '''def __repr__(self):
        return(self.name)'''