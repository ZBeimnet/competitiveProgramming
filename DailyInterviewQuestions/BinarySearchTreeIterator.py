# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.iterator = self.inorder_gen(root)
        self.next_value = None

    def next(self) -> int:
        if self.next_value != None:
            next_val = self.next_value
            self.next_value = None
            return next_val
        return next(self.iterator)

    def hasNext(self) -> bool:
        try:
            self.next_value = next(self.iterator)
        except StopIteration:
            return False
        return True            
    
    def inorder_gen(self, root):
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.val
                node = node.right

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()