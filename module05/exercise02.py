def fun(x: int, y: int, z: int) -> int:
    return x + y * z

# positional parameters
print(fun(1, 2, 3)) #7
# key-based parameters
print(fun(z=3, x=1, y=2)) #7