# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        stack = [(root, None, None)]
        forest = ([root], [])[root.val in to_delete_set]
        
        while stack:
            node, parent, direction = stack.pop()
            
            if node.val in to_delete_set:
                if parent:
                    if direction == "left":
                        parent.left = None
                    else:
                        parent.right = None
                if node.left and node.left.val not in to_delete_set:
                    forest.append(node.left)
                if node.right and node.right.val not in to_delete_set:
                    forest.append(node.right)
            
            if node.left:
                stack.append((node.left, node, "left"))
            if node.right:
                stack.append((node.right, node, "right"))
        
        return forest
