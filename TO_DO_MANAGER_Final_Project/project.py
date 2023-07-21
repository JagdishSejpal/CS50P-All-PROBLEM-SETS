import click

TASKS_FILE = "tasks.txt"


def add_task(task, tasks_file=TASKS_FILE):
    with open(tasks_file, "a") as file:
        file.write(task + "\n")


def view_tasks(tasks_file=TASKS_FILE):
    tasks = []
    with open(tasks_file, "r") as file:
        tasks = [line.strip() for line in file]
    return tasks


def complete_task(task_index, tasks_file=TASKS_FILE):
    tasks = view_tasks(tasks_file)
    if task_index < len(tasks):
        del tasks[task_index]
        with open(tasks_file, "w") as file:
            file.write("\n".join(tasks) + "\n")


@click.command()
@click.argument("task", nargs=-1)
def add(task):
    """Add a task to the to-do list."""
    task_str = " ".join(task)
    add_task(task_str)
    click.echo(f"Added task: {task_str}")


@click.command()
def view():
    """View all tasks in the to-do list."""
    tasks = view_tasks()
    if tasks:
        click.echo("Tasks:")
        for index, task in enumerate(tasks):
            click.echo(f"{index + 1}. {task}")
    else:
        click.echo("No tasks.")


@click.command()
@click.argument("task_index", type=int)
def complete(task_index):
    """Mark a task as completed."""
    complete_task(task_index - 1)
    click.echo(f"Completed task at index {task_index}")


@click.group()
def main():
    """To-Do List Manager"""
    pass


if __name__ == "__main__":
    main.add_command(add)
    main.add_command(view)
    main.add_command(complete)
    main()
