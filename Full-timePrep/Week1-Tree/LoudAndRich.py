from collections import defaultdict
from typing import List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        answer = [-1] * len(quiet)
        
        # build graph: {a: b(richer than a), c(richer than a)}
        for rich in richer:
            graph[rich[1]].append(rich[0])
        
        # running dfs on each person to find answer[person]
        for i in range(len(quiet)):
            if answer[i] == -1:
                self.dfs(graph, i, answer, quiet)
        
        return answer
    
    def dfs(self, graph, person, answer, quiet):
        if answer[person] != -1: # return answer of person if it is already calculated
            return answer[person]
        if len(graph[person]) == 0: # the richest person
            answer[person] = person
            return person
        
        loudest_p = person
        for richer in graph[person]:
            louder_p = self.dfs(graph, richer, answer, quiet)
            if quiet[loudest_p] > quiet[louder_p]:
                loudest_p = louder_p
                
        answer[person] = loudest_p
        return loudest_p
        
        
        