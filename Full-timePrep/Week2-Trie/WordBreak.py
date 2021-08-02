from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, set(wordDict), 0, {})
    
    def dfs(self, s, word_dict, start, cache):
        if start in cache:
            return cache[start]
        if start == len(s):
            return True
        
        if s[start:] in word_dict: # important prunning :)
            cache[start] = True
            return True
        for i in range(start + 1, len(s)):
            if s[start:i] in word_dict:
                break_res = self.dfs(s, word_dict, i, cache)
                if break_res:
                    cache[start] = True
                    return True
        
        cache[start] = False
        return False