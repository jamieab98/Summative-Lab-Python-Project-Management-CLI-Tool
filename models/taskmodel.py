class Task:
    tasks = []

    def __init__(self, title, status="incomplete"):
        self.title = title
        self.status = status
        Task.tasks.append(self)
    
    '''def __repr__(self):
        return self.status'''