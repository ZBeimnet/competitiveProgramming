# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return node
        
        last_left = self.dfs(node.left)
        last_right = self.dfs(node.right)
        
        if last_left and last_right:
            temp = node.right
            node.right = node.left
            last_left.right = temp
        elif last_left:
            node.right = node.left
            last_right = last_left
        
        node.left = None
        return last_right
    
        