# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []

        queue = deque([(root, 0)])
        output = []
        current_level = 0
        current_max = root.val

        while queue:
            node, level = queue.popleft()

            if level == current_level:
                current_max = max(current_max, node.val)
            else:
                output.append(current_max)
                current_max = node.val
                current_level += 1

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        output.append(current_max)

        return output

