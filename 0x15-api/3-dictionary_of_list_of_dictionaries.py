#!/usr/bin/python3

<<<<<<< HEAD
"""Returns to-do list information for a given employee ID."""
=======
"""Exports to-do list information of all employees to JSON format."""
>>>>>>> 30b8e9606ad55da5175b88db77ef3743687e9d60

import json

import requests



<<<<<<< HEAD


if __name__ == '__main__':

        url = "https://jsonplaceholder.typicode.com"



            users = requests.get("{}/users".format(url)).json()

                todos = requests.get(url + "/todos").json()



                    dict = {}

                        for user in users:

                                    arr = []

                                            user_id = user.get('id')

                                                    for todo in todos:

                                                                    if user.get('id') == todo.get('userId'):

                                                                                        arr.append({'task': todo.get('title'),

                                                                                                                        'completed': todo.get('completed'),

                                                                                                                                                    'username': user.get('username')})

                                                                                                dict[user_id] = arr



                                                                                                    filename = "todo_all_employees.json"

                                                                                                        with open(filename, "w", encoding="utf-8") as json_file:

                                                                                                                    json_text = json.dumps(dict)

                                                                                                                            json_file.write(json_text)
=======
if __name__ == "__main__":

        url = "https://jsonplaceholder.typicode.com/"

            users = requests.get(url + "users").json()



                with open("todo_all_employees.json", "w") as jsonfile:

                            json.dump({

                                            u.get("id"): [{

                                                                "task": t.get("title"),

                                                                                "completed": t.get("completed"),

                                                                                                "username": u.get("username")

                                                                                                            } for t in requests.get(url + "todos",

                                                                                                                                                    params={"userId": u.get("id")}).json()]

                                                                                                                        for u in users}, jsonfile)
>>>>>>> 30b8e9606ad55da5175b88db77ef3743687e9d60
