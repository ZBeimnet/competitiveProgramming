class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        value_node_map = {}
        
        for i in range(1, len(edges) + 1):
            self.make_set(i, value_node_map)
    
        for u, v in edges:
            node_u = value_node_map[u]
            node_v = value_node_map[v]
            if self.find_set(node_u) == self.find_set(node_v):
                return [u, v]
            self.union(node_u, node_v)
    
    def make_set(self, val, value_node_map):
        node = Node(val)
        value_node_map[val] = node
    
    def find_set(self, node):
        if node.parent == node:
            return node
        root = self.find_set(node.parent)
        # path-compression
        node.parent = root
        return root
    
    def union(self, node1, node2):
        set1_root = self.find_set(node1)
        set2_root = self.find_set(node2)
        # union by rank
        if set1_root.rank > set2_root.rank:
            set2_root.parent = set1_root
        else:
            set1_root.parent = set2_root
            if set1_root.rank == set2_root.rank:
                set2_root.rank += 1
        
