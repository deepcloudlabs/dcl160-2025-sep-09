from collections import Counter

s = "binnurkurt"
# expected output: p -> 1, r -> 2, m -> 2, ...
histogram = {}
for letter in s:
    histogram[letter] = histogram.get(letter, 0) + 1
print(histogram)

histogram= dict(Counter(s))
print(histogram)

# list/set/dict comprehension
histogram = { char: s.count(char) for char in set(s)}
print(histogram)