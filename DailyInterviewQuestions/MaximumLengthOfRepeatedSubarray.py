class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]
        max_length = 0
        
        for i in range(1, len(nums2) + 1):
            for j in range(1, len(nums1) + 1):
                if nums2[i - 1] == nums1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
        
        return max_length
        
     
