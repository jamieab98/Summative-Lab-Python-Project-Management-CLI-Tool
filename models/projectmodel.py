from utils.addproject import addproject
class Project:
    projects = []

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
        Project.projects.append(self)
        projectdata = {
            "title": self.title,
            "description": self.description,
            "due_data": self.due_date,
            "tasks": self.tasks
        }
        addproject(projectdata)
    
    def assign_task(self, task):
        self.tasks.append(task)
    
    '''def __repr__(self):
        return self.title'''