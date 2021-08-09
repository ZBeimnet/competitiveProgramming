class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: 
            return 0
        return self.dfs(n, 1, 1, {})
    
    def dfs(self, n, curr_len, copied, cache):
        state = (curr_len, copied)
        if state in cache:
            return cache[state]
        if n == curr_len:
            return 1
        if curr_len > n:
            return float("inf")
        
        paste = 1 + self.dfs(n, curr_len + copied, copied, cache)
        paste_copy = 2 + self.dfs(n, curr_len + copied, curr_len + copied, cache)
        ans = min(paste_copy, paste)
        
        cache[state] = ans
        return ans
        