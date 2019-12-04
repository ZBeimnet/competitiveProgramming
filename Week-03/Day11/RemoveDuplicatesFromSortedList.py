from LinkedList import LinkedList, Node


def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    current_node = head
    next_node = current_node.next
    while next_node is not None:
        if current_node.data == next_node.data:
            current_node.next = next_node.next
            next_node = current_node
        current_node = next_node
        next_node = next_node.next

    return head


list1 = LinkedList()
head_node = Node(1)
list1.head = head_node
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
head_node.next = n2
n2.next = n3
n3.next = n4
list1.insert_after(n2, 2)
list1.print_list()
remove_duplicates(head_node)
list1.print_list()