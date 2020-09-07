from time import time

# a = ABCBDAB  --> BCAB
# b = BDCABA
# LCS(BCCDAB, BDCABA) = B + LCS(CCDAB, DCABA) --> max(LCS(CBDAB, CABA), LCS(BDAB, DCABA))


def treasure_hunt(grid):
    return dfs(grid, (0, 0), (len(grid) - 1, 0)) + dfs(grid, (0, len(grid[0]) - 1), (len(grid) - 1, len(grid[0]) - 1))


def dfs(grid, start, end):
    visited = {start}
    neighbours = [(1, 1), (1, -1), (1, 0)]
    stack = [[start, grid[start[0]][start[1]]]]
    max_sum = 0
    while stack:
        point, curr_sum = stack.pop()
        if point == end:
            max_sum = max(max_sum, curr_sum)
        for neighbour in neighbours:
            x = point[0] + neighbour[0]
            y = point[1] + neighbour[1]
            if 0 <= x < len(grid) and \
                0 <= y < len(grid[0]) and \
                    (x, y) not in visited:
                stack.append([(x, y), curr_sum + grid[x][y]])
                visited.add((x, y))
    return max_sum


def main():
    row, col = input().split()
    elements = input().split()
    grid = [[0 for _ in range(int(col))] for _ in range(int(row))]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = int(elements[count])
            count += 1

    return treasure_hunt(grid)


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
    dp = [([0] * (len(str1) + 1)) for _ in range(len(str2) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


def print_lcs(str_1, str_2, len_1, len_2, lookup):
    if len_1 == 0 or len_2 == 0:
        return ""

    if str_1[len_1 - 1] == str_2[len_2 - 1]:
        return print_lcs(str_1, str_2, len_1 - 1, len_2 - 1, lookup) + str_1[len_1 - 1]

    if lookup[len_1 - 1][len_2] > lookup[len_1][len_2 - 1]:
        return print_lcs(str_1, str_2, len_1 - 1, len_2, lookup)
    else:
        return print_lcs(str_1, str_2, len_1, len_2 - 1, lookup)


start = time()
print(lcs_tabular("bsdfdsfdkjkkscd", "abcdkjfkjlllsjkhkjhkjhkjjkdfd"))
end = time()
print(end - start)
# start = time()
# print(lcs_memo(0, 0, "bsdfdsfdkjkkscd", "abcdkjfkjlllsjkhkjhkjhkjjkdfd", {}))
# end = time()
# print(end - start)
