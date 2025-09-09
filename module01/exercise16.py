x = 42
y = 549
print("x = " + str(x) +" and y = " + str(y))
print(f"x = {x} and y = {y}")
x = x ^ y # shorthand notation: x ^= y
y = x ^ y
x = x ^ y
print(f"x = {x} and y = {y}")
"""
x y x^y
= = ===
0 0  0
0 1  1  
1 0  1
1 1  0
"""
