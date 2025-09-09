def is_even(n : int) -> bool:
    return n % 2 == 0

fun = is_even # function object

print(type(fun))

print(is_even(10))
print(fun(10))