#!/usr/bin/python3
"""This module export data in the JSON format"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    USER_ID = argv[1]
    dict = {}
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(USER_ID)).json()
    USERNAME = r.get("username")
    r = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                     format(USER_ID)).json()
    dict[USER_ID] = [{"task": i.get("title"),
                      "completed": i.get("completed"),
                      "username": USERNAME} for i in r]

    with open(USER_ID + ".json", "w") as file:
        json.dump(dict, file)
