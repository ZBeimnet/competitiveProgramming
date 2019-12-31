from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = 1

        while left < right:
            mid = (left + right) // 2

            # counting numbers <= mid in nums
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return right



