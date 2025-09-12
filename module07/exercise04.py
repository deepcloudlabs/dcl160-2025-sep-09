import pickle

with open("employees.pkl", mode="rb") as file:
    employees = pickle.load(file)
    print(type(employees))
    for employee in employees:
        print(type(employee[2]))
        print(employee)
