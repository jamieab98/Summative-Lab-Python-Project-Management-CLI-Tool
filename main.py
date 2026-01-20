import argparse
from models.usermodel import User
from models.projectmodel import Project
from models.taskmodel import Task
from utils.assign_project import assignproject
from utils.assign_task import assigntask
from utils.completetask import completetask
from utils.adduser import adduser
from utils.addproject import addproject
from utils.addtask import addtask
from utils.loaddata import loaddata

def main():

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

    add_task = subparsers.add_parser("add_task", help="Add a task to the database and assign it to a project")
    add_task.add_argument("task", type=str)
    add_task.add_argument("project", type=str)

    complete_task = subparsers.add_parser("complete_task", help="Mark a task as complete")
    complete_task.add_argument("task", type=str)

    list_users = subparsers.add_parser("list_users", help="Get a list of users")

    users_projects = subparsers.add_parser("users_projects", help="Get a list of projects assigned to a specific user")
    users_projects.add_argument("user", type=str)

    args = parser.parse_args()

    loaddata()

    if args.command == "add_user":
        User(args.user, args.email)
        adduser(args.user, args.email)
    if args.command == "add_project":
        Project(args.project, args.description, args.due_date)
        addproject(args.project, args.description, args.due_date)
    if args.command == "add_task":
        Task(args.task)
        addtask(args.task)
        assigntask(args.task, args.project)
    if args.command == "assign_project":
        '''Add these lines back in once we have the script running constantly'''
        '''u = [user for user in User.users if user.name == args.user][0]'''
        '''u.assign_project(args.project)'''
        assignproject(args.user, args.project)
    if args.command == "complete_task":
        completetask(args.task)
    if args.command == "list_users":
        print(User.users)
    if args.command == "users_projects":
        userprojects = [user.projects for user in User.users if user.name == args.user][0]
        print(userprojects)
    

if __name__ == "__main__":
    main()