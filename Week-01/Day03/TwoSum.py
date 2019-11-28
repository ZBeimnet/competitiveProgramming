from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    length_of_list = len(nums)

    for i in range(length_of_list):
        for j in range(i + 1, length_of_list):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum([2, 7, 11, 15], 9))
