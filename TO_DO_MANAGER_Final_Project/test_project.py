import os
import pytest
from project import add_task, view_tasks, complete_task, TASKS_FILE


@pytest.fixture
def setup_cleanup_tasks_file():
    with open(TASKS_FILE, "w") as file:
        file.write("")

    yield


def test_add_task(setup_cleanup_tasks_file):
    add_task("Task 1")
    add_task("Task 2")

    tasks = view_tasks()
    assert len(tasks) == 2
    assert tasks[0] == "Task 1"
    assert tasks[1] == "Task 2"


def test_complete_task(setup_cleanup_tasks_file):
    add_task("Task 1")
    add_task("Task 2")

    complete_task(0)

    tasks = view_tasks()
    assert len(tasks) == 1
    assert tasks[0] == "Task 2"
