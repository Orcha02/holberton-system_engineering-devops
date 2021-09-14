#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests


if __name__ == '__main__':
    all_employees = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for user in users:

        user_id = user.get('id')
        username = user.get('username')

        all_todos = []

        todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={'userId': user_id}).json()

        for task in todos:
            todo = {}
            todo['username'] = username
            todo['task'] = task.get('title')
            todo['completed'] = task.get('completed')
            all_todos.append(todo)

        all_employees[user_id] = all_todos

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_employees, f)
