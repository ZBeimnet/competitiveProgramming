import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            current_sum = 1 + num
            divisor_count = 2
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisor_count += 1
                    divisor1 = num // i
                    divisor2 = num // (num // i)
                    current_sum += divisor1
                    if divisor1 != divisor2:
                        divisor_count += 1
                        current_sum += divisor2
                if divisor_count > 4:
                    break
            if divisor_count == 4:
                total += current_sum

        return total