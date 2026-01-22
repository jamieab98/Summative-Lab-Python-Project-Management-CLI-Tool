from models.usermodel import User
from models.projectmodel import Project
from models.taskmodel import Task

u = User("Ashley", "ashleyjones@gmail.com")

assert u.name == "Ashley", "User name was not set correctly"
assert u.email == "ashleyjones@gmail.com", "Email was not set correctly"

p1 = Project("project49", "Run a marathon in less than 4 hours", "12/31/2027")
p2 = Project("project67", "Save 1x yearly salary in saving account", "09/09/2028")

assert p1.title == "project49", "Project title was not set correctly"
assert p1.description == "Run a marathon in less than 4 hours", "Project description was not correctly set"
assert p1.due_date == "12/31/2027", "Project due date was not correctly set"
assert p1.tasks == []
assert p2.title == "project67", "Project title was not set correctly"
assert p2.description == "Save 1x yearly salary in saving account", "Project description was not correctly set"
assert p2.due_date == "09/09/2028", "Project due date was not correctly set"
assert p2.tasks == []

t1 = Task("Sign up for a marathon")
t2 = Task("Complete 4 half marathons")
t3 = Task("Complete a half marathon in less than 2 hours")
t4 = Task("Create a budget")
t5 = Task("Get rid of all credit card debt")

assert t1.title == "Sign up for a marathon", "Task title was not set correctly"
assert t2.title == "Complete 4 half marathons", "Task title was not set correctly"
assert t3.title == "Complete a half marathon in less than 2 hours", "Task title was not set correctly"
assert t4.title == "Create a budget", "Task title was not set correctly"
assert t5.title == "Get rid of all credit card debt", "Task title was not set correctly"