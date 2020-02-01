class Graph:
    def __init__(self, col, row, graph):
        self.col = col
        self.row = row
        self.graph = graph

    def is_safe(self, i, j, visited):
        return 0 <= i < self.row and \
               0 <= j < self.col and \
               not visited[i][j] and self.graph[i][j]

    def dfs(self, i, j, visited):
        possible_neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        visited[i][j] = True

        for k in range(8):
            if self.is_safe(i + possible_neighbours[k][0], j + possible_neighbours[k][1], visited):
                self.dfs(i + possible_neighbours[k][0], j + possible_neighbours[k][1], visited)

        # stack = [(i, j)]
        #
        # while stack:
        #     current = stack.pop()
        #     visited[current[0]][current[1]] = True
        #
        #     possible_neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]
        #     for k in range(8):
        #         if self.is_safe(i + possible_neighbours[k][0], j + possible_neighbours[k][1], visited):
        #             stack.append((i + possible_neighbours[k][0], j + possible_neighbours[k][1]))

    def count_islands(self):
        visited = [([False] * self.col) for i in range(self.row)]
        count = 0

        for i in range(self.row):
            for j in range(self.col):
                if not visited[i][j] and self.graph[i][j]:
                    self.dfs(i, j, visited)
                    count += 1

        return count


gr = [[1, 1, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [1, 0, 0, 1, 1],
      [0, 0, 0, 0, 0],
      [1, 0, 1, 0, 1]]

rows = len(gr)
cols = len(gr[0])

g = Graph(rows, cols, gr)

print(g.count_islands())

