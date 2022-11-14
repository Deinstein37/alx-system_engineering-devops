#!/usr/bin/python3

<<<<<<< HEAD
"""

Use JSONPlaceholder API to get information about employee

"""
=======
""" A module to get info from an api"""
>>>>>>> 30b8e9606ad55da5175b88db77ef3743687e9d60

import requests

import sys



<<<<<<< HEAD
if __name__ == '__main__':



        employee_ID = int(sys.argv[1])

            user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(

                            employee_ID)

                response = requests.get(user_url)

                    res_json = response.json()

                        name = res_json.get('name')

                            todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(

                                            employee_ID)

                                todo_json = requests.get(todo_url).json()

                                    total_tasks = 0

                                        num_completed_tasks = 0

                                            completed_tasks = []



                                                for task in todo_json:

                                                            total_tasks += 1

                                                                    if task.get('completed') is True:

                                                                                    completed_tasks.append(task.get('title'))

                                                                                                num_completed_tasks += 1



                                                                                                    print("Employee {} is done with tasks({}/{}):".format(name,

                                                                                                                  num_completed_tasks, total_tasks))

                                                                                                        for item in completed_tasks:

                                                                                                                    print("\t {}".format(item))
=======
todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos"

user_url = "https://jsonplaceholder.typicode.com/users/{}"



if __name__ == "__main__":

        complete = 0

            task_list = []

                response_task = requests.get(todos_url.format(sys.argv[1]))

                    total = len(response_task.json())

                        response_user = requests.get(user_url.format(sys.argv[1]))

                            username = response_user.json().get("name", None)

                                for i in response_task.json():

                                            if i.get("completed", False):

                                                            complete += 1

                                                                        task_list.append(i.get("title", None))

                                                                            print("Employee {} is done with tasks({:d}/{:d}):".format(

                                                                                            username, complete, total))

                                                                                for i in task_list:

                                                                                            print("\t {}".format(i))
>>>>>>> 30b8e9606ad55da5175b88db77ef3743687e9d60
