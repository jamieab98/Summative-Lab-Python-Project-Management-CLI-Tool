from utils.addtask import addtask
class Task:
    tasks = []

    def __init__(self, title):
        self.title = title
        self.status = "incomplete"
        Task.tasks.append(self)
        taskdata = {
            "title": self.title,
            "status": self.status,
        }
        addtask(taskdata)
    
    def __repr__(self):
        return self.title