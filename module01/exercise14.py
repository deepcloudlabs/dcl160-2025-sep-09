value: str = "42"
number: int = int(value)

message: str = "The value is " + str(number) + "."
print(message)

x = float("nan") # str -> float
x = float("inf") # str -> float
x = float("-inf") # str -> float
