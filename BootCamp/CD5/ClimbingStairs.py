class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        arr = [0] * n

        # base cases
        arr[0] = 1
        arr[1] = 2

        for i in range(2, n):
            # state transition relation
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[-1]
