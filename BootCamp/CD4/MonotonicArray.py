class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        monotonic = 0  # 0 - not determined yet, 1 - mono_inc, 2 - mono_dec

        for i in range(len(A) - 1):
            if A[i] < A[i + 1] and monotonic == 0:
                monotonic = 1
            elif A[i] > A[i + 1] and monotonic == 0:
                monotonic = 2

            if A[i] < A[i + 1] and monotonic == 2:
                return False
            if A[i] > A[i + 1] and monotonic == 1:
                return False

        return True

