#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSort function below.
def countSort(arr):
    # initialize our count array
    count = [[] for _ in range(100)]

    # here, we add the strings in their respective index (in count array)
    half = len(arr) // 2
    for i in range(len(arr)):
        if i < half:
            count[int(arr[i][0])].append("-")
        else:
            count[int(arr[i][0])].append(arr[i][1])

    # here, we build the output array
    output = []
    for i in range(len(count)):
        for j in range(len(count[i])):
            output.append(count[i][j])

    print(" ".join(output))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
