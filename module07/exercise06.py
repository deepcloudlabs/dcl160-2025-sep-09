import json


with open("employees.json", "rt") as file:
    employees = json.load(file)
    for employee in employees:
        print(type(employee[2])) # salary
        print(employee)