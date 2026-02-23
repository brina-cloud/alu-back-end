#!/usr/bin/python3
"""
Script that fetches and displays an employee's TODO list progress
using the JSONPlaceholder REST API.
Usage: python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"


    user_response = requests.get("{}/{}".format(user_url, employee_id))
    if user_response.status_code != 200:
        print("Error: Employee with ID {} not found.".format(employee_id))
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("username")

    todos_response = requests.get("{}".format(todos_url), params={"userId": employee_id}
    )
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks
    ))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))