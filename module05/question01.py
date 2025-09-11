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
# region create secret
import random


def create_random_digit(min: int, max: int) -> int:
    return random.randint(min, max)


def create_secret_number(level: int) -> int:
    digits = [create_random_digit(1, 9)]
    while (len(digits) < level):
        digit = create_random_digit(0, 9)
        if digit not in digits:
            digits.append(digit)
    # [5, 4, 9] -> 549
    secret = 0
    for digit in digits:
        secret = 10 * secret + digit
    return secret


# endregion

# region game state
game_state = {
    "level": 3,
    "secret": create_secret_number(3),
    "moves": [],
    "max_moves": 10,
}


# endregion

def move_to_next_level(state: dict) -> bool:
    state["level"] += 1
    if state["level"] > 10:
        return False
    state["secret"] = create_secret_number(state["level"])
    state["moves"] = []
    state["max_moves"] += 2
    return True

"""
  12:00
  create_move(584,549) -> (587,"-1+1")
"""
def create_move(guess: int, secret: int) -> tuple[int, str]:
    pass


def game_loop(state=game_state):
    while True:
        guess = int(input("Enter your guess: "))
        if guess == state["secret"]:
            if not move_to_next_level(state):
                print("You win!")
                break
            print(f"Level up! Current level: {state["level"]}")
        else:
            state["moves"].append(create_move(guess, state["secret"]))
            if len(state["moves"]) > state["max_moves"]:
                print("You lose!")
                break
            for move in state["moves"]:
                print(move)


game_loop()
