class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def is_same_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif tree1 and tree2:
        current_node = tree1.val == tree2.val
        left = is_same_tree(tree1.left, tree2.left)
        right = is_same_tree(tree1.right, tree2.right)
        return current_node and left and right
    else:
        return False


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(is_same_tree(root1, root2))
