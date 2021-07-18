# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque, defaultdict
from typing import List
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        column_nodes = defaultdict(list)
        queue = deque([(root, 0)]) # states -> (node, vertical_level)
        result = []
        
        while queue:
            size = len(queue)
            mini_column_nodes = defaultdict(list)
            
            for _ in range(size):
                node, vertical_level = queue.popleft()
                mini_column_nodes[vertical_level].append(node.val)
                if node.left:
                    queue.append((node.left, vertical_level - 1))
                if node.right:
                    queue.append((node.right, vertical_level + 1))
            
            for key, value in mini_column_nodes.items():
                column_nodes[key].extend(sorted(value))
        
        for key in sorted(column_nodes.keys()):
            result.append(column_nodes[key])
        
        return result
        
