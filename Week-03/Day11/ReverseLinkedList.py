from LinkedList import LinkedList, Node


def reverse_linked_list(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return head

    previous_node = None
    current_node = linked_list.head
    next_node = current_node.next

    while next_node is not None:
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        next_node = next_node.next

    current_node.next = previous_node

    while current_node is not None:
        print(str(current_node.data) + " -->", end=" ")
        current_node = current_node.next
    print(current_node)


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
reverse_linked_list(list1)

