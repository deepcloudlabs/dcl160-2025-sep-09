from functools import reduce

numbers = range(1, 100)


# even -> cubed -> sum
def is_even(n):
    print(f"is_even called with {n}")
    return n % 2 == 0


def to_cubed(n):
    print(f"to_cubed called with {n}")
    return n ** 3

def to_sum(acc, n):
    print(f"to_sum called with {acc}, {n}")
    return acc + n

print("Application is just started.")

# lazy evaluation
result = reduce(to_sum,map(to_cubed, filter(is_even, numbers)))

print("Application is completed.")
