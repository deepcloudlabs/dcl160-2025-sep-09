a = {1, 2, 3, 4, 5}
b = {6, 7, 8}
c = set()  # empty set
print(a.isdisjoint(b))  # True
print(b.isdisjoint(a))  # True
print(c.isdisjoint(a))  # True
