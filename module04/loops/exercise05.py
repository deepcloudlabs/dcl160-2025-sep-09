"""
 A mathematician lives on a street where house numbers are consecutive
 starting from 1. He/She says that the sum of the house numbers less than
 his/her house number is equal to the sum of the house numbers greater
 than his/her house number. Knowing that his house number contains
 3 digits design an algorithm and write a Python script
 to find his house number.
"""
for building_no in range(100, 1000): # 100 ~ 999
    left_sum = 0
    for house_no in range(1, building_no):
        left_sum += house_no
    right_sum = 0
    right_building_no = building_no + 1
    while right_sum < left_sum:
        right_sum += right_building_no
        right_building_no += 1
    if left_sum == right_sum:
        print(f"Mathematician lives at {building_no}, and there are {right_building_no-1} buildings in the street!")
        break