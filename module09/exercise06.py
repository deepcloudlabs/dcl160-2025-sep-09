import re
pattern = r"[^aieuo]+"
with open("resources/dictionary-eng.txt", mode="rt") as dictionary:
    for word in dictionary:
        if re.fullmatch(pattern, word.strip()):
            print(word.strip())