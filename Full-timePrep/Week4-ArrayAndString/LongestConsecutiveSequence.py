from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        
        for num in nums:
            if num - 1 not in nums_set:
                length = 0
                curr_num = num
                while curr_num in nums_set:
                    length += 1
                    curr_num += 1
                max_length = max(max_length, length)
        
        return max_length