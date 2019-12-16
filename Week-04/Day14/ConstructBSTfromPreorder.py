class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def bst_from_pre_order(pre_order):
    pre_order_traversal = pre_order
    length = len(pre_order_traversal)
    left_sub_tree = []
    right_sub_tree = []
    current_root = pre_order_traversal[0]
    root_node = TreeNode(current_root)

    # append values to left and right sub-tree comparing them with current-root
    for i in range(1, length):
        if i < current_root:
            left_sub_tree.append(i)
        else:
            right_sub_tree.append(i)

    # do the same for the left and right sub-trees recursively
    if len(left_sub_tree) > 0:
        root_node.left = bst_from_pre_order(left_sub_tree)
    if len(right_sub_tree) > 0:
        root_node.right = bst_from_pre_order(right_sub_tree)

    return root_node
