def find_intersection(array1, array2):
    intersection = []

    # always make array1 the smaller array
    if len(array1) > len(array2):
        array1, array2 = array2, array1

    # loop through array1 and find if element is found in array2
    for i in range(len(array1)):
        if array1[i] in array2:
            if array1[i] not in intersection:
                intersection.append(array1[i])

    return intersection


print(find_intersection([1, 2, 2, 1], [2, 2]))
print(find_intersection([4, 9, 5], [9, 4, 9, 8, 4]))
