#!/usr/bin/python3
import requests
import sys

def get_employee_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        user_res = requests.get("{}/users/{}".format(base_url, employee_id))
        user_res.raise_for_status()
        user_data = user_res.json()
        employee_name = user_data.get("name")
        
        todos_res = requests.get("{}/todos".format(base_url), params={"userId": employee_id})
        todos_res.raise_for_status()
        todos = todos_res.json()
        
        completed_tasks = [task for task in todos if task.get("completed") is True]
        total_tasks = len(todos)
        done_count = len(completed_tasks)
        
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, done_count, total_tasks))
        
        for task in completed_tasks:
            print("\t {}".format(task.get("title")))
            
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            emp_id = int(sys.argv[1])
            get_employee_progress(emp_id)
        except ValueError:
            pass