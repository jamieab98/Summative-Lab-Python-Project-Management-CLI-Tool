class Project:
    projects = []

    def __init__(self, title, description, due_date, tasks=[]):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = tasks
        Project.projects.append(self)
    
    def assign_task(self, task):
        self.tasks.append(task)
    
    def __repr__(self):
        return self.title