from collections import defaultdict
from typing import List
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = [1] * n
        ans = [0] * n
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        self.dfs_postorder(0, None, graph, count, ans)
        self.dfs_preorder(0, None, graph, count, ans)
        
        return ans
    
    
    def dfs_postorder(self, node, parent, graph, count, ans):
        for child in graph[node]:
            if child != parent:
                self.dfs_postorder(child, node, graph, count, ans)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]
    
    
    def dfs_preorder(self, node, parent, graph, count, ans):
        for child in graph[node]:
            if child != parent:
                ans[child] = ans[node] - count[child] + (len(graph) - count[child])
                self.dfs_preorder(child, node, graph, count, ans)