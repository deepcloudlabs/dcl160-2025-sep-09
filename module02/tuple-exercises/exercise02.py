# tuple: immutable, str: immutable
jack = ("jack bauer", 100000, "TR1", ["IT", "SALES"], True, 1956)
print(jack)
# immutable -> append does not exists in tuple: jack.append("jack@example.com")
# error: jack[0]="jack shephard"
# error: jack[4] = False
# error: jack[0][0] = "J" # due to str is immutable
print(jack)
