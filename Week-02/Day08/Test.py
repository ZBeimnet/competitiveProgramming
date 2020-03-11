# class Student:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#
# a = Student("Beimnet", 4)
# b = Student("Kidus", 2)
# c = Student("Dani", 3)
# d = a
# dict = {a: 1, b: 1, c: 1}
#
# unique = {a, b, c, d}
# print(unique)
import time


def fib(n, memo):
    if n == 0 or n == 1:
        return n
    elif n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def fib_bottom_up(n):
    memo = {0: 0, 1: 1}
    if n == 0 or n == 1:
        return memo[n]
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def fib_var(n):
    if n < 2:
        return n
    fib_one, fib_two = 0, 1
    for _ in range(2, n):
        fib_one, fib_two = fib_two, fib_one + fib_two
    return fib_one + fib_two


def triple_step(n, memo):
    if n < 4:
        return n
    elif n not in memo:
        memo[n] = triple_step(n - 3, memo) + triple_step(n - 2, memo) + triple_step(n - 1, memo)
    return memo[n]


start = time.time()
# print(fib(998, {}))
# print(fib_var(10000))
print(triple_step(100, {}))
end = time.time()
print(end - start)













