class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        new_grid = grid
        row = len(new_grid)
        column = len(new_grid[0])

        for i in range(1, column):
            new_grid[0][i] += new_grid[0][i - 1]

        for i in range(1, row):
            new_grid[i][0] += new_grid[i - 1][0]

        for i in range(1, row):
            for j in range(1, column):
                new_grid[i][j] += min(new_grid[i - 1][j], new_grid[i][j - 1])

        return new_grid[row - 1][column - 1]