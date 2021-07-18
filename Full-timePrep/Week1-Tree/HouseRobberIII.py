# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.dfs(root, False, {}) # states -> (root, parent_robbed)
    
    
    def dfs(self, node, parent_robbed, cache):
        state = (node, parent_robbed)
        if state in cache:
            return cache[state]
        if not node:
            return 0
        if not node.left and not node.right:
            return (0, node.val)[not parent_robbed]
        
        max_amount = 0
        # option 1
        left1 = self.dfs(node.left, False, cache)
        right1 = self.dfs(node.right, False, cache)
        left2 = right2 = 0
        if not parent_robbed:
            # option 2
            left2 = self.dfs(node.left, True, cache)
            right2 = self.dfs(node.right, True, cache)
            max_amount = left2 + right2 + node.val
        max_amount = max(max_amount, left1 + right1)
        
        cache[state] = max_amount
        return max_amount
