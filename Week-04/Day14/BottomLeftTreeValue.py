class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find_bottom_left_value(self, root: TreeNode) -> int:
        tree_height = self.find_height(root)
        last_level_leafs = self.return_elements_at_level(root, tree_height, [])
        left_most = last_level_leafs[0]

        return left_most

    def find_height(self, root):
        if root is None:
            return 0
        else:
            left_height = self.find_height(root.left)
            right_height = self.find_height(root.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    def return_elements_at_level(self, root, level, data):
        if root is None:
            return
        if level == 1:
            data.append(root.val)
        elif level > 1:
            self.return_elements_at_level(root.left, level - 1, data)
            self.return_elements_at_level(root.right, level - 1, data)

        return data
