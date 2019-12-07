class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.enqueue(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        stack_length = self.stack.size()

        for i in range(stack_length - 1):
            self.stack.enqueue(self.stack.dequeue())

        return self.stack.dequeue()

    def top(self) -> int:
        """
        Get the top element.
        """
        stack_length = self.stack.size()

        for i in range(stack_length - 1):
            self.stack.enqueue(self.stack.dequeue())

        dequeued_el = self.stack.dequeue()
        self.stack.enqueue(dequeued_el)

        return dequeued_el

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack.size() == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()