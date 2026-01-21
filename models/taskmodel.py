class Task:
    tasks = []

    def __init__(self, title, status="incomplete"):
        self._title = title
        self._status = status
        self._id = len(Task.tasks)+1
        Task.tasks.append(self)
    
    @property
    def id(self):
        return self._id
    
    @property
    def title(self):
        return self._title
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if self._status == 'complete':
            raise ValueError("[bold red]The task has already been completed[/bold red]")
        else:
            self._status = 'complete'
    
    '''def __repr__(self):
        return self.status'''