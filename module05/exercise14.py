def create_move(guess: int, secret: int) -> tuple[int, str]:
    # int -> str
    guess_str = str(guess)
    secret_str = str(secret)
    perfect_match = 0
    partial_match = 0
    for i, digit_of_guess in enumerate(guess_str):
        for j, digit_of_secret in enumerate(secret_str):
            if digit_of_guess == digit_of_secret:
                if i == j:
                    perfect_match += 1
                else:
                    partial_match += 1
    if perfect_match == 0 and partial_match == 0:
        return (guess, "No match")
    message = ""
    if partial_match > 0:
        message = f"-{partial_match}"
    if perfect_match > 0:
        message = f"{message}+{perfect_match}"
    return (guess, message)

print(create_move(584,549)) # (584, "-1+1")
print(create_move(1234,3615)) # (1234, "-2")