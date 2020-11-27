class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    if self.dfs((i, j), grid, visited):
                        return True

        return False

    def dfs(self, point, grid, visited):
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        stack = [(None, point)]

        while stack:
            prev, cur_point = stack.pop()

            visited.add(cur_point)

            for neighbour in neighbours:
                x = cur_point[0] + neighbour[0]
                y = cur_point[1] + neighbour[1]
                if 0 <= x < len(grid) and \
                        0 <= y < len(grid[0]) and \
                        grid[cur_point[0]][cur_point[1]] == grid[x][y]:
                    if (x, y) not in visited:
                        stack.append((cur_point, (x, y)))
                    elif prev != (x, y) and (x, y) in visited:
                        return True

        return False
