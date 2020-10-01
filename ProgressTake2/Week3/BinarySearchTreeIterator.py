# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.elements = []
        self.inorderTraversal(root, self.elements)
        self.index = 0

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.elements[self.index - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.elements)
    
    def inorderTraversal(self, root, arr):
        if not root:
            return 
        
        self.inorderTraversal(root.left, arr)
        arr.append(root.val)
        self.inorderTraversal(root.right, arr)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
