fullname = """jac   k         
s    h    


e   p     
        h   a   rd"""
for c in fullname:
    if not c.isspace(): # \n\t <space>
        print(c, end="")