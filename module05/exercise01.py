def is_even(n: int) -> bool:
    return n % 2 == 0


def is_odd(n: int) -> bool:
    return not is_even(n)


def is_odd2(n: int) -> bool:
    return n % 2 == 1

print(is_odd(10))
print(is_odd(15))

