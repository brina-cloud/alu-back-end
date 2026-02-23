#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""

import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee info
    user_resp = requests.get(f"{base_url}/users/{employee_id}")
    if user_resp.status_code != 200:
        sys.exit(1)

    user = user_resp.json()
    EMPLOYEE_NAME = user.get("name")

    # Fetch todos
    todos_resp = requests.get(f"\
    {base_url}/todos", params={"userId": employee_id})

    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()

    TOTAL_NUMBER_OF_TASKS = len(todos)
    NUMBER_OF_DONE_TASKS = [t for t in todos if t.get("completed") is True]
    NUMBER_OF_DONE_TASKS = len(NUMBER_OF_DONE_TASKS)

    # Output (EXACT format)
    print(
        f"Employee {EMPLOYEE_NAME} is done "
        f"with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )

    for task in NUMBER_OF_DONE_TASKS:
        print(f"\t {task.get('TASK_TITLE')}")


if __name__ == "__main__":
    main()
