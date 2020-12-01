from math import floor, sqrt


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        divisors_sum = 0

        for i in range(2, floor(sqrt(num)) + 1):
            if num % i == 0:
                if i == num // i:
                    divisors_sum += i
                else:
                    divisors_sum += i + num // i

        return divisors_sum + 1 == num