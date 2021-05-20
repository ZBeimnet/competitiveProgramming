class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # find transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse each row
        for row in range(len(matrix)):
            start = 0
            end = len(matrix[0]) - 1
            while start < end:
                matrix[row][start], matrix[row][end] = matrix[row][end], matrix[row][start]
                start += 1
                end -= 1
