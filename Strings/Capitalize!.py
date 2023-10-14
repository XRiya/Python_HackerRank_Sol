 #!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    s_ar = s.split(" ")
    final_ar = []
    space = " "
    for w in s_ar:
        final_ar.append(w.capitalize())
    return space.join(final_ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
