from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        return self.dfs(graph, visited, 0, hasApple, 0)

    def dfs(self, graph, visited, node, hasApple, cost):
        if node in visited:
            return 0

        visited.add(node)

        children_cost = 0

        for child in graph[node]:
            children_cost += self.dfs(graph, visited, child, hasApple, 2)

        if not children_cost and not hasApple[node]:
            return 0

        return cost + children_cost


