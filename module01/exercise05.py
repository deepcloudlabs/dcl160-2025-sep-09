x : float = 5 / 2 # FPU
print(type(x))
print(x)

y: int = 5 // 2 # ALU
print(type(y))
print(y)

z = 5 * 2. # FPU
print(type(z))
print(z)

n = 5 * 2 # ALU
print(type(n))
print(n)

m: int = 5. // 2 # ALU -> Type Conversion
print(type(m))
print(m)