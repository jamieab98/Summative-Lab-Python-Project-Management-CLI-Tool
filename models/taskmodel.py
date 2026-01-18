from utils.addtask import addtask
class Task:
    tasks = []

    def __init__(self, title):
        self.title = title
        self.status = "incomplete"
        self.assigned_to = []
        Task.tasks.append(self)
        taskdata = {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }
        addtask(taskdata)
    
    def __repr__(self):
        return self.title