import argparse

parser = argparse.ArgumentParser(description = "Program for managers to manage their users, projects, and tasks")
subparsers = parser.add_subparsers(dest = "command", required=True)

args = parser.parse_args()