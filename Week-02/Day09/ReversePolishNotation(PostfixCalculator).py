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


class Solution:
    def evalRPN(self, tokens) -> int:
        operators = ['+', '-', '*', '/']
        list_length = len(tokens)

        stack = Stack()

        for i in range(list_length):
            if tokens[i] not in operators:
                stack.push(tokens[i])
            else:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if tokens[i] == '*':
                    stack.push(operand1 * operand2)
                elif tokens[i] == '/':
                    stack.push(int(operand2 / operand1))
                elif tokens[i] == '+':
                    stack.push(operand1 + operand2)
                else:
                    stack.push(operand1 - operand2)

        return stack.pop()


sol = Solution()
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
print(sol.evalRPN(["0", "3", "/"]))
