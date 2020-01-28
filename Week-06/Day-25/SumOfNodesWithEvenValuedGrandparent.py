# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        even_sum = 0

        while stack:
            current = stack.pop()
            val = current[0].val
            right = current[0].right
            left = current[0].left

            if right:
                stack.append([right, val])
                if current[1] % 2 == 0:
                    even_sum += right.val
            if left:
                stack.append([left, val])
                if current[1] % 2 == 0:
                    even_sum += left.val

        return even_sum