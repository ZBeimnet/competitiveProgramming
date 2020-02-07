class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        length = len(pairs)
        mcl_at_index = [1] * length

        sorted_pairs = sorted(pairs)

        for i in range(1, length):
            for j in range(i):
                if sorted_pairs[j][1] < sorted_pairs[i][0]:
                    mcl_at_index[i] = max(mcl_at_index[i], mcl_at_index[j] + 1)

        return max(mcl_at_index)

