def fun(x=1, y=2, z=3) -> int:
    return x + y * z


print(fun())
print(fun(1))
print(fun(1, 2))
print(fun(1, 2, 3))
# print(fun(1, 2, 3, 4, 5, 6))  # TypeError: fun() takes from 0 to 3 positional arguments but 6 were given
