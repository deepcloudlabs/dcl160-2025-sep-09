# positional parameters
def fun(*args):
    print(f"positional arguments: {args}")
    print(f"length of positional arguments: {len(args)}")
    if len(args) == 0:
        print("no positional arguments")
    return sum(args)


def gun(*args):
    return (min(args), max(args))


print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55
print(fun(1, 2, 3, 4, 5))  # 15
print(gun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # (1,10)
