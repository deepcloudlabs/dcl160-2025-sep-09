a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a ^ b)  # { 1, 2, 5, 6}
print(b ^ a)  # { 1, 2, 5, 6}
print(a.symmetric_difference(b)) # { 1, 2, 5, 6}
print(b.symmetric_difference(a)) # { 1, 2, 5, 6}
