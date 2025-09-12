import re

text = "kate      austen,         e-posta:      kate@example.com"
pattern = r"([a-zA-Z][a-z]+\s+[a-zA-Z][a-z]+),\s+e-posta:\s+(\w+@\w+\.\w{2,5})"
result = re.search(pattern, text)
print(result.group(1))
print(result.group(2))