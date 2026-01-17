from utils.adduser import add_user
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

    '''def __repr__(self):
        return(self.name)'''

user1 = User("jamie", "jamieab98@gmail.com")