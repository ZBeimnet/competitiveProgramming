class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        new_a = sorted(A)
        moves = 0

        for i in range(1, len(new_a)):
            if new_a[i - 1] >= new_a[i]:
                moves += new_a[i - 1] - new_a[i] + 1
                new_a[i] += new_a[i - 1] - new_a[i] + 1

        return moves