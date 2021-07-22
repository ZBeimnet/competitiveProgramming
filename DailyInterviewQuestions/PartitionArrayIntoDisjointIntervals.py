from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        right_min = nums[:]
        for i in range(len(nums) - 2, 0, -1):
            if right_min[i] > right_min[i+1]:
                right_min[i] = right_min[i+1]
        
        left_max = nums[0]
        for i in range(1, len(nums)):
            if left_max <= right_min[i]:
                return i 
            left_max = max(left_max, nums[i])