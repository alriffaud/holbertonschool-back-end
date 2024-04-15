#!/usr/bin/python3
"""This module exports data in the JSON format"""

if __name__ == "__main__":
    import requests
    import json

    dict = {}
    r1 = requests.get("https://jsonplaceholder.typicode.com/users").json()
    r2 = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    dict = {j.get("id"): [{"task": i.get("title"),
                           "completed": i.get("completed"),
                           "username": j.get("username")} for i in r2
                          if i.get("userId") == j.get("id")] for j in r1}

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict, file)
