import random

#region create secret
def create_random_digit(min:int, max:int) -> int:
    return random.randint(min, max)

def create_secret_number(level : int) -> int:
    digits = [create_random_digit(1,9)]
    while (len(digits) < level):
        digit = create_random_digit(0,9)
        if digit not in digits:
            digits.append(digit)
    # [5, 4, 9] -> 549
    secret = 0
    for digit in digits:
        secret = 10 * secret + digit
    return secret
#endregion

print(create_secret_number(3))
print(create_secret_number(3))
print(create_secret_number(3))
print(create_secret_number(3))
print(create_secret_number(3))