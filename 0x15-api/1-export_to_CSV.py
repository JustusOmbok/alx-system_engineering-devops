#!/usr/bin/python3
""" API to fetch employee data and disIplay it."""
from csv import DictWriter, QUOTE_ALL
import requests
from sys import argv


def write_to_csv(_data, _id):
    """ Data is taken as dict and id to rep name."""
    with open("{}.csv".format(_id), "w") as file:
        headers = ["USER_ID", "USERNAME",
                   "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        csv_writer = DictWriter(file, fieldnames=headers, quoting=QUOTE_ALL)
        csv_writer.writerows(_data)


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
        users_info = {
                "USER_ID": _id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
                }
        _data.append(users_info)

    write_to_csv(_data, _id)
