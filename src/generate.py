"""! @file generate.py
@brief Profiling tool for generating input data files for profiling.
@author Kristian Duzek <xduzekk00>
"""

import random

def generate(filename, n):
    with open(filename, "w") as f:
        for _ in range(n):
            f.write(str(random.randint(0, 100)) + " ")

generate("data1.txt", 10)
generate("data2.txt", 1000)
generate("data3.txt", 1000000)