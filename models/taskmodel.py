class Task:
    tasks = []
    def __init__(self, title):
        self.title = title
        self.status = "incomplete"
        self.assigned_to = []