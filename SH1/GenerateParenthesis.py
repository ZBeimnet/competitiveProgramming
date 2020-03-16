from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        queue = deque([[[], n, n]])  # our states --> strings in list, openning_br_no, closing_br_no

        while queue:
            current_string, openning_no, closing_no = queue.popleft()
            # print(current_string, openning_no, closing_no)
            # checking if we've reached the end-state (openning=closing=0)
            if openning_no == 0 and closing_no == 0:
                result.append("".join(current_string))
                continue

            # decisions at each step of the way
            if 0 < openning_no < closing_no:
                next_string_one = current_string + ['(']
                next_string_two = current_string + [')']
                queue.append([next_string_one, openning_no - 1, closing_no])
                queue.append([next_string_two, openning_no, closing_no - 1])
            elif 0 < openning_no == closing_no:
                next_string_one = current_string + ['(']
                queue.append([next_string_one, openning_no - 1, closing_no])
            elif openning_no == 0 and closing_no > 0:
                next_string_one = current_string + ([')'] * closing_no)
                queue.append([next_string_one, openning_no, 0])

        return result