names = ["jack", "kate", "james", "ben", "sun", "kim", "kate", "jack", "james", "sun", "jack"]
print(names)
print(len(names))
print(names.count("jack"))
print(names.count("ben"))
print(names.index("ben"))
index = names.index("jack")
print(index)  # first jack: 0
index = names.index("jack", index + 1)
print(index)  # second jack: 7
print(names.index("jack", index + 1))  # last jack: 10
# print(names.index("donald")) # ValueError: tuple.index(x): x not in tuple
print(names.count("donald") > 0)
print("donald" in names)
print("kate" in names)
