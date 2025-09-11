from functools import reduce

numbers = [[1,2,3],[4,5],[6,7,8,9]]
genres = [["Drama","Comedy","War"],["Drama","Comedy"],["Romance","Drama","Comedy","War"]]
# [1,2,3,4,5,6,7,8,9]

def flat_map(iterable):
    return reduce(lambda acc,value: acc + value, iterable, [])

print(flat_map(numbers))
print(flat_map(genres))