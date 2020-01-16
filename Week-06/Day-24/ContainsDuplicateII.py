class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        dictionary = {}

        for i in range(length):
            if nums[i] in dictionary:
                dictionary[nums[i]].append(i)
            else:
                dictionary[nums[i]] = [i]

        for key in dictionary.keys():
            current_element = dictionary[key]
            current_length = len(current_element)
            if current_length > 1:
                for i in range(1, current_length):
                    if (current_element[i] - current_element[i - 1]) <= k:
                        return True

        return False