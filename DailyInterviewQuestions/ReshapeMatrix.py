from typing import List

# Soln 1
class Solution1:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        new_mat = [[0] * c for _ in range(r)]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rank = i * len(mat[0]) + j
                corresponding_row = rank // c
                corresponding_col = rank % c
                new_mat[corresponding_row][corresponding_col] = mat[i][j]
        
        return new_mat

# Soln 2 - Using Generators
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        new_mat = [[0] * c for _ in range(r)]
        old_mat_generator = (mat[i][j] for i in range(len(mat)) for j in range(len(mat[0])))
        
        for i in range(len(new_mat)):
            for j in range(len(new_mat[0])):
                new_mat[i][j] = next(old_mat_generator)
        
        return new_mat
    
    
