from math import sqrt, floor


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        prime_count = 0
        nums = [True] * n
        nums[0] = nums[1] = False

        for i in range(2, floor(sqrt(n)) + 1):
            if nums[i]:
                for j in range(i ** 2, n, i):
                    nums[j] = False

        for i in range(len(nums)):
            if nums[i]:
                prime_count += 1

        return prime_count