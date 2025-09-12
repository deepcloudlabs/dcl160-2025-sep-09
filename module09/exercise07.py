import re

result = re.split(r"\s*,\s*", "1, 2,        3,\t\t\t\t\t 4, 5, 6, 7")
print(result)
print("1, 2,        3,\t\t\t\t\t 4, 5, 6, 7".split(", "))