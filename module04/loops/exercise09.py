employees = [
    ("jack shephard", "Sales", 100000, 1978,True),
    ("kate austen", "IT", 200000, 1985,False),
    ("ben linus", "Finance", 150000, 1967,True),
    ("james sawyer", "HR", 70000, 1979,True),
    ("kim kwon", "Sales", 120000, 1986,True),
    ("sun kwon", "IT", 170000, 1984,False),
    ("hugo reyes", "IT", 120000, 1992,True)
]
part_time_employees = [employee for employee in employees if not employee[-1] ]
full_time_employees = [(full_name,full_time) for full_name,dept,salary,birth_year,full_time in employees if full_time ]
it_employees = [employee for employee in employees if employee[1].upper() == "IT"]
print(part_time_employees)
print(full_time_employees)
print(it_employees)