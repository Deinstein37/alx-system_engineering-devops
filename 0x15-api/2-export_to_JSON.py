#!/usr/bin/python3

<<<<<<< HEAD
"""

Module 0-gather_data_from_an_API

"""


=======
"""Exports to-do list information for a given employee ID to JSON format."""
>>>>>>> 30b8e9606ad55da5175b88db77ef3743687e9d60

import json

import requests

<<<<<<< HEAD
from sys import argv



if __name__ == '__main__':



        id = argv[1]

            user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(

                        id)).json()

                username = user.get('username')

                    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".

                                                    format(id)).json()

                        json_filename = id + ".json"



                            tasks = []



                                for task in todo:

                                            task_dict = {}

                                                    task_dict["task"] = task.get('title')

                                                            task_dict["completed"] = task.get('completed')

                                                                    task_dict["username"] = username

                                                                            tasks.append(task_dict)



                                                                                dictionary = {}

                                                                                    dictionary[id] = tasks



                                                                                        with open(json_filename, "w") as json_file:

                                                                                                    json.dump(dictionary, json_file)
=======
import sys



if __name__ == "__main__":

        user_id = sys.argv[1]

            url = "https://jsonplaceholder.typicode.com/"

                user = requests.get(url + "users/{}".format(user_id)).json()

                    username = user.get("username")

                        todos = requests.get(url + "todos", params={"userId": user_id}).json()



                            with open("{}.json".format(user_id), "w") as jsonfile:

                                        json.dump({user_id: [{

                                                            "task": t.get("title"),

                                                                            "completed": t.get("completed"),

                                                                                            "username": username

                                                                                                        } for t in todos]}, jsonfile)
>>>>>>> 30b8e9606ad55da5175b88db77ef3743687e9d60
