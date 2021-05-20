class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        longest_path = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest_path = max(longest_path, self.dfs(i, j, matrix, cache, neighbours))
        
        return longest_path
    
    def dfs(self, r, c, matrix, cache, neighbours):
        if (r, c) in cache:
            return cache[(r, c)]
        
        longest_from_point = 0
        for neighbour in neighbours:
            new_r = neighbour[0] + r
            new_c = neighbour[1] + c
            if 0 <= new_r < len(matrix) and \
                0 <= new_c < len(matrix[0]) and \
                 matrix[r][c] < matrix[new_r][new_c]:
                longest_from_point = max(longest_from_point, self.dfs(new_r, new_c, matrix, cache, neighbours))
        
        cache[(r, c)] = longest_from_point + 1
        return longest_from_point + 1
