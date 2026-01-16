import argparse

parser = argparse.ArgumentParser(description = "Program for managers to manage their users, projects, and tasks")
subparsers = parser.add_subparsers(dest = "command", required=True)

add_user = subparsers.add_parser("add_user", help="Add a user to the database")
add_user.add_argument("user", type=str)

add_project = subparsers.add_parser("add_project", help="Add a project to the database")
add_project.add_argument("project", type=str)

assign_project = subparsers.add_parser("assign_project", help="Take a user and assign them a project")
assign_project.add_argument("user", type=str)
assign_project.add_argument("project", type=str)

add_task = subparsers.add_parser("add_task", help="Add a task to the database")
add_task.add_argument("task", type=str)

args = parser.parse_args()

if args.command == "add_user":
    print(args.user)
if args.command == "add_project":
    print(args.project)
if args.command == "add_task":
    print(args.task)
if args.command == "assign_project":
    print(f"Assign {args.project} to {args.user}")