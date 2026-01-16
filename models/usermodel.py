class User:
    users = []

    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.projects = []
        User.users.append(self)

    def __repr__(self):
        return(self.name)