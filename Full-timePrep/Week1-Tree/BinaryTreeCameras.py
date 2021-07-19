### - Trying every possible way that we can plant a camera and choosing the minimum. 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        return self.dfs(root, True, False, {})
    
    def dfs(self, node, p_monitored, p_has_camera, cache):
        state = (node, p_monitored, p_has_camera)
        if state in cache:
            return cache[state]
        if not node:
            return 0
        if not node.left and not node.right:
            return (1, 0)[p_has_camera]
        
        # option - 1
        left1 = self.dfs(node.left, True, True, cache)
        right1 = self.dfs(node.right, True, True, cache)
        min_camera = left1 + right1 + 1
        
        if p_monitored and p_has_camera:
            # option - 2
            left2 = self.dfs(node.left, True, False, cache)
            right2 = self.dfs(node.right, True, False, cache)
            min_camera = min(min_camera, left2 + right2)
        elif p_monitored and not p_has_camera:
            left2 = right2 = left3 = right3 = float("inf")
            # option - 2
            if node.left:
                left2 = self.dfs(node.left, False, False, cache)
                right2 = self.dfs(node.right, True, False, cache)
            # option - 3
            if node.right:
                left3 = self.dfs(node.left, True, False, cache)
                right3 = self.dfs(node.right, False, False, cache)
            min_camera = min(min_camera, left2 + right2, left3 + right3)
        
        cache[state] = min_camera
        return min_camera