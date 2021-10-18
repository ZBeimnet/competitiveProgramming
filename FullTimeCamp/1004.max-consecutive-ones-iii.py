#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List

"""
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        one_count = 0
        start = end = 0

        while end < len(nums):
            if (nums[end] == 0 and k > 0) or nums[end] == 1:
                if nums[end] == 0:
                    k -= 1
                one_count += 1
                max_len = max(max_len, one_count)
                end += 1
            else:
                if nums[start] == 0:
                    k += 1
                one_count -= 1
                start += 1
        
        return max_len

# @lc code=end

