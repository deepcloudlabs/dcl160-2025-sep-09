# key-based parameters
def fun(**kwargs):
    print(f"key-based arguments: {kwargs}")
    print("x" in kwargs)
    print("y" in kwargs)
    print("z" in kwargs)
    for key, value in kwargs.items():
        print(f"{key}={value}")

fun(x=1, z=3)