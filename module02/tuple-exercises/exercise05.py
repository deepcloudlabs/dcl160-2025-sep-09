numbers : tuple[int] = (1, 3, 5, 10, 8, 7, 9, 2, 4, 6)
print(numbers)
# numbers.sort() : AttributeError: 'tuple' object has no attribute 'sort'
sorted_numbers : list[int] = sorted(numbers)
print(numbers)
print(type(sorted_numbers))
print(sorted_numbers)