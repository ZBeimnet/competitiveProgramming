# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        tree_nodes = []
        
        self.traverse_preorder(root, tree_nodes)
        
        for i in range(1, len(tree_nodes)):
            tree_nodes[i - 1].left = tree_nodes[i].left = None
            tree_nodes[i - 1].right = tree_nodes[i]
        
    def traverse_preorder(self, node, tree_nodes):
        if node:
            tree_nodes.append(node)
            self.traverse_preorder(node.left, tree_nodes)
            self.traverse_preorder(node.right, tree_nodes)
        
