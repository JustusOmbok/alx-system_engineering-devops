#!/usr/bin/python3
""" API to fetch empolee data and display it."""
import requests
from sys import argv


if __name__ == "__main__":
    _id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, _id)
    tasks_url = "{}todos?userId={}".format(base_url, _id)

    response = requests.get(user_url)
    user_info = response.json()
    name = user_info["name"]

    response = requests.get(tasks_url)
    tasks = response.json()

    done_tasks = 0
    total_tasks = 0
    completed_titles = []
    for task in tasks:
        if task["completed"]:
            done_tasks += 1
            completed_titles.append(task["title"])
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, done_tasks, total_tasks))
    for title in completed_titles:
        print("\t{}".format(title))
