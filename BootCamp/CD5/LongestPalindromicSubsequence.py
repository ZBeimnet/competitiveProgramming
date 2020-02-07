class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [([0] * length) for i in range(length)]

        # every char is palindrome to itself
        for i in range(length):
            dp[i][i] = 1

        for i in range(1, length):
            start = 0
            while start < length - i:
                if s[start] == s[start + i]:
                    dp[start][start + i] = dp[start + 1][start + i - 1] + 2
                else:
                    dp[start][start + i] = max(dp[start][start + i - 1], dp[start + 1][start + i])
                start += 1

        return dp[0][length - 1]