"""
"tree" -> eetr
count = [..., [2, e],..., [1, t], [1, r], ...]
output = ["ee", "t", "r"]
time -> s + nlogn ?, space -> n
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = [[0, chr(i)] for i in range(129)]  # 129 -> Ascii + 1
        output = []

        for char in s:
            char_count[ord(char)][0] += 1

        char_count.sort(reverse=True)

        for count, char in char_count:
            if count:
                output.append(char * count)

        return "".join(output)