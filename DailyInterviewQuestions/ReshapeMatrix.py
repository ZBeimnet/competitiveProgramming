from typing import List


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
    
    