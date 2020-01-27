class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * (len(self.graph))
        queue = [s]
        visited[s] = True

        while queue:
            current_vertex = queue.pop()
            print(current_vertex, end=" ")

            for i in self.graph[current_vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs(self, s):
        visited = [False] * (len(self.graph))
        stack = [s]

        while stack:
            current_vertex = stack.pop()

            if not visited[current_vertex]:
                print(current_vertex, end=" ")
                visited[current_vertex] = True

            for i in self.graph[current_vertex]:
                if not visited[i]:
                    stack.append(i)
