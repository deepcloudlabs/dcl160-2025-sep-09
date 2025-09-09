a = {1, 2, 3, 4 , 5}
b = {1, 5}
c = set() # empty set
print(a.issubset(b)) # False
print(b.issubset(a)) # True
print(c.issubset(a)) # True
