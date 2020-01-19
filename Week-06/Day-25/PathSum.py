# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.checkSum(root, sum, 0)

    def checkSum(self, root, summ, current_sum):
        if not root:
            return False

        if not root.left and not root.right:
            return summ == (current_sum + root.val)

        if self.checkSum(root.left, summ, root.val + current_sum):
            return True

        if self.checkSum(root.right, summ, root.val + current_sum):
            return True

        return False

