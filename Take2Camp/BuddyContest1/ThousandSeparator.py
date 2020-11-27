class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        nums = []
        while n > 0:
            curr = str(n % 1000)
            curr_len = len(curr)
            if curr_len < 3:
                curr = "0" * (3 - curr_len) + curr
            nums.append(curr)
            n = n // 1000

        nums.reverse()
        nums[0] = str(int(nums[0]))
        return ".".join(nums)
