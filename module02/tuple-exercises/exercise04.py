odds = (1, 3, 5, 7, 9)
evens = (2, 4, 6, 8, 10)
numbers = (*odds,*evens) # packing
print(numbers)
numbers = odds + evens
print(numbers)
numbers = (odds,evens)
print(numbers)
