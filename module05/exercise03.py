def fun(x: int, y: int, z: int ) -> int:
    return x + y * z

# print(fun(1, 2)) # TypeError: fun() missing 1 required positional argument: 'z'
print(fun(z=3, y=2)) # TypeError: fun() missing 1 required positional argument: 'x'