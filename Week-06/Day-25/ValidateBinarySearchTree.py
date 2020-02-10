# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        tree_values = self.inorder_traversal(root, [])

        # check for validity
        for i in range(len(tree_values) - 1):
            if tree_values[i + 1] <= tree_values[i]:
                return False

        return True

    def inorder_traversal(self, root, traversal):
        if root:
            self.inorder_traversal(root.left, traversal)
            traversal.append(root.val)
            self.inorder_traversal(root.right, traversal)

        return traversal


