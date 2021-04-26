class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        return self.dfs(obstacles, 2, 0, {}) # states -> lane, point
    
    def dfs(self, obstacles, lane, point, cache):
        if (lane, point) in cache:
            return cache[(lane, point)]
        if point == len(obstacles) - 1:
            return 0
        
        min_jumps_after = float("inf")
        if obstacles[point + 1] == lane:
            for i in range(1, 4):
                if i != lane and obstacles[point] != i:
                    jumps_after = self.dfs(obstacles, i, point + 1, cache)
                    min_jumps_after = min(min_jumps_after, jumps_after)
            min_jumps_after += 1 # cause we're making a jump at this point
        else:
            min_jumps_after = self.dfs(obstacles, lane, point + 1, cache)
        
        cache[(lane, point)] = min_jumps_after
        return min_jumps_after
