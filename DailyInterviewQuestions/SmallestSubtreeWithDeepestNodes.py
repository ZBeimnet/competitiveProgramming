# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        no_deepest_nodes, depth = self.bfs(root)
        return self.dfs(root, 1, no_deepest_nodes, depth)[1]
    
    def bfs(self, root):
        queue = deque([root])
        level_count = 0
        level = 0
        
        while queue:
            size = len(queue)
            count = 0
            for _ in range(size):
                count += 1
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_count = count
            level += 1
        
        return (level_count, level)
    
    def dfs(self, node, curr_depth, total_deepest, depth):
        if not node:
            return (0, None)
        if not node.left and not node.right and curr_depth == depth and total_deepest == 1:
            return (1, node)
        if not node.left and not node.right and curr_depth == depth:
            return (1, None)
        
        left = self.dfs(node.left, curr_depth + 1, total_deepest, depth)
        right = self.dfs(node.right, curr_depth + 1, total_deepest, depth)
        
        if not left[1] and not right[1]:
            if left[0] + right[0] == total_deepest:
                return (left[0] + right[0], node)
            else:
                return (left[0] + right[0], None)
        elif not left[1]:
            return (total_deepest, right[1])
        else:
            return (total_deepest, left[1])
        
