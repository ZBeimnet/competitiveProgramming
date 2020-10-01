"""
    3     -> 1
   / \           ^
  9  20   -> 2   |
    /  \         |
   15   7 -> 3   |
run bfs on root, state -> (root, level), root_level = 1
[[3], [9, 20], [15, 7]] -> return the reverse
time-complexity -> O(N), where N is no of nodes
space-complexity -> O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodes_in_each_level = []
        queue = deque([(root, 1)])
        current_level = 0

        while queue:
            node, level = queue.popleft()

            if level > current_level:
                nodes_in_each_level.append([node.val])
                current_level += 1
            else:
                nodes_in_each_level[-1].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        nodes_in_each_level.reverse()

        return nodes_in_each_level
