#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
from typing import List

"""
[1,1,0,1,1,1]
      **
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                start = i + 1
            max_len = max(max_len, i - start + 1)
        
        return max_len

        


# @lc code=end
