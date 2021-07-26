from collections import defaultdict, deque
from typing import List
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        answer = [0] * n
        graph = defaultdict(list)
        # build graph
        for xi, yi in paths:
            graph[xi].append(yi)
            graph[yi].append(xi)
        # run bfs on each garden
        for garden in graph:
            if answer[garden - 1] == 0:
                self.bfs(garden, graph, answer)
        # for gardens with no path
        for i, f_type in enumerate(answer):
            if f_type == 0:
                answer[i] = 1
        return answer
    
    def bfs(self, garden, graph, answer):
        queue = deque([(garden, 1)]) # states -> (garden, flower_type)
        answer[garden - 1] = 1
        while queue:
            garden_no, f_type = queue.popleft()
            for neighbour in graph[garden_no]:
                if answer[neighbour - 1] == 0:
                    excluded_types = set([f_type] + [answer[x - 1] for x in graph[neighbour]])
                    new_type = next((x for x in range(1, 5) if x not in excluded_types))
                    answer[neighbour - 1] = new_type
                    queue.append((neighbour, new_type))


# Greedy Soln from leetcode discuss
# https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290858/JavaC%2B%2BPython-Greedily-Paint
from collections import defaultdict, deque
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        answer = [0] * n
        graph = defaultdict(list)
        
        # build graph
        for xi, yi in paths:
            graph[xi].append(yi)
            graph[yi].append(xi)
        
        # since we have at most 3 neighbour gardens, 
        # we can greedily choosing 1 type for each garden out of 4 types
        for i in range(n):
            answer[i] = ({1, 2, 3, 4} - {answer[x - 1] for x in graph[i + 1]}).pop()
        
        return answer
