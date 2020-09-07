class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 1:
            return [1] * (rowIndex + 1)

        startRow = [1, 1]
        currentRow = [1, 1, 1]

        for i in range(2, rowIndex + 1):
            for j in range(1, len(currentRow) - 1):
                currentRow[j] = startRow[j - 1] + startRow[j]
            startRow = currentRow
            currentRow = [1] * (i + 2)

        return startRow