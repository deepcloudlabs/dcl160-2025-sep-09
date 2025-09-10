numbers = list(range(1, 20))
evens = []
odds = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
print(f"Evens: {evens}")
print(f"Odds: {odds}")