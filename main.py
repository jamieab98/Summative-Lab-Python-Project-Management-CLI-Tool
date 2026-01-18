import argparse
from models.usermodel import User
from models.projectmodel import Project
from models.taskmodel import Task
from utils.assign_project import assignproject

parser = argparse.ArgumentParser(description = "Program for managers to manage their users, projects, and tasks")
subparsers = parser.add_subparsers(dest = "command", required=True)

add_user = subparsers.add_parser("add_user", help="Add a user to the database")
add_user.add_argument("user", type=str)
add_user.add_argument("email", type=str)

add_project = subparsers.add_parser("add_project", help="Add a project to the database")
add_project.add_argument("project", type=str)
add_project.add_argument("description", type=str)
add_project.add_argument("due_date", type=str)

assign_project = subparsers.add_parser("assign_project", help="Take a user and assign them a project")
assign_project.add_argument("user", type=str)
assign_project.add_argument("project", type=str)

add_task = subparsers.add_parser("add_task", help="Add a task to the database")
add_task.add_argument("task", type=str)

assign_task = subparsers.add_parser("assign_task", help="Take a project and assign a task to it")
assign_task.add_argument("project", type=str)
assign_task.add_argument("task", type=str)

args = parser.parse_args()

if args.command == "add_user":
    User(args.user, args.email)
if args.command == "add_project":
    Project(args.project, args.description, args.due_date)
if args.command == "add_task":
    Task(args.task)
if args.command == "assign_project":
    '''u = [user for user in User.users if user.name == args.user][0]'''
    '''u.assign_project(args.project)'''
    assignproject(args.user, args.project)
if args.command == "assign_task":
    p = [project for project in Project.projects if project.title == args.project][0]
    p.assign_task(args.task)