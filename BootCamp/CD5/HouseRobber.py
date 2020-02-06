class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_memo = [0] * (len(nums) + 1)
        nums_memo[1] = nums[0]

        for i in range(1, len(nums)):
            nums_memo[i + 1] = max(nums_memo[i], nums_memo[i - 1] + nums[i])

        return nums_memo[-1]