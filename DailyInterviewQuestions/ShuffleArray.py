from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original_nums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.original_nums[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums) - 1):
            rand_idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[rand_idx] = self.nums[rand_idx], self.nums[i]
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()