fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i,fruits[i])

for i,fruit in enumerate(fruits):
    print(i,fruit)

fullname = "jack shephard"
for index,letter in enumerate(fullname):
    print(index,letter)