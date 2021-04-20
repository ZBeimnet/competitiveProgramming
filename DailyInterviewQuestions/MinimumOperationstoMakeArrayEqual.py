class Solution:
    def minOperations(self, n: int) -> int:
        target_ind = n // 2
        target_val = ((2 * target_ind) + 1, 2 * target_ind)[n % 2 == 0]
        
        return (target_ind * target_val) - (target_ind ** 2)
