from typing import List


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        right_max = T[n-1]
        res = [0] * n
        for i in range(n-2, -1, -1):
            t = T[i]
            if right_max <= t:
                right_max = t
            else:
                temp = 1
                while T[i+temp] <= t:
                    temp += res[i+temp]
                res[i] = temp
        return res

    def dailyTemperaturesUsingStack(self, t):
        length = len(t)
        result = [0]*length
        stack = Stack()

        for i in range(length):
            while not stack.isEmpty() and t[i] > t[stack.peek()]:
                result[stack.peek()] = i - stack.peek()
                stack.pop()
            stack.push(i)

        return result


t = Solution()
print(t.dailyTemperaturesUsingStack([73,74,75,71,69,72,76,73]))
