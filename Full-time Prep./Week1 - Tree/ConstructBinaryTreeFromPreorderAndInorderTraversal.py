# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_map = {}
        pre_index = [0]
        
        for i, num in enumerate(inorder):
            inorder_map[num] = i
            
        return self.build(preorder, inorder_map, pre_index, 0, len(preorder) - 1)
    
    
    def build(self, preorder, inorder_map, pre_index, left, right):
        if left > right:
            return None
        
        root = TreeNode(preorder[pre_index[0]])
        index = inorder_map[preorder[pre_index[0]]]
        pre_index[0] += 1
        
        root.left = self.build(preorder, inorder_map, pre_index, left, index - 1)
        root.right = self.build(preorder, inorder_map, pre_index, index + 1, right)
        
        return root