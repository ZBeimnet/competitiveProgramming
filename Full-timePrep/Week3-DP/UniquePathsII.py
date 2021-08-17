from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.dfs(obstacleGrid, 0, 0, {})
    
    def dfs(self, obstacleGrid, row, col, cache):
        state = (row, col)
        if state in cache:
            return cache[state]
        if row >= len(obstacleGrid) or col >= len(obstacleGrid[0]):
            return 0
        if obstacleGrid[row][col] == 1:
            return 0
        if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
            return 1
        
        down = self.dfs(obstacleGrid, row  + 1, col, cache)
        right = self.dfs(obstacleGrid, row, col + 1, cache)
        ans = down + right
        
        cache[state] = ans
        return ans
    
    
                
                    