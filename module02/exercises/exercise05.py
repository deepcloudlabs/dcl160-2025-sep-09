# rotate a list by k-steps
numbers = [1, 2, 3, 4, 5]
print(numbers)
k = 5
rotated_numbers = numbers[-k:] + numbers[:-k]
print(rotated_numbers)

