class Task:
    tasks = []

    def __init__(self, title, status="incomplete"):
        self.title = title
        self.status = status
        self.id = len(Task.tasks)+1
        Task.tasks.append(self)
    
    '''def __repr__(self):
        return self.status'''