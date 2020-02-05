def factorial_tabular(x):
    dp = [0] * 100

    dp[0] = 1   # base case
    for i in range(1, x + 1):
        dp[i] = i * dp[i - 1]   # state transition relation

    return dp[x]


def factorial_mem(x, dp):
    # base case
    if x == 0:
        return 1

    if dp[x] != 0:
        return dp[x]

    dp[x] = x * factorial_mem(x - 1, dp)

    return dp[x]


print(factorial_mem(4, [0] * 100))
print(factorial_tabular(4))
