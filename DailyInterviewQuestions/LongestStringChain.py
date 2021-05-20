from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        graph = defaultdict(list)
        cache = {}
        longest_chain = 0
        
        for word in words:
            graph[len(word)].append(word)
        
        for start in graph:
            for word in graph[start]:
                longest_from_word = self.dfs(word, graph, cache)
                longest_chain = max(longest_chain, longest_from_word)
        
        return longest_chain
    
    def dfs(self, start, graph, cache):
        if start in cache:
            return cache[start]
        if len(start) + 1 not in graph:
            return 1
        
        longest = 0
        
        for word in graph[len(start) + 1]:
            if self.check_chainability(start, word):
                longest = max(longest, self.dfs(word, graph, cache))
        
        cache[start] = longest + 1
        return longest + 1
    
    def check_chainability(self, word1, word2):
        for i in range(len(word2)):
            if word1 == f"{word2[:i]}{word2[i + 1:]}":
                return True
        return False
