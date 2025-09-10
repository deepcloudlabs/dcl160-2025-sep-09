"""
 A mathematician lives on a street where house numbers are consecutive
 starting from 1. He/She says that the sum of the house numbers less than
 his/her house number is equal to the sum of the house numbers greater
 than his/her house number. Knowing that his house number contains
 3 digits design an algorithm and write a Python script
 to find his house number.
"""


def find_mathematicians_house():
    # Loop through all 3-digit house numbers
    for house_number in range(100, 1000):
        # Calculate sum of houses before the mathematician's house
        sum_before_house = 0
        for previous_house in range(1, house_number):
            sum_before_house += previous_house

        # Calculate sum of houses after the mathematician's house
        sum_after_house = 0
        next_house = house_number + 1
        while sum_after_house < sum_before_house:
            sum_after_house += next_house
            next_house += 1

        # Check if sums are equal
        if sum_after_house == sum_before_house:
            last_house_on_street = next_house - 1
            return house_number, last_house_on_street


mathematician_house, last_house = find_mathematicians_house()
print(f"Mathematician's house number: {mathematician_house}")
print(f"Last house on the street: {last_house}")