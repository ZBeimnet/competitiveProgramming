# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        stack = [root]
        flipped_nodes = []
        voyage_idx = 0
        
        while stack:
            node = stack.pop()
            
            if node.val != voyage[voyage_idx]:
                return [-1]
            if node.left and node.left.val != voyage[voyage_idx + 1]:
                node.left, node.right = node.right, node.left
                flipped_nodes.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            voyage_idx += 1
        
        return flipped_nodes
        