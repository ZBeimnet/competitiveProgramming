#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superDigit function below.
def superDigit(n, k):
    p = n * k
    stack = [p]

    while len(stack[-1]) > 1:
        curr = stack.pop()
        total = 0
        for digit in curr:
            total += int(digit)
        stack.append(str(total))

    return stack.pop()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
