class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = [0] * 100001
        for _, num in enumerate(nums):
            count[num + 50000] += 1

        output = []
        for i, current_count in enumerate(count):
            if current_count:
                output.extend([i - 50000] * current_count)

        return output