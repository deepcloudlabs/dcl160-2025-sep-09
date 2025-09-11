from functools import reduce

employees = [
    {"fullname": "jack shephard", "department": "Sales", "salary": 100000, "year": 1978, "fulltime": True},
    {"fullname": "kate austen", "department": "IT", "salary": 200000, "year": 1985, "fulltime": False},
    {"fullname": "ben linus", "department": "Finance", "salary": 150000, "year": 1967, "fulltime": True},
    {"fullname": "james sawyer", "department": "HR", "salary": 70000, "year": 1979, "fulltime": True},
    {"fullname": "kim kwon", "department": "Sales", "salary": 120000, "year": 1986, "fulltime": True},
    {"fullname": "sun kwon", "department": "IT", "salary": 200000, "year": 1984, "fulltime": False},
    {"fullname": "hugo reyes", "department": "IT", "salary": 120000, "year": 1992, "fulltime": True}
]
# imperative programming
total_salary = 0
for employee in employees:  # external loop
    if employee["department"] == "IT":
        salary = employee["salary"]
        total_salary += salary
print(f"Total salary in IT department: {total_salary}")


# declarative programming: SQL, functional programming
# pipeline: function chain -> filter -> map -> reduce
# MapReduce: Hadoop
def is_working_in_it(employee) -> bool:
    return employee["department"] == "IT"


def topla(birikec, deger):
    return birikec + deger


def to_net_salary(employee):
    vergi_dilimi = 0.2
    return employee["salary"] * vergi_dilimi


lambda_is_working_in_it = lambda employee: employee["department"] == "IT" and employee["fulltime"]
# lambda expression: anonymous function
to_sum = lambda acc, salary: acc + salary
to_salary = lambda emp: emp["salary"]
if_it_worker = lambda employee: employee["department"] == "IT"
total_salary = reduce(lambda acc, salary: acc + salary,
                      map(to_salary, filter(if_it_worker, employees)))  # internal loop
total_salary = reduce(topla, map(lambda emp: emp["salary"], filter(if_it_worker, employees)))  # internal loop
total_salary = sum(map(to_salary, filter(if_it_worker, employees)))  # internal loop
print(f"Total salary in IT department: {total_salary}")
"""
select sum(salary)
from employees
where department = "IT";
"""
