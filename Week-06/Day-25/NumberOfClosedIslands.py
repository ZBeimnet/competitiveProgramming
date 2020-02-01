class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [([False] * col) for i in range(row)]

        # excluding group of 0's on edges
        for i in range(col):
            # if node not visited and if it is a land(0) run bfs on it
            if not visited[0][i] and not grid[0][i]:
                self.dfs(0, i, visited, grid)
            if not visited[row - 1][i] and not grid[row - 1][i]:
                self.dfs(row - 1, i, visited, grid)

        for i in range(row):
            if not visited[i][0] and not grid[i][0]:
                self.dfs(i, 0, visited, grid)
            if not visited[i][col - 1] and not grid[i][col - 1]:
                self.dfs(i, col - 1, visited, grid)

        # count group of 0's inside
        count = 0

        for i in range(row):
            for j in range(col):
                if not visited[i][j] and not grid[i][j]:
                    self.dfs(i, j, visited, grid)
                    count += 1

        return count

    def dfs(self, i, j, visited, grid):
        visited[i][j] = True
        possible_neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for k in range(4):
            # check if a neighbour is part of the grid and is land(0)
            curr_row = i + possible_neighbours[k][0]
            curr_col = j + possible_neighbours[k][1]
            if 0 <= curr_row < len(grid) \
                    and 0 <= curr_col < len(grid[0]) \
                    and not visited[curr_row][curr_col] \
                    and not grid[curr_row][curr_col]:
                self.dfs(curr_row, curr_col, visited, grid)




