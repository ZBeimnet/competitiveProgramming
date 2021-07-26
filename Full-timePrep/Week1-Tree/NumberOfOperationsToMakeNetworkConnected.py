from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        required_edges = 0
        groups = 0
        
        for node1, node2 in connections:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        for node in range(n):
            if node not in visited:
                connected_nodes = self.dfs(node, graph, visited)
                required_edges += connected_nodes - 1
                groups += 1
        
        return (-1, groups - 1)[len(connections) - required_edges >= groups - 1]
    
    def dfs(self, node, graph, visited):
        visited.add(node)
        count = 0
        for neighbour in graph[node]:
            if neighbour not in visited:
                count += self.dfs(neighbour, graph, visited)
        return count + 1