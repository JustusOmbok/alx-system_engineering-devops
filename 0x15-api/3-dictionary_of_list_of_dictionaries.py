#!/usr/bin/python3
""" API to fetch employee data and disIplay it."""
import json
import requests
from time import sleep
from sys import argv


def write_to_json(list_dictionaries):
    """Takes data as dict and converts to json."""
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)


def save_to_file(LO_dict, name):
    """Takes dates data and writes to a json file."""
    with open(name + ".json", "w") as f:
        f.write(write_to_json(LO_dict))


if __name__ == "main__":
    usr_data = {}

    base_url = "https://jsonplaceholder.typicode.com/"

    url = "{}{}".format(base_url, "users")
    response = requests.get(url)
    users = response.json()
    ids = [x["id"] for x in users]
    for _id in ids:
        sleep(1)
        user_url = "{}users/{}".format(base_url, _id)
        tasks_url = "{}todos?userId={}".format(base_url, _id)

        response = requests.get(user_url)
        use_info = response.json()
        user_name = use_info.get("username")

        res = requests.get(tasks_url)
        tasks = res.json()

        _data = []
        for task in tasks:
            users_info = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user_name
                    }
            _data.append(users_info)

        usr_data[_id] = _data

    save_to_file(usr_data, "todo_all_employees")
