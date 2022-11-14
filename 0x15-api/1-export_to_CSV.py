#!/usr/bin/python3

<<<<<<< HEAD
"""

Module 0-gather_data_from_an_API

"""


=======
"""Exports to-do list information for a given employee ID to CSV format."""
>>>>>>> 30b8e9606ad55da5175b88db77ef3743687e9d60

import csv

import requests

<<<<<<< HEAD
from sys import argv



if __name__ == '__main__':



        id = argv[1]

            user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(

                            id)

                response = requests.get(user_url)

                    username = response.json().get('username')

                        todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(

                                        id)

                            todo = requests.get(todo_url).json()



                                with open('{}.csv'.format(id), 'w', encoding='UTF8', newline='') as f:

                                            writer = csv.writer(f, quoting=csv.QUOTE_ALL)



                                                    for task in todo:

                                                                    task_status = task.get('completed')

                                                                                task_title = task.get('title')

                                                                                            writer.writerow([id, username, task_status, task_title])
=======
import sys



if __name__ == "__main__":

        user_id = sys.argv[1]

            url = "https://jsonplaceholder.typicode.com/"

                user = requests.get(url + "users/{}".format(user_id)).json()

                    username = user.get("username")

                        todos = requests.get(url + "todos", params={"userId": user_id}).json()



                            with open("{}.csv".format(user_id), "w", newline="") as csvfile:

                                        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

                                                [writer.writerow(

                                                                [user_id, username, t.get("completed"), t.get("title")]

                                                                         ) for t in todos]
>>>>>>> 30b8e9606ad55da5175b88db77ef3743687e9d60
