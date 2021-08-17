from collections import defaultdict
class Solution:
    def solve(self, nums, target):
        subarray_sum = defaultdict(int)
        count = prefix_sum = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum == target:
                count += 1
            count += subarray_sum[prefix_sum - target]
            subarray_sum[prefix_sum] += 1
        
        return count
        
