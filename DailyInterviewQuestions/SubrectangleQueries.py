class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.queries = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.queries.append((row1, row2, col1, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for i in range(len(self.queries) - 1, -1, -1):
            r1, r2, c1, c2, v = self.queries[i]
            if r1 <= row <= r2 and c1 <= col <= c2:
                return v
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
