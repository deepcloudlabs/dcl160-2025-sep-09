# key-based parameters
def fun(*args, **kwargs):
    print(f"positional: {args}")
    print(f"key-based arguments: {kwargs}")
    print("x" in kwargs)
    print("y" in kwargs)
    print("z" in kwargs)
    for key, value in kwargs.items():
        print(f"{key}={value}")
    for arg in args:
        print(arg)


fun(1, 2, 3, x=4, y=5, z=6)
