from math import floor, ceil

x = int(True) # True -> integer -> 1
print(x)
x = int(False) # True -> integer -> 0
print(x)
#x = int("forty two") # NLP ? ValueError: invalid literal for int() with base 10: 'forty two'
#print(x)
#x = int("3.999") # ValueError: invalid literal for int() with base 10: '3.999'
#print(x)
x = float("3.999")
print(x)
y = int(x)
print(y)
z = floor(x)
print(z)
z = ceil(x)
print(z)
x = -3.7
z = ceil(x)
print(z)
str(True)
str(3.1415)
x = bool(42) # True
print(x)
x = bool(0) # false
print(x)
x = bool("True")
print(x)
x = bool("true")
print(x)
hash_of_empty_string = "".__hash__()
print(hash_of_empty_string)
x = bool("") # False
print(x)


