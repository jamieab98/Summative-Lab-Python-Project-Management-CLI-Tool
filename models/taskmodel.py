class Task:
    tasks = []

    def __init__(self, title):
        self.title = title
        self.status = "incomplete"
        Task.tasks.append(self)
    
    '''def __repr__(self):
        return self.title'''