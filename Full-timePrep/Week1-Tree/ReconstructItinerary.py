from collections import defaultdict
from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(reverse=True)
        for start, end in tickets:
            graph[start].append(end)
        
        stack = ["JFK"]
        result = []
        while stack:
            top = stack[-1]
            if top in graph and len(graph[top]) > 0:
                stack.append(graph[top].pop())
            else:
                result.append(stack.pop())
        
        return result[::-1]
        
        