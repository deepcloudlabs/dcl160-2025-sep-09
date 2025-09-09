numbers = {4, 8, 15, 16, 23, 42}
print(numbers)
print(len(numbers))
numbers.add(7)
print(numbers)
print(len(numbers))
numbers.add(32)
numbers.add(32)
numbers.add(32)
print(numbers)
print(len(numbers))
#print(numbers[0]) # TypeError: 'set' object is not subscriptable
#print(numbers[-1]) # TypeError: 'set' object is not subscriptable
# hash table: O(1) class: __hash__
print(15 in numbers) # O(1)
print(549 in numbers)
