from functools import reduce

employees = [
    {"fullname": "jack shephard", "department": "Sales", "salary": 100000, "year": 1978, "fulltime": True},
    {"fullname": "kate austen", "department": "IT", "salary": 200000, "year": 1985, "fulltime": False},
    {"fullname": "ben linus", "department": "Finance", "salary": 150000, "year": 1967, "fulltime": True},
    {"fullname": "james sawyer", "department": "IT", "salary": 70000, "year": 1979, "fulltime": True},
    {"fullname": "kim kwon", "department": "Sales", "salary": 120000, "year": 1986, "fulltime": True},
    {"fullname": "sun kwon", "department": "IT", "salary": 200000, "year": 1984, "fulltime": False},
    {"fullname": "hugo reyes", "department": "IT", "salary": 120000, "year": 1992, "fulltime": True}
]

#num_of_it_employees = sum(map(lambda emp: 1,filter(lambda emp: emp["department"] == "IT",employees)))
num_of_it_employees = sum(map(lambda emp: 1 if emp["department"] == "IT" else 0,employees))
#num_of_it_employees = len(list(filter(lambda emp: emp["department"] == "IT",employees)))
print(f"Number of IT employees: {num_of_it_employees}")

# C# -> LINQ
# Java -> Stream API
# Python, JS -> MapReduce 
# C++11 -> lambda expression, STL
# C++20 -> ranges api