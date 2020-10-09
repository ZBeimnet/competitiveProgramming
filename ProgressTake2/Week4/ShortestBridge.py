"""
0 1 | 1* 1 | 0  1
1 0 | 1  0 | 1 *1
-----
1 1 -
- - -
- - 1
# find the first island (dfs)
# from every element in the first island move one step at a time toward
  the other island tracking the steps (bfs)
# return the steps once you reach the second island
"""
from collections import deque


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        island_one = None

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    island_one = self.dfs(A, (i, j))
                    break

        return self.bfs(A, island_one)

    def dfs(self, A, point):
        island = {point}
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = [point]

        while stack:
            row, col = stack.pop()

            for neighbour in neighbours:
                new_row = row + neighbour[0]
                new_col = col + neighbour[1]
                if 0 <= new_row < len(A) and \
                        0 <= new_col < len(A[0]) and \
                        A[new_row][new_col] == 1 and \
                        (new_row, new_col) not in island:
                    stack.append((new_row, new_col))
                    island.add((new_row, new_col))

        return island

    def bfs(self, A, island_one):
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(point, 0) for point in island_one])
        for x, y in island_one:
            A[x][y] = -1

        while queue:
            point, level = queue.popleft()

            for neighbour in neighbours:
                new_row = point[0] + neighbour[0]
                new_col = point[1] + neighbour[1]
                if 0 <= new_row < len(A) and \
                        0 <= new_col < len(A[0]) and \
                        A[new_row][new_col] != -1:
                    if A[new_row][new_col] == 0:
                        queue.append(((new_row, new_col), level + 1))
                        A[new_row][new_col] = -1
                    else:
                        return level