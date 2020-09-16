# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        #         if not root: return None

        #         if root.val == val:
        #             return root
        #         elif root.val > val:
        #             return self.searchBST(root.left, val)
        #         else:
        #             return self.searchBST(root.right, val)

        if not root: return None

        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node.val == val:
                return curr_node
            elif curr_node.val > val and curr_node.left:
                stack.append(curr_node.left)
            elif curr_node.right:
                stack.append(curr_node.right)

        return None
