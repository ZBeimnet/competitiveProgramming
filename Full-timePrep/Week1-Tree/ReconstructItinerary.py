# I could only come up with a brute-force soln with resulted in TLE.
# https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
# https://leetcode.com/problems/reconstruct-itinerary/discuss/375397/Simply-simple-Python-Solution-Using-stack-for-dfs-with-comments
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
        
        