  # TODO MANAGER
    #### Video Demo:  https://youtu.be/hFtnSEQgIkU
    #### Description:
    The To-Do List Manager is a Python project that allows users to manage their to-do tasks through a command-line interface. The project is implemented using the Click library, which simplifies the creation of command-line interfaces in Python.

Key features of the To-Do List Manager:

Add Task: Users can add new tasks to their to-do list by executing the add command followed by the task description. For example, python project.py add Buy groceries.

View Tasks: Users can view all their tasks by executing the view command. It displays a numbered list of tasks on the console.

Complete Task: Users can mark a task as completed by executing the complete command followed by the task index. The task index corresponds to the task's position in the task list displayed during the view command.

Data Persistence: The project uses text files (tasks.txt and test_tasks.txt) to store the tasks. The main tasks are saved in tasks.txt, and the test tasks are saved in test_tasks.txt to ensure data isolation during testing.

Pytest Integration: The project includes test cases using the Pytest framework to validate the functionality of the project's functions. The tests ensure that tasks can be added, viewed, and completed correctly.

Overall, this To-Do List Manager provides a simple and effective way to manage tasks through the command-line interface, making it a useful tool for organizing daily activities and staying on top of to-do lists.