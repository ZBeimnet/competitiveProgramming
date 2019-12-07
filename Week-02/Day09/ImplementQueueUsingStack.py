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


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # copy the stack to another, to get the first element
        new_stack = Stack()
        for i in range(self.stack.size()):
            new_stack.push(self.stack.pop())

        # now remove the the element at the top of the new stack
        popped_el = new_stack.pop()

        # now copy back the elements to get the correct order
        for i in range(new_stack.size()):
            self.stack.push(new_stack.pop())

        return popped_el

    def peek(self) -> int:
        """
        Get the front element.
        """
        # copy the stack to another, to get the first element
        new_stack = Stack()
        for i in range(self.stack.size()):
            new_stack.push(self.stack.pop())

        # now remove the the element at the top of the new stack
        popped_el = new_stack.pop()
        # push it back
        new_stack.push(popped_el)

        # now copy back the elements to get the correct order
        for i in range(new_stack.size()):
            self.stack.push(new_stack.pop())

        return popped_el

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stack.size() == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
