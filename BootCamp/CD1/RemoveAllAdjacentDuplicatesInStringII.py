class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        stack.append(["start", 1])

        for char in s:
            if char == stack[-1][0]:
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        output = ""
        for char, count in stack:
            output += char * count

        return output[5:]










