from time import time


def fibonacci_one(num):
    if num == 0 or num == 1:
        return num

    return fibonacci_one(num - 1) + fibonacci_one(num - 2)


def fibonacci_memo(num, memo):
    if num == 0 or num == 1:
        return num

    if memo[num] == 0:
        memo[num] = fibonacci_memo(num - 1, memo) + fibonacci_memo(num - 2, memo)

    return memo[num]


start = time()
print(fibonacci_memo(990, [0] * 1000))
end = time()
print(end - start)
