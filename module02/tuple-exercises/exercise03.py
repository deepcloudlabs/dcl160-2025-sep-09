# tuple: immutable, str: immutable
jack = ("jack bauer", 100000, "TR1", ["IT", "SALES"], True, 1956)
print(jack[0])
print(jack[-1])
print(jack[5])
print(jack[-2])
print(len(jack))
print(jack[-6])
#error: print(jack[-7]) # IndexError: tuple index out of range
# [index]: -len(jack) <= index < len(jack)

