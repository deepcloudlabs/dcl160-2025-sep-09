my_dears = ["Werner", "Alex", "Anne-Flore", "Irene", "Alex"]

# write the relevant Python code to sort the content in reverse-alphabetical order without creating another data structure
print(my_dears)
my_dears.sort(reverse=True)
print(my_dears)

# write the relevant Python code to look for ‘Alex’ value index
index_of_werner = my_dears.index("Alex")
print(index_of_werner) # 3
index_of_werner = my_dears.index("Alex", index_of_werner + 1)
print(index_of_werner) # 4

# Define a strategy and write the Python code to cast my_dears list into a new data structure named unique_dears that only consists of unique values
# list -> list/unique
unique_dears =  list(sorted(set(my_dears),reverse=True)) # list -> set -> sorted -> list
print(unique_dears)

# write the relevant Python code in order to get the following result from the data structure unique_dears :
# [(0, 'Anne-Flore'), (1, 'Werner'), (2, 'Irene'), (3, 'Alex')]
print(list(enumerate(unique_dears)))