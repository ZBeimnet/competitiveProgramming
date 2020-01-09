import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        n = n - 1

        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        i = 2
        while i <= math.floor(math.sqrt(n)):
            if primes[i]:
                k = i * i
                while k <= n:
                    primes[k] = False
                    k += i
            i += 1

        prime_count = 0
        for i in range(len(primes)):
            if primes[i]:
                prime_count += 1

        return prime_count
