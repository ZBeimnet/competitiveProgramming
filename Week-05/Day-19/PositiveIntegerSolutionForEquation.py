"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []

        #         for i in range(1, z+1):
        #             for j in range(1, z+1):
        #                 if customfunction.f(i, j) == z:
        #                     result.append([i, j])
        #                     break

        #         return result

        for i in range(1, z + 1):

            left = 1
            right = z
            while left <= right:
                mid = (left + right) // 2

                if customfunction.f(i, mid) > z:
                    right = right - 1
                elif customfunction.f(i, mid) < z:
                    left = left + 1
                else:
                    result.append([i, mid])
                    break

        return result
