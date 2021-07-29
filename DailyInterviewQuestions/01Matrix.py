from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque([(i, j) for i in range(len(mat)) for j in range(len(mat[0])) if mat[i][j] == 0])
        neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        dist = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                mat[row][col] = dist
                for neighbour in neighbours:
                    new_row = row + neighbour[0]
                    new_col = col + neighbour[1]
                    if 0 <= new_row < len(mat) and \
                        0 <= new_col < len(mat[0]) and \
                         (new_row, new_col) not in visited and \
                          mat[new_row][new_col] != 0:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            dist += 1
        
        return mat
