jack = ("jack bauer", 100000, "TR1", ["IT", "SALES"], True, 1956)
fullname, salary, iban, *rest = jack  # unpacking
print(fullname, salary, iban)
print(type(rest))
print(rest)
