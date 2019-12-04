class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(str(current_node.data) + " -->", end=" ")
            current_node = current_node.next
        print(current_node)

    def insert_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = node

    def insert_after(self, node, data):
        is_found = False
        start_node = self.head
        while start_node.next is not None:
            if start_node == node:
                is_found = True
                break
            else:
                start_node = start_node.next
        if is_found:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
        else:
            print("Node not found")

    def delete_node(self, delete_key):
        current_node = self.head
        previous_node = self.head

        if current_node.data == delete_key:
            self.head = current_node.next
            current_node = None
        while current_node is not None:
            if current_node.data == delete_key:
                break
            else:
                previous_node = current_node
                current_node = current_node.next
        if current_node is None:
            return
        previous_node.next = current_node.next
        current_node = None

# list1 = LinkedList()
# list1.head = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
#
# list1.head.next = e2
# e2.next = e3
# list1.insert_first("Sun")
# list1.insert_last("Thu")
# list1.insert_after(e2, "Tue-Night")
# list1.delete_node("Tue-Night")
# list1.print_list()
