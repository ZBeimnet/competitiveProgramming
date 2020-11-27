class Solution:
    def minOperations(self, nums: List[int]) -> int:
        total = sum(nums)
        operations = 0

        while total:
            for i in range(len(nums)):
                if nums[i] % 2:
                    nums[i] -= 1
                    total -= 1
                    operations += 1
            if total:
                for i in range(len(nums)):
                    nums[i] //= 2
                    total -= nums[i]
                operations += 1

        return operations