# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque([(root, 1)]) # states -> (node, horizontal_index)
        max_width = 0
        
        while queue:
            size = len(queue)
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            for _ in range(size):
                node, horizontal_index = queue.popleft()
                nodes_before = 2 * (horizontal_index - 1)
                if node.left:
                    queue.append((node.left, nodes_before + 1))
                if node.right:
                    queue.append((node.right, nodes_before + 2))
        
        return max_width