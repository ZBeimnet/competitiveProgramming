def find_duplicate(nums):
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        if count > 1:
            return nums[i]


print(find_duplicate())

