#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    word_count = {}
    output = [0] * len(queries)

    # counting the words in strings array
    for word in strings:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # checking if queries are in strings and adding their appereance count to the output array
    for i in range(len(queries)):
        if queries[i] in word_count:
            output[i] = word_count[queries[i]]

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
