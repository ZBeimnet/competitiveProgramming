from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        neighbours = [-1, 0, 1]
        
        for i in range(len(matrix) - 2, -1, -1):
            for j in range(len(matrix[0])):
                min_below = float("inf")
                for c in neighbours:
                    row, col = i + 1, c + j
                    if 0 <= col < len(matrix[0]):
                        min_below = min(min_below, matrix[row][col])
                matrix[i][j] += min_below
        
        return min(matrix[0])
        