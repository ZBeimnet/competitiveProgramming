class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.dfs(d, f, target, {}) % ((10**9) + 7)
    
    def dfs(self, d, f, target, cache):
        state = (d, target)
        if state in cache:
            return cache[state]
        if d == 0 and target == 0:
            return 1
        if d < 0 or target < 0:
            return 0
        
        ways = 0
        for face in range(1, f + 1):
            ways += self.dfs(d - 1, f, target - face, cache)
        
        cache[state] = ways
        return ways