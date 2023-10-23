#!/usr/bin/python3
""" API to fetch employee data and disIplay it."""
import json
import requests
from sys import argv


def write_to_json(list_dictionaries):
    """ Data is taken as dict and converted to json."""
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)


def save_to_file(LO_dict, name):
    """Saves the data to a json file."""
    with open(name + ".json", "w") as f:
        f.write(write_to_json(LO_dict))


if __name__ == "__main__":
    _id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, _id)
    tasks_url = "{}todos?userId={}".format(base_url, _id)

    response = requests.get(user_url)
    user_info = response.json()
    user_name = user_info.get("username")

    response = requests.get(tasks_url)
    tasks = response.json()

    _data = []
    for task in tasks:
        task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name
                }
        _data.append(task_info)

    save_to_file({_id: _data}, _id)
