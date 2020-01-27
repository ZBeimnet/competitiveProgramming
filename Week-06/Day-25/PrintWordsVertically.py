from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        word_list = s.split()  # "how are you" ---> ["how", "are", "you"]

        max_length = len(word_list[0])
        for i in range(1, len(word_list)):
            current_length = len(word_list[i])
            if current_length > max_length:
                max_length = current_length

        output = []
        count = 0
        while count < max_length:
            current_word = ""

            for i in range(len(word_list)):
                if len(word_list[i]) > count:
                    current_word += word_list[i][count]
                else:
                    current_word += " "

            index_last_char = len(current_word)
            for i in range(len(current_word) - 1, -1, -1):
                if current_word[i] != " ":
                    index_last_char = i
                    break

            if len(current_word) - 1 != index_last_char:
                current_word = current_word[:index_last_char + 1]

            output.append(current_word)
            count += 1

        return output

