from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        right_max = T[n-1]
        res = [0] * n
        for i in range(n-2, -1, -1):
            t = T[i]
            if right_max <= t:
                right_max = t
            else:
                temp = 1
                while T[i+temp] <= t:
                    temp += res[i+temp]
                res[i] = temp
        return res