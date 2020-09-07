class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1] * i for i in range(1, numRows + 1)]

        for i in range(2, len(triangle)):
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        return triangle