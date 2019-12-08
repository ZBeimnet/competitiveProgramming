class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_el = None

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.min_el = x
            self.stack.append(x)
        else:
            if x < self.min_el:
                self.stack.append(2 * x - self.min_el)
                self.min_el = x
            else:
                self.stack.append(x)

    def pop(self) -> None:
        popped_el = self.stack.pop()
        current_min = self.min_el
        if popped_el < current_min:
            self.min_el = 2 * current_min - popped_el

    def top(self) -> int:
        top_el = self.stack[-1]
        if top_el < self.min_el:
            return self.min_el
        return top_el

    def getMin(self) -> int:
        return self.min_el

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()