def sort_colors(nums):
    num_length = len(nums)
    colors_count = [0] * 3

    # iterating over nums list and counting each color value
    for i in range(num_length):
        colors_count[nums[i]] += 1

    # modifying nums in-place based on count
    counter = 0
    for i in range(len(colors_count)):
        for j in range(colors_count[i]):
            nums[counter] = i
            counter += 1

    print(nums)


sort_colors([2, 0, 2, 1, 1, 0])
