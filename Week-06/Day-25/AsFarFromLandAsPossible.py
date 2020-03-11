from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        max_distance = -1

        # run bfs for every zero
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    current_distance = self.bfs((i, j), grid)
                    # if there is no land
                    if current_distance == -1:
                        return max_distance
                    max_distance = max(current_distance, max_distance)

        return max_distance

    def bfs(self, point, grid):
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([point])
        visited = set([point])

        while queue:
            x, y = queue.popleft()
            # if land found (since this is bfs it is the nearest land)
            if grid[x][y]:
                return abs(x - point[0]) + abs(y - point[1])

            for neighbour in neighbours:
                curr_x = x + neighbour[0]
                curr_y = y + neighbour[1]
                if 0 <= curr_y < len(grid) and \
                        0 <= curr_x < len(grid) and \
                        (curr_x, curr_y) not in visited:
                    queue.append((curr_x, curr_y))
                    visited.add((curr_x, curr_y))

        return -1
