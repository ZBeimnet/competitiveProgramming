# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        current = root
        result_list = []

        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result_list.append(current.val)
                current = current.right
            else:
                break

        new_root = current = TreeNode(result_list[0])
        for i in range(1, len(result_list)):
            new_node = TreeNode(result_list[i])
            current.right = new_node
            current = current.right

        return new_root

    # def in_order_traversal(self, root, traversal):
    # # left-subtree -> root -> right-subtree
    #     if root:
    #         traversal = self.in_order_traversal(root.left, traversal)
    #         traversal += str(root.val) + "-"
    #         traversal = self.in_order_traversal(root.right, traversal)