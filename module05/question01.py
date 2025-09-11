""" 11:00
Mastermind Game
secret: 459
level : 3 -> 10
max moves: 10 -> 12 -> 14
player: 123 -> No match
        456 -> -2
        574 -> -1+1
        548 -> +2
        549 -> level=4
secret: 3615
        1234 -> -2
"""
#region create secret
import random
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

#region game state
level = 3
secret = create_secret_number(level)
moves = []
#endregion

def move_to_next_level():
    #TODO: implement the logic
    pass

def game_loop():
    global level, secret, moves
    while True:
        guess = int(input("Enter your guess: "))
        if guess == secret:
            level += 1
            if level > 10:
                print("You win!")
                break
            print(f"Level up! Current level: {level}")
            move_to_next_level()
        else:
            pass
            #TODO: implement the logic

game_loop()