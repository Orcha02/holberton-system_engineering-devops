#!/usr/bin/python3
"""Given employee ID, returns information about his/her TODO list progress"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    url = 'https://jsonplaceholder.typicode.com/'
    user = "{}users/{}".format(url, user_id)
    user_name_dict = requests.get(user).json()
    user_name = user_name_dict.get("username")

    todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                        params={'userId': user_id})
    todo = todo.json()
    total_todo = len(todo)

    todo_done = [task for task in todo if task['completed'] is True]
    total_todo_done = len(todo_done)

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump({user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name
                } for task in todo]}, json_file)