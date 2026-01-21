class Task:
    tasks = []

    def __init__(self, title, status="incomplete"):
        self._title = title
        self.status = status
        self._id = len(Task.tasks)+1
        Task.tasks.append(self)
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    '''def __repr__(self):
        return self.status'''