"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
#         # lets try recursively
#         if not root:
#             return 0

#         max_level = 0
#         for i in range(len(root.children)):
#             max_level = max(max_level, self.maxDepth(root.children[i]))

#         return max_level + 1

        if not root:
            return 0

        stack = []

        max_level = 1
        stack.append([root, max_level])

        while stack:
            current = stack.pop()
            current_level = current[1]

            if not current[0].children:
                max_level = max(max_level, current_level)
                continue

            for node in current[0].children:
                stack.append([node, current_level+1])

        return max_level

