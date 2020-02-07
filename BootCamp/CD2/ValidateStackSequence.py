class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        length = len(pushed)
        push_pt = 0
        pop_pt = 0

        while pop_pt < length:

            if push_pt < length:
                next_popped = popped[pop_pt]
                next_pushed = pushed[push_pt]

                if next_pushed != next_popped:
                    if stack and stack[-1] != next_popped:
                        stack.append(next_pushed)
                        push_pt += 1
                    elif stack and stack[-1] == next_popped:
                        stack.pop()
                        pop_pt += 1
                    elif not stack:
                        stack.append(next_pushed)
                        push_pt += 1
                else:
                    push_pt += 1
                    pop_pt += 1
            else:
                if stack[-1] == popped[pop_pt]:
                    stack.pop()
                    pop_pt += 1
                else:
                    return False

        return True


