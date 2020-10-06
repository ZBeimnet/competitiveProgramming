#!/bin/python3

import os
import sys
import heapq


#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    heapq.heapify(A)
    no_ops = 0

    while A[0] < k:
        if len(A) < 2:
            return - 1

        sweetness1, sweetness2 = heapq.heappop(A), heapq.heappop(A)
        new_sweetness = (2 * sweetness2) + sweetness1

        heapq.heappush(A, new_sweetness)
        no_ops += 1

    return no_ops


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
