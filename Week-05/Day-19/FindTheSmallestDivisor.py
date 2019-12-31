import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = nums[-1]

        while left < right:
            mid = (right + left) // 2

            total = 0
            for i in range(len(nums)):
                total += math.ceil(nums[i] / mid)

            if total > threshold:
                left = mid + 1
            else:
                right = mid

        return left



