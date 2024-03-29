from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            if right - left >= 2:
                if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid + 1] > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return (left, right)[nums[right] > nums[left]]
        
        return left