# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        one_count = self.dfs(root)
        return (None, root)[one_count > 0]
    
    def dfs(self, node):
        if not node:
            return 0 # count 1's
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        if left == 0:
            node.left = None
        if right == 0:
            node.right = None
            
        return left + right + (0, 1)[node.val == 1]
