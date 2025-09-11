def fun(x: int, y: int, z: int, w: int = 0) -> int:
    return x + y * z - w

print(fun(1, 2,3)) # TypeError: fun() missing 1 required positional argument: 'z'
print(fun(z=3, y=2, x = 4)) # TypeError: fun() missing 1 required positional argument: 'x'