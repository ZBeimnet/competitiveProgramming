class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        window_sum = 0
        window_length = 0
        starting_pt = 0

        for i in range(len(s)):
            current_diff = abs(ord(s[i]) - ord(t[i]))

            if current_diff + window_sum <= maxCost:
                window_length += 1
                window_sum += current_diff
            else:
                window_sum = window_sum - abs(ord(s[starting_pt]) - ord(t[starting_pt])) + abs(ord(s[i]) - ord(t[i]))
                starting_pt += 1

        return window_length
