from typing import Any, Generator

employees = [
    {"fullname": "jack shephard", "department": "Sales", "salary": 100000, "year": 1978, "fulltime": True},
    {"fullname": "kate austen", "department": "IT", "salary": 200000, "year": 1985, "fulltime": False},
    {"fullname": "ben linus", "department": "Finance", "salary": 150000, "year": 1967, "fulltime": True},
    {"fullname": "james sawyer", "department": "HR", "salary": 70000, "year": 1979, "fulltime": True},
    {"fullname": "kim kwon", "department": "Sales", "salary": 120000, "year": 1986, "fulltime": True},
    {"fullname": "sun kwon", "department": "IT", "salary": 200000, "year": 1984, "fulltime": False},
    {"fullname": "hugo reyes", "department": "IT", "salary": 120000, "year": 1992, "fulltime": True}
]


# generator function
def get_employees_by_department(department: str, employees_list: list[dict]) -> Generator[dict, Any, None]:
    print("get_employees_by_department is started!")
    for emp in employees_list:
        print(f"[for in get_employees_by_department] {emp}")
        if emp["department"] == department:
            yield emp


result = get_employees_by_department("IT", employees)
print(f"first it employee: {next(result)}")
print(f"second it employee: {next(result)}")
