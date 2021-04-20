class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        return self.dfs(nums, target, cache)
    
    def dfs(self, nums, target, cache):
        if target in cache:
            return cache[target]
        if target == 0:
            return 1
        if target < 0:
            return 0
        
        no_combinations = 0
        for num in nums:
            no_combinations += self.dfs(nums, target - num, cache)
        
        cache[target] = no_combinations
        return no_combinations
