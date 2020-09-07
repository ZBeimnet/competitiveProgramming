class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)


class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)

    def print_tree(self, traversal_type):
        if traversal_type == "pre_order":
            return self.pre_order_traversal(self.root, "")
        elif traversal_type == "in_order":
            return self.in_order_traversal(self.root, [])
        elif traversal_type == "in_order_iterative":
            return self.iterative_in_order(self.root)
        elif traversal_type == "post_order":
            return self.post_order_traversal(self.root, "")
        else:
            print("Traversal type not supported!")

    def pre_order_traversal(self, root, traversal):
        # root -> left-subtree -> right-subtree
        if root:
            traversal += str(root.value) + "-"
            traversal = self.pre_order_traversal(root.left, traversal)
            traversal = self.pre_order_traversal(root.right, traversal)

        return traversal

    def iterative_pre_order(self, root):
        if not root:
            return

        stack = Stack()
        result_list = []
        stack.push(root)

        while stack.size() > 0:
            current_node = stack.pop()
            result_list.append(current_node.value)

            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)

        return result_list

    def in_order_traversal(self, root, traversal):
        # left-subtree -> root -> right-subtree
        if root:
            self.in_order_traversal(root.left, traversal)
            traversal.append(root.value)
            self.in_order_traversal(root.right, traversal)

        return traversal

    def iterative_in_order(self, root):
        # empty stack to simulate call stack
        stack = Stack()
        current = root
        result_list = []

        while stack or current:
            if current:
                stack.push(current)
                current = current.left
            else:
                current = stack.pop()
                result_list.append(current.value)
                current = current.right

        return result_list

    def post_order_traversal(self, root, traversal):
        # left-subtree -> right-subtree -> root
        if root:
            traversal = self.post_order_traversal(root.left, traversal)
            traversal = self.post_order_traversal(root.right, traversal)
            traversal += str(root.value) + "-"

        return traversal

    def iterative_post_order(self, root):
        if not root:
            return None

        stack = Stack()
        result = []
        stack.push(root)

        while stack.size() > 0:
            current_node = stack.pop()
            result.append(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

        result.reverse()
        return result


tree = BinaryTree(7)
tree.root.left = Node(4)
tree.root.right = Node(8)
tree.root.left.left = Node(2)
tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
tree.root.right.right = Node(10)

print(tree.print_tree("in_order"))
# print(tree.iterative_post_order(tree.root))
