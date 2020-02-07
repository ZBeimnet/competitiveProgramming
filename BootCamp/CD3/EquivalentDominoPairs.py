class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #         sum_count = [0] * 19

        #         for i in range(len(dominoes)):
        #             current_sum = dominoes[i][0] + dominoes[i][1]
        #             sum_count[current_sum] += 1

        # domino_pairs = 0
        # for i in range(len(sum_count)):
        #     if sum_count[i] > 1:
        #         domino_pairs += (sum_count[i] * (sum_count[i] - 1)) // 2

        sum_count = {}
        for i in dominoes:
            if tuple(sorted(i)) in sum_count:
                sum_count[tuple(sorted(i))] += 1
            else:
                sum_count[tuple(sorted(i))] = 1

        domino_pairs = 0
        for pair in sum_count.values():
            domino_pairs += ((pair) * (pair - 1)) // 2

        return domino_pairs