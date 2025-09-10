numbers = [4, 8, None, 15, None, None, None, 16, 23, None, None, 42]
print(numbers)
while None in numbers:
    numbers.remove(None)
print(numbers)
