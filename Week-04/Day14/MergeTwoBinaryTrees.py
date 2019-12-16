class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def merge_trees(tree1, tree2):

    if not tree1 and not tree2:
        return None
    else:
        if tree1 and tree2:
            tree3 = TreeNode(tree1.val + tree2.val)
        elif tree1 and not tree2:
            tree3 = tree1
        else:
            tree3 = tree2
        tree3.left = merge_trees(tree1.left, tree2.left)
        tree3.right = merge_trees(tree1.right, tree2.right)

        return tree3
