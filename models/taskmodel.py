class Task:
    tasks = []

    def __init__(self, title):
        self.title = title
        self.status = "incomplete"
        self.assigned_to = []
        Task.tasks.append(self)
    
    def __repr__(self):
        return self.title

task1 = Task("Complete the Summative Lab Assignment for Module 7")