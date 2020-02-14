class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        new_shift = shifts

        for i in range(len(new_shift) - 2, -1, -1):
            new_shift[i] += new_shift[i + 1]

        result = []
        for i in range(len(new_shift)):
            current = chr(((ord(S[i]) - 97 + new_shift[i]) % 26) + 97)
            result.append(current)

        return "".join(result)