from LinkedList import LinkedList, Node


def delete_node(node):
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    next_node.next = None


list1 = LinkedList()
head = Node(1)
list1.head = head
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
head.next = n2
n2.next = n3
n3.next = n4
list1.print_list()
delete_node(n2)
list1.print_list()