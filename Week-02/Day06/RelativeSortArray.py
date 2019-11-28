def sort_array_relatively(array1, array2):
    sorted_list = []
    left_out_elements = []

    arr2_index = 0
    while arr2_index < len(array2):
        for i in range(len(array1)):
            if array1[i] == array2[arr2_index]:
                sorted_list.append(array1[i])
        arr2_index += 1

    for i in range(len(array1)):
        if array1[i] not in array2:
            left_out_elements.append(array1[i])

    left_out_elements.sort()

    for i in range(len(left_out_elements)):
        sorted_list.append(left_out_elements[i])

    return sorted_list


print(sort_array_relatively([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))

