def remove_one(li, list_length):
    nums = li.split()
    nums = [int(nums[x]) for x in range(list_length)]

    max_length = 1
    removed = 0
    pointer_one = 0
    pointer_two = 1
    while pointer_one > list_length-2:
        current_length = 1
        while removed % 2 == 0:
            if nums[pointer_one] < nums[pointer_two]:
                current_length += 1
