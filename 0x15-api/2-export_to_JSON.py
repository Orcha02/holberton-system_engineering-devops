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

    my_dict = {}
    my_list = []

    for task in todo:
        employee_task = {}
        employee_task['username'] = user_name
        employee_task['task'] = task.get('title')
        employee_task['completed'] = task.get('completed')
        my_list.append(employee_task)

    my_dict[user_id] = my_list
    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(my_dict, json_file)
