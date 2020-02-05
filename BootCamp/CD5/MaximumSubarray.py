from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        new_nums = nums

        for i in range(1, len(new_nums)):
            if new_nums[i - 1] > 0:
                new_nums[i] += new_nums[i - 1]

        return max(new_nums)