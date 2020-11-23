class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        fair_indices = 0
        right_sum = [[0, 0] for _ in range(n)]  # [even, odd]
        left_sum = [[0, 0] for _ in range(n)]

        # build right sum
        right_sum[0] = [nums[0], 0]
        for i in range(1, n):
            if i % 2 == 0:
                right_sum[i][0] = nums[i] + right_sum[i - 1][0]
                right_sum[i][1] = right_sum[i - 1][1]
            else:
                right_sum[i][1] = nums[i] + right_sum[i - 1][1]
                right_sum[i][0] = right_sum[i - 1][0]

        # build left sum
        left_sum[-1] = [0, nums[-1]]
        if (n - 1) % 2 == 0:
            left_sum[-1] = [nums[-1], 0]
        for i in range(n - 2, -1, -1):
            if i % 2 == 0:
                left_sum[i][0] = nums[i] + left_sum[i + 1][0]
                left_sum[i][1] = left_sum[i + 1][1]
            else:
                left_sum[i][1] = nums[i] + left_sum[i + 1][1]
                left_sum[i][0] = left_sum[i + 1][0]

        # checking for possible indices to remove
        for i in range(n):
            if i == 0:
                even_sum = left_sum[i + 1][1]
                odd_sum = left_sum[i + 1][0]
                if even_sum == odd_sum:
                    fair_indices += 1
            elif i == n - 1:
                even_sum = right_sum[i - 1][0]
                odd_sum = right_sum[i - 1][1]
                if even_sum == odd_sum:
                    fair_indices += 1
            else:
                even_sum = right_sum[i - 1][0] + left_sum[i + 1][1]
                odd_sum = right_sum[i - 1][1] + left_sum[i + 1][0]
                if even_sum == odd_sum:
                    fair_indices += 1

        return fair_indices
