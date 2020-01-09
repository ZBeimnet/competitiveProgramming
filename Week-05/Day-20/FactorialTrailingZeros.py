class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_counts = 0
        i = 5
        while n // i >= 1:
            zero_counts += n // i
            i *= 5

        return zero_counts