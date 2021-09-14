#!/usr/bin/python3
"""Given employee ID, returns information about his/her TODO list progress"""
import csv
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

    with open('{}.csv'.format(user_id), 'w') as csv_file:
        csvWriter = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo:
            csvWriter.writerow([user_id, user_name,
                                str(task.get('completed')),
                                task.get('title')])
