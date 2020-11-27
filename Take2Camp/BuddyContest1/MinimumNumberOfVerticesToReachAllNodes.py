class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set()
        result = []

        for f, t in edges:
            incoming.add(t)

        for i in range(n):
            if i not in incoming:
                result.append(i)

        return result