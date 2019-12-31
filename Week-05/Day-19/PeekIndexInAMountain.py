class Solution:
    def peakIndexInMountainArray(self, A) -> int:

        # for i in range(1, len(A)-1):
        #     if A[i] > A[i+1]:
        #         return i

        left = 0
        right = len(A) - 1

        while left < right:
            mid = (left + right) // 2

            if A[mid] > A[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left