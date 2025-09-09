x = "\u20ba" # unicode -> char stream
print(x)
print(len(x))
x = b"\xf0\x9d\x84\x9e" # unicode -> byte stream -> char -> symbol
print(x)
print(len(x))
y = x.decode("utf-8")
print(y)
print(len(y))
