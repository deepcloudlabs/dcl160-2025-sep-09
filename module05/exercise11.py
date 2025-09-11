"""
    def fun(x,y=2,z):
                  ^
SyntaxError: parameter without a default follows parameter with a default
"""
def fun(x,z,y=2):
    return x + y * z

#fun(x=1,z=3)