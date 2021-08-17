from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.dfs(nums, 0, {})
    
    def dfs(self, nums, index, cache):
        if index in cache:
            return cache[index]
        if index == len(nums) - 1:
            return 0
        if nums[index] == 0:
            return float("inf")
        
        min_jump_from_index = float("inf")
        for i in range(index + 1, min(index + nums[index] + 1, len(nums))):
            min_jump_from_index = min(min_jump_from_index, self.dfs(nums, i, cache))
        
        cache[index] = min_jump_from_index + 1
        return min_jump_from_index + 1