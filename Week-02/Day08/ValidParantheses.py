class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        opening_braces = ['(', '{', '[']
        closing_braces = [')', '}', ']']

        for char in s:
            if char in opening_braces:
                stack.push(char)
            elif char in closing_braces:
                if stack.isEmpty():
                    return False

                top = stack.pop()
                if top == '(' and char == ')':
                    continue
                elif top == '{' and char == '}':
                    continue
                elif top == '[' and char == ']':
                    continue
                else:
                    return False

        if stack.isEmpty():
            return True

        return False
