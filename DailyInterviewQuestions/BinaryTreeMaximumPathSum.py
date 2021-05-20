# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.dfs(root)[1]
    
    def dfs(self, node):
        if node == None:
            return (-1001, -1001)
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        path_max = max(left[0] + node.val, right[0] + node.val, node.val)
        global_max = max(left[1], right[1], path_max, left[0] + right[0] + node.val)
        
        return (path_max, global_max)
        
