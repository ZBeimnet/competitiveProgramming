# Problem link - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# https://docs.python.org/3/library/operator.html

import operator

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.find_boundary(nums, target, "LEFT_BOUND") 
        right_idx = self.find_boundary(nums, target, "RIGHT_BOUND")
        
        return [left_idx, right_idx]
    
    def find_boundary(self, nums, target, flag):
        comparator = (operator.gt, operator.ge)[flag == "LEFT_BOUND"]
        left, right = 0, len(nums) - 1
        idx = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                idx = mid
                
            if comparator(nums[mid], target):
                right = mid - 1
            else:
                left = mid + 1
                
        return idx
    
