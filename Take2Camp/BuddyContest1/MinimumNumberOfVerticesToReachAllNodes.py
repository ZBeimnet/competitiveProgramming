class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        with_incoming = set()
        result = []

        for _, t in edges:
            with_incoming.add(t)

        for node in range(n):
            if node not in with_incoming:
                result.append(node)

        return result