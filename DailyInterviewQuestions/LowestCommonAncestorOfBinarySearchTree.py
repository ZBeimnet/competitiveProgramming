# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)[2]
    
    def dfs(self, node, p, q):
        if not node:
            return (False, False, None)
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        
        if left[2] != None or right[2] != None:
            return (True, True, (left[2], right[2])[right[2] != None])
        
        ans = [False, False, None]
        ans[0] = left[0] or right[0] or p.val == node.val
        ans[1] = left[1] or right[1] or q.val == node.val
        ans[2] = (None, node)[ans[0] and ans[1]]
        
        return tuple(ans)
    
