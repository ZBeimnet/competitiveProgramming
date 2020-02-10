from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = [False] * len(M)
        friend_circles = 0

        for i in range(len(M)):
            if not visited[i]:
                self.dfs(i, M, visited)
                friend_circles += 1

        return friend_circles

    def dfs(self, i, M, visited):
        stack = [i]

        while stack:
            person_1 = stack.pop()

            for person_2 in range(len(M)):
                if M[person_1][person_2] == 1 and not visited[person_2]:
                    visited[person_2] = True
                    stack.append(person_2)

        return
