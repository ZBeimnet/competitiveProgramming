# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        tree_values = self.get_tree_values(root)
        return self.build_balanced_bst(tree_values, 0, len(tree_values) - 1)
    
    
    def build_balanced_bst(self, tree_values, start, end):
        if start > end:
            return None
        
        mid = start + ((end - start) // 2)
        root = TreeNode(tree_values[mid])
        root.left = self.build_balanced_bst(tree_values, start, mid - 1)
        root.right = self.build_balanced_bst(tree_values, mid + 1, end)
        
        return root
    
    
    def get_tree_values(self, root):
        tree_values = []
        stack = []
        current_node = root
        
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                tree_values.append(current_node.val)
                current_node = current_node.right
                
        return tree_values