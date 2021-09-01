# KMP
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        new_s = f"{s}#{s[::-1]}"
        prefix = [0] * len(new_s)
        l, r = 0, 1
        
        while r < len(new_s):
            if new_s[l] == new_s[r]:
                prefix[r] = l + 1
                l += 1
                r += 1
            else:
                if l == 0:
                    r += 1
                else:
                    l = prefix[l-1]
        
        return f"{s[prefix[-1]:][::-1]}{s}"
        
