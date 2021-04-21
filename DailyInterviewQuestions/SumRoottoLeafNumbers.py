# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        stack = [(root, [str(root.val)])]
        total_sum = 0
        
        while stack:
            node, path = stack.pop()
            
            if not node.left and not node.right:
                total_sum += int("".join(path))
            
            if node.left:
                stack.append((node.left, path + [str(node.left.val)]))
            if node.right:
                stack.append((node.right, path + [str(node.right.val)]))
        
        return total_sum
