# Create a list named numbers consisting of integers from 0 to 10 (10 not included).
numbers = list(range(0, 10))
print(numbers)
# Add values of 35 and 48 to numbers in one command using a relevant function
#numbers.append(35)
#numbers.append(48)
numbers.extend([35, 48])
print(numbers)

# Remove the last 4 values in the list by assigning a sliced empty list to numbers list
numbers[-4:] = []
print(numbers)

