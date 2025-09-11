employees = [
    {"fullname": "jack shephard", "department": "Sales", "salary": 100000, "year": 1978, "fulltime": True},
    {"fullname": "kate austen", "department": "IT", "salary": 200000, "year": 1985, "fulltime": False},
    {"fullname": "ben linus", "department": "Finance", "salary": 150000, "year": 1967, "fulltime": True},
    {"fullname": "james sawyer", "department": "HR", "salary": 70000, "year": 1979, "fulltime": True},
    {"fullname": "kim kwon", "department": "Sales", "salary": 120000, "year": 1986, "fulltime": True},
    {"fullname": "sun kwon", "department": "IT", "salary": 200000, "year": 1984, "fulltime": False},
    {"fullname": "hugo reyes", "department": "IT", "salary": 120000, "year": 1992, "fulltime": True}
]


def get_employees_by_department(department: str, employees: list[dict]) -> list[dict]:
    department_employees = []
    for emp in employees:
        print(f"[for in get_employees_by_department] {emp}")
        if emp["department"] == department:
            department_employees.append(emp)
    return department_employees


for emp in get_employees_by_department("IT", employees):
    print(f"[for in main] {emp}")
