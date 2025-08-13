import sys
from typing import Any, Dict, List, Optional


def main() -> None:
    """Main part of the program"""
    tasks: List[Dict[str, Any]] = []
    task_id: int = 1
    print("Welcome to To-Do Application:")

    while True:
        print()
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        action_task = get_positive_int("\nWhat do you want to do? ")

        if action_task == 1:
            task_id = add_tasks(tasks, task_id)
        elif action_task == 2:
            view_tasks(tasks)
        elif action_task == 3:
            update_tasks(tasks)
        elif action_task == 4:
            delete_tasks(tasks)
        else:
            print("Invalid operation")

        if input("\nDo you want to exit the program? ").lower() == "y":
            sys.exit("\nExiting program...")


def add_tasks(tasks: List[Dict[str, Any]], task_id: int) -> int:
    """
    Add tasks in the todo list

    Args:
        tasks (list): All of the tasks
        task_id (int): Id of the task

    Returns:
        int: Updated task id
    """
    while True:
        print()
        title: str = input("Title: ").strip()
        priority: str = input("Priority: ").strip().lower()
        if priority in ["low", "medium", "high"]:
            tasks.append({"id": task_id, "title": title, "priority": priority})
            task_id += 1
        else:
            print("\nInvalid priority")

        if input("\nDo you want to add more tasks? ").lower() == "n":
            break
    return task_id


def view_tasks(tasks: List[Dict[str, Any]]) -> None:
    """
    List all of the tasks in the format: ID | Task | Priority

    Args:
        tasks (List): List of all of the tasks
    """
    if len(tasks) > 0:
        print("\nID | Task | Priority")
        for task in tasks:
            print(f"{task["id"]} | {task["title"]} | {task["priority"]}")
    else:
        print("\nThere is nothing in the database")


def delete_tasks(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Delete the task from the todo list provided by the user

    Args:
        tasks (list): List of all the tasks

    Returns:
        list: List of all of the deleted tasks
    """
    while True:
        delete_task_id: int = get_positive_int("\nWhich task do you want to delete: ")
        deleted_tasks: List[Dict[str, Any]] = []
        task = get_task(tasks, delete_task_id)

        if task:
            print("\nDeleting task...")
            deleted_tasks.append(tasks.pop(tasks.index(task)))
            print("\nDeleted successfully...")
        else:
            print("There is no such task in the database to delete")

        if input("\nDo you want to delete more tasks? ").lower() == "n":
            return deleted_tasks


def update_tasks(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Update the tasks in the todo list provided by the user

    Args:
        tasks (list): List of all the tasks

    Returns:
        list: list of updated tasks
    """
    while True:
        update_task_id: int = get_positive_int("\nWhich task do you want to update? ")
        updated_tasks: List[Dict[str, Any]] = []
        task = get_task(tasks, update_task_id)

        if task:
            print("\nUpdating Task...")
            task["title"] = input("\nTitle: ")
            priority = input("Priority: ").lower()
            if priority in ["high", "medium", "low"]:
                task["priority"] = priority
                updated_tasks.append(task)
                print("\nUpdated successfully...")
        else:
            print("\nThere is no such task in database")

        if input("\nDo you want to update more tasks? ").lower() == "n":
            return updated_tasks


def get_task(tasks: List[Dict[str, Any]], task_id: int) -> Optional[Dict[str, Any]]:
    """
    Get the task dict of specified task_id

    Args:
        tasks (list): List of all of the tasks
        task_id (int): id of the task dict you want

    Returns:
        Dict: Specified task id dict
    """
    if len(tasks) < 1:
        return None

    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def get_positive_int(prompt: str) -> int:
    """
    Getting positive int from the user

    Args:
        prompt (str): Prompt for the user

    Returns:
        int: Positive int provided by the user
    """
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
