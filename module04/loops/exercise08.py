numbers = [4, 8, None, 15, None, None, None, 16, 23, None, None, 42]
print(numbers)
values = [number for number in numbers if number is not None]
print(values)
