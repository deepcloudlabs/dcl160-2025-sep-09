import re
empty_line = r"^\s*$"
with open("resources/dictionary-tr.txt", mode="rt") as dictionary:
    for word in dictionary:
        if re.fullmatch(empty_line, word.strip()):
            print("Empty line!")