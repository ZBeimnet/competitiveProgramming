"""
X X X X -> x=0
X X X X
X X X X
X O X X -> x=len(grid)-1
|     |
y=0  y=len(grid[0])-1
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []

        for row in [0, len(board) - 1]:
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    self.dfs(board, (row, col))

        for col in [0, len(board[0]) - 1]:
            for row in range(len(board)):
                if board[row][col] == "O":
                    self.dfs(board, (row, col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "1":
                    board[i][j] = "O"

        return

    def dfs(self, board, point):
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = [(point[0], point[1])]

        while stack:
            x, y = stack.pop()
            board[x][y] = "1"

            for neighbour in neighbours:
                new_x = x + neighbour[0]
                new_y = y + neighbour[1]
                if 0 <= new_x < len(board) and \
                        0 <= new_y < len(board[0]) and \
                        board[new_x][new_y] == "O":
                    stack.append((new_x, new_y))

        return