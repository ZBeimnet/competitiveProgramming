from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] > target:
                right = middle + 1
            elif nums[middle] < target:
                left = middle
            else:
                return middle

        return -1