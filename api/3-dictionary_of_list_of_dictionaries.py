#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress
from https://jsonplaceholder.typicode.com
"""

import json
import requests
import sys


def main():
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee info
    users_resp = requests.get(f"{base_url}/users")
    if users_resp.status_code != 200:
        sys.exit(1)

    users = users_resp.json()

    # Fetch todos
    todos_resp = requests.get(f"{base_url}/todos")
    todos = todos_resp.json()

    user_map = {}
    for user in users:
        user_map[user.get('id')] = user.get('username')

    all_tasks = {}
    for task in todos:
        user_id = task.get('userId')
        user_id_str = str(user_id)

        if user_id_str not in all_tasks:
            all_tasks[user_id_str] = []

        all_tasks[user_id_str].append({
            "username": user_map[user_id],
            "task": task.get('title'),
            "completed": task.get('completed')
        })

    filename = "todo_all_employees.json"

    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(all_tasks, jsonfile)

if __name__ == "__main__":
    main()