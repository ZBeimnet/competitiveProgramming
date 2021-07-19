# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        subtrees, duplicates = set(), {}
        self.dfs(root, subtrees, duplicates)
        return list(duplicates.values())
    
    
    def dfs(self, node, subtrees, duplicates):
        if not node:
            return ""
        
        left_st = self.dfs(node.left, subtrees, duplicates)
        right_st = self.dfs(node.right, subtrees, duplicates)
        st_string = f"({node.val}L{left_st}R{right_st})"
        
        if st_string in subtrees and st_string not in duplicates:
            duplicates[st_string] = node
        elif st_string not in subtrees:
            subtrees.add(st_string)
        
        return st_string
            