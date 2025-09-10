text = "Merhaba Dünya!"
vowels="aeıiuüoö"
number_of_vowels = 0
# count the vowels: 5
for letter in text:
    if letter in vowels:
        number_of_vowels += 1
print(number_of_vowels)

# list comprehension
number_of_vowels = sum([1 for letter in text if letter in vowels])

print(number_of_vowels)
