# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [(root, 0)]
        level_map = {}

        while queue:
            current = queue.pop(0)

            if current[1] in level_map:
                level_map[current[1]].append(current[0].val)
            else:
                level_map[current[1]] = [current[0].val]

            if current[0].left:
                queue.append((current[0].left, current[1] + 1))

            if current[0].right:
                queue.append((current[0].right, current[1] + 1))

        output = []
        for key in level_map.keys():
            output.append(level_map[key][-1])

        return output







