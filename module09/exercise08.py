import re

result = re.search("sam", "SAM WHITE")
print(result.group() if result else "not found")
result = re.search("sam", "SAM WHITE", flags=re.IGNORECASE)
print(result.group() if result else "not found")