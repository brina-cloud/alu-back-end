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
    employee_name = user.get("name")

    # Fetch todos
    todos_resp = requests.get(f"\
    {base_url}/todos", params={"userId": employee_id})

    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()

    total_tasks = len(todos)
    completed_tasks = [t for t in todos if t.get("completed") is True]
    done_tasks = len(completed_tasks)

    # Output (EXACT format)
    print(
        f"Employee {employee_name} is done "
        f"with tasks({done_tasks}/{total_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()
