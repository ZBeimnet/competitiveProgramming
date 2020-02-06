class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return None

        self.nums = [[nums[0], nums[0]]]

        for i in range(1, len(nums)):
            self.nums.append([nums[i], nums[i] + self.nums[i - 1][1]])

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j][1] - self.nums[i][1] + self.nums[i][0]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)