class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    new_list = ListNode(0)

    if l1 is None:
        return l2
    if l2 is None:
        return l1

    current_new = new_list
    current_l1 = l1
    current_l2 = l2
    while current_l1.next is not None:
        while current_l2.next is not None:
            if current_l1.val <= current_l2.val:
                current_new.next = current_l1
                current_new = current_new.next
                current_l1 = current_l1.next
            else:
                current_new.next = current_l2
                current_new = current_new.next
                current_l2 = current_l2.next

    if current_l2.next is None:
        current_new.next = current_l2
        current_new = current_new.next
        while current_l1 is not None:
            current_new.next = current_l1
            current_new = current_new.next
            current_l1 = current_l1.next

    if current_l1.next is None:
        current_new.next = current_l1
        current_new = current_new.next
        while current_l2 is not None:
            current_new.next = current_l2
            current_new = current_new.next
            current_l2 = current_l2.next

    second_node = new_list.next
    new_list = second_node

    return new_list


print(merge_two_lists([2], [1]))
