from time import time


def lcs_recursive(i, j, str1, str2):
    # base-case
    if i == len(str1) or j == len(str2):
        return 0
    elif str1[i] == str2[j]:
        return 1 + lcs_recursive(i + 1, j + 1, str1, str2)
    else:
        return max(lcs_recursive(i, j + 1, str1, str2), lcs_recursive(i + 1, j, str1, str2))


def lcs_memo(i, j, str1, str2, memo):
    # base-case
    if i == len(str1) or j == len(str2):
        return 0
    elif (i, j) not in memo:
        if str1[i] == str2[j]:
            memo[(i, j)] = 1 + lcs_memo(i + 1, j + 1, str1, str2, memo)
        else:
            memo[(i, j)] = max(lcs_memo(i, j + 1, str1, str2, memo), lcs_memo(i + 1, j, str1, str2, memo))

    return memo[(i, j)]


def lcs_tabular(str1, str2):
    dp = [([0] * (len(str1) + 1)) for i in range(len(str2) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


start = time()
print(lcs_tabular("bsdfdsfdkjkkscd", "abcdkjfkjlllsjkhkjhkjhkjjkdfd"))
end = time()
print(end - start)
start = time()
print(lcs_memo(0, 0, "bsdfdsfdkjkkscd", "abcdkjfkjlllsjkhkjhkjhkjjkdfd", {}))
end = time()
print(end - start)
