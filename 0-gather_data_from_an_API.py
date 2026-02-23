#!/usr/bin/python3
"""Gather data from an API and display it in a formatted way."""
import requests
import sys

url = "https://jsonplaceholder.typicode.com"

def get_user_info(user_id):
    """Get user information from the API."""
    r = requests.get(f'{url}/users/{user_id}')
    if r.status_code == 200:
        return r.json()
    else:
        print(f'Error: Unable to fetch user information for user ID {user_id}')
        sys.exit(1)

    user_name = r.json().get('name')



    user_todos = r.get(f'{url}/users/{user_id}/todos', params={'userId': user_id})
    todos = user_todos.json()
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed') == True]
    number_of_completed_tasks = len(completed_tasks)

    print(f'Employee {user_name} is done with tasks({number_of_completed_tasks}/{total_tasks}):')
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
    
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print('Usage: python3 0-gather_data_from_an_API.py <user_id>')
            sys.exit(1)

        try:
            user_id = int(sys.argv[1])
        except ValueError:
            print('Error: user_id must be an integer')
            sys.exit(1)

        get_user_info(user_id)

