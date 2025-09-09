x = float("inf")
print(type(x))
print(x)
x = float("-inf")
print(type(x))
print(x)
x = float("inf") / float("-inf")
print(type(x))
print(x)
x = x * 0
print(x)
print(x == x)
import math
print(math.isnan(x)) # True
print(math.isinf(x)) # False
print(math.isfinite(x)) # False
x = float("-inf")
print(math.isnan(x)) # False
print(math.isinf(x)) # True
print(math.isfinite(x)) # False
x = 42
print(math.isnan(x)) # False
print(math.isinf(x)) # False
print(math.isfinite(x)) # True
