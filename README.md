Make sure to install rich with 
    pip install rich

To use the CLI, select one of the following commands:
    add_user
    add_project
    assign_project
    add_task
    complete_task
    list_users
    users_projects
    incomplete_tasks

Then go into the console and type
    "python3 main.py *insert command here* *insert command arguments*

See below on the syntax for all commands
    add_user *name* *email*
    add_project *title* *description* *due_date*
    assign_project *user* *project title*
    add_task *task title* *project title*
    complete_task *task id*
    list_users
    users_projects *name*
    incomplete_tasks *project title*

Notes:

When typing in arguments for any commands, make sure to it is one string of text per argument or surround the argument with parenthesis

When inputting the due date for a project, the format but be mm/dd/yyyy

To see the id of tasks, use the incomplete_tasks command