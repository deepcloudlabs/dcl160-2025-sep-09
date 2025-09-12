import csv

with open("employees.csv", "rt") as file:
    employees = csv.reader(file)
    for employee in employees:
        print(employee)