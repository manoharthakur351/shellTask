# ShellTask

A command line tool for managing and tracking tasks on Linux operating systems, developed by Andrew.

Features:
- Create new tasks using the -n flag
- View a list of all your current tasks
- Mark tasks as complete
- Edit existing tasks using the -e flag
- Delete tasks

Installation:
To use this tool, you will need to have a Linux operating system installed on your computer. 

Usage:
Once the tool is installed, you can run it by typing "tasks" in your terminal. This will display a list of all available commands and options.

Creating a new task:
To create a new task, run the following command:
tasks -n "Task description"

Viewing all tasks:
To view a list of all your current tasks, run the following command:
tasks list

Marking a task as complete:
To mark a task as complete, run the following command:
tasks complete [task_id]

Editing a task:
To edit an existing task, run the following command:
tasks -e [task_id] "New task description"

Deleting a task:
To delete a task, run the following command:
tasks delete [task_id]


