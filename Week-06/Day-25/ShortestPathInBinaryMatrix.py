from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1

        end_pt = (len(grid) - 1, len(grid[0]) - 1)
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        queue = deque([[(0, 0), 1]])  # our states --> pos, dist
        grid[0][0] = 1  # visiting a node

        while queue:
            curr_pt, dist = queue.popleft()
            # if we've reached end_pt return distance
            if curr_pt == end_pt:
                return dist

            for neighbour in neighbours:
                x = neighbour[0] + curr_pt[0]
                y = neighbour[1] + curr_pt[1]
                if 0 <= x < len(grid) and \
                        0 <= y < len(grid[0]) and \
                            not grid[x][y]:
                    queue.append([(x, y), dist + 1])
                    grid[x][y] = 1

        return -1


