"""
Leap Year
2000 Leap Year
2004 Leap Year
2008 Leap Year
2100 Not Leap Year
2104 Leap Year
2108 Leap Year
2200 Not Leap Year
2300 Not Leap Year
2400 Leap Year
"""
year = int(input('Enter a year: ').strip())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')