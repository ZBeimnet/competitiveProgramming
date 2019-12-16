class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def find_lca(root, p, q):
    while root:
        if root.val < p.val:
            root = root.right
        elif root.val > q.val:
            root = root.left
        else:
            return root


n1 = TreeNode(6)
n2 = TreeNode(2)
n3 = TreeNode(8)
n4 = TreeNode(0)
n5 = TreeNode(4)
n6 = TreeNode(3)
n7 = TreeNode(5)
n8 = TreeNode(7)
n9 = TreeNode(9)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n6
n5.right = n7
n3.left = n8
n3.right = n9

print(find_lca(n1, TreeNode(2), TreeNode(8)).val)