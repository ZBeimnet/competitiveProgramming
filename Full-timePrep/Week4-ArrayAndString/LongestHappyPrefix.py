class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix = [0] * len(s)
        i, j = 0, 1
        
        while j < len(s):
            if s[i] == s[j]:
                prefix[j] = i + 1
                j += 1
                i += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = prefix[i-1]
        
        return s[:prefix[-1]]
