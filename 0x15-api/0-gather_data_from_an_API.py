#!/usr/bin/python3
"""Given employee ID, returns information about his/her TODO list progress"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    user_id = argv[1]

    url = 'https://jsonplaceholder.typicode.com/'
    user = "{}users/{}".format(url, user_id)
    employee_dict = requests.get(user).json()
    employee_name = employee_dict.get("name")

    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': user_id})
    todo = todo.json()
    total_todo = len(todo)

    todo_done = [task for task in todo if task['completed'] is True]
    total_todo_done = len(todo_done)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total_todo_done, total_todo))
    for info_dict in todo_done:
        task_title = info_dict.get("title")
        print("\t " + task_title)
