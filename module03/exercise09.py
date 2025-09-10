customer = "11111111110   ,  \n\tjack shephard,   100000\t\n,\t\tTR1,\n\t\n  SALES  :  HR \t,1982"
tokens = []
for token in customer.split(","):
    tokens.append(token.rstrip().lstrip())
departments = tokens[4].split(":")
tokens[4]= []
for department in departments:
    tokens[4].append(department.rstrip().lstrip())
tokens[2] = float(tokens[2])
tokens[-1] = int(tokens[-1])

print(tokens)