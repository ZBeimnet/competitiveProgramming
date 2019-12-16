# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, tree1: TreeNode, tree2: TreeNode) -> TreeNode:
        if not tree1 and not tree2:
            return None
        else:
            if tree1 and tree2:
                tree3 = TreeNode(tree1.val + tree2.val)
                tree3.left = self.mergeTrees(tree1.left, tree2.left)
                tree3.right = self.mergeTrees(tree1.right, tree2.right)
            elif tree1 and not tree2:
                tree3 = tree1
            else:
                tree3 = tree2

            return tree3