from datetime import datetime
#Project class for creating projects objects
class Project:
    
    projects = []

    def __init__(self, title, description, due_date, tasks=[]):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = tasks
        Project.projects.append(self)
    
    @property
    def due_date(self):
        return(self._due_date)
    
    @due_date.setter
    def due_date(self, value):
        if check_date(value):
            self._due_date = value
        else:
            raise ValueError("Date format must be 'mm/dd/yyyy")
    
    def assign_task(self, task):
        self.tasks.append(task)
    
    '''def __repr__(self):
        return self'''
    
def check_date(date):
    try:
        datetime.strptime(date, "%m/%d/%Y")
        return True
    except ValueError:
        return False