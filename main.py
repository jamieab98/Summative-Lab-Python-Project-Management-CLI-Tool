import argparse

parser = argparse.ArgumentParser(description = "Program for managers to manage their users, projects, and tasks")
subparsers = parser.add_subparsers(dest = "command", required=True)

add_user = subparsers.add_parser("add_user")
add_user.add_argument("user", type=str)

add_project = subparsers.add_parser("add_project")
add_project.add_argument("project", type=str)

args = parser.parse_args()

if args.command == "add_user":
    print(args.user)
if args.command == "add_project":
    print(args.project)