from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        r, c = 0, 0
        visited = set()
        result = []
        
        while self.is_valid(r, c, matrix, visited):
            result.append(matrix[r][c])
            visited.add((r, c))
            r_mov, c_mov = dirs[dir_idx % 4]
            new_r, new_c = r + r_mov, c + c_mov
            if self.is_valid(new_r, new_c, matrix, visited):
                r, c = new_r, new_c
            else:
                dir_idx += 1
                r_mov, c_mov = dirs[dir_idx % 4]
                r, c = r + r_mov, c + c_mov
        
        return result
    
    def is_valid(self, r, c, matrix, visited):
        if 0 <= r < len(matrix) and \
            0 <= c < len(matrix[0]) and \
             (r, c) not in visited:
            return True
        return False
        
        