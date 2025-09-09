import math

pi = 4 * math.atan(1)
print(pi)

from mpmath import *

mp.dps = 500_000; mp.pretty = True
pi = mpf(4) * mpf(atan(1))
print(pi)
