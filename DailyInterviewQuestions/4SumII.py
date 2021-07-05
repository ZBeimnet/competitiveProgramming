from collections import defaultdict
from typing import List
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum_pairs = defaultdict(int)
        tuples = 0
        
        for i in range(len(A)):
            for j in range(len(B)):
                sum_pairs[A[i] + B[j]] += 1
        
        for i in range(len(C)):
            for j in range(len(D)):
                if -(C[i] + D[j]) in sum_pairs:
                    tuples += sum_pairs[-(C[i] + D[j])]
        
        return tuples
