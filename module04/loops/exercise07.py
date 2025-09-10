numbers = list(range(1, 20))
evens = [number for number in numbers if number % 2 == 0]
odds = [number for number in numbers if number % 2 == 1]
print(f"Evens: {evens}")
print(f"Odds: {odds}")