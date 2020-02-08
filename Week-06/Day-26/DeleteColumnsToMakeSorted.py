class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        deletion_indexes = 0

        for i in range(len(A[0])):
            for j in range(len(A) - 1):
                if A[j][i] > A[j + 1][i]:
                    deletion_indexes += 1
                    break

        return deletion_indexes
