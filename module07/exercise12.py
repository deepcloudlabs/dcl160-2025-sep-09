# read_employees.py
import employee_pb2

# Read and parse
employees_msg = employee_pb2.Employees()
with open("employees.bin", "rb") as f:
    employees_msg.ParseFromString(f.read())

# Print
for emp in employees_msg.employees:
    print(f"Name: {emp.name}, Dept: {emp.department}, "
          f"Salary: {emp.salary}, Birth Year: {emp.birth_year}, "
          f"Full-time: {emp.full_time}")