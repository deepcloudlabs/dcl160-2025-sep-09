x = 42 # variable -> global variable

def fun(): # stateful function
    global x
    x += 1 # local variable -> global variable

print(x) # 42
fun()
fun()
fun()
print(x) # 45