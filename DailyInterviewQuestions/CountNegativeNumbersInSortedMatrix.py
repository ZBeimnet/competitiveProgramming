class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        current_row = 0
        current_col = col = len(grid[0]) - 1
        negatives = 0

        while current_row <= len(grid) - 1 and current_col >= 0:
            if current_col == 0:
                if grid[current_row][current_col] < 0:
                    negatives += (col - current_col) + 1
                else:
                    negatives += (col - current_col)
                current_row += 1
            elif grid[current_row][current_col] < 0:
                current_col -= 1
            else:
                current_row += 1
                negatives += (col - current_col)

        return negatives
