class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_length = 0
        cache = {}
        
        for i in range(len(nums)):
            max_length = max(max_length, self.dfs(nums, i, cache))
        
        return max_length + 1
    
    def dfs(self, nums, curr_idx, cache):
        if curr_idx in cache:
            return cache[curr_idx]
        
        max_length = 0
        
        for i in range(curr_idx + 1, len(nums)):
            if nums[i] > nums[curr_idx]:
                max_length = max(max_length, 1 + self.dfs(nums, i, cache))
        
        cache[curr_idx] = max_length
        return max_length 
