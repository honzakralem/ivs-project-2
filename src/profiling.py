"""! @file profiling.py
@brief Profiling tool calculating deviation using the math library
@author Kristian Duzek <xduzekk00>
"""

from mathlib import *
import sys

sum_x = 0
sum_x2 = 0 
avg = 0
N = 0

for line in sys.stdin:
    for num in line.split():
        x = float(num)
        sum_x = add(sum_x, x)
        sum_x2 = add(sum_x2, pow(x,2))
        N += 1

avg = div(sum_x, N)
s = 0
s = sub(sum_x2, mul(N, pow(avg, 2)))
N -= 1
s = div(s, N)
s = sqt(s, 2)

print(s)
