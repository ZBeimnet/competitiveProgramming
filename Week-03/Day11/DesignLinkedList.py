class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        counter = 0
        start_node = self.head
        while start_node:
            if counter == index:
                return start_node.data
            else:
                start_node = start_node.next
                counter += 1

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node

        start_node = self.head
        while start_node.next:
            start_node = start_node.next
        start_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        curr = self.head
        if index == 0:
            self.addAtHead(val)
        else:
            node = Node(val)
            while curr.next and index > 0:
                index -= 1
                prev = curr
                curr = curr.next
            if index == 0:
                prev.next = node
                node.next = curr
            elif index == 1:
                curr.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            while curr and index > 0:
                index -= 1
                prev = curr
                curr = curr.next
            if curr:
                prev.next = curr.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)