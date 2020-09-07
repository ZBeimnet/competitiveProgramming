from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        serverPositions = defaultdict(int)
        noOfServers = 0

        # registering server positions
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    row, col = "R" + str(i), "C" + str(j)
                    serverPositions[row] += 1
                    serverPositions[col] += 1

        # counting servers that communicate
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    row, col = "R" + str(i), "C" + str(j)
                    if serverPositions[row] > 1 or serverPositions[col] > 1:
                        noOfServers += 1

        return noOfServers
