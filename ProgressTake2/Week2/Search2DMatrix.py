import math


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        row, col = len(matrix), len(matrix[0])
        left, right = 1, row * col

        while left <= right:
            mid = (left + right) // 2
            curr_row = math.ceil(mid / col) - 1
            curr_col = mid - (curr_row * col) - 1
            if matrix[curr_row][curr_col] == target:
                return True
            elif matrix[curr_row][curr_col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False