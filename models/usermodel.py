from utils.assign_project import assignproject
class User:
    users = []

    def __init__ (self, name, email, projects=[]):
        self.name = name
        self.email = email
        self.projects = projects
        User.users.append(self)

    def assign_project(self, project):
        self.projects.append(project)
        assignproject(self.name, project)

    def __repr__(self):
        return(self.name)
