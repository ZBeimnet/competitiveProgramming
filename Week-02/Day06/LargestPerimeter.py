def largest_perimeter(array):
    array.sort(reverse=True)
    perimeter = 0

    for i in range(len(array) - 2):
        if array[i] + array[i + 1] > array[i + 2]:
            if array[i + 1] + array[i + 2] > array[i]:
                if array[i] + array[i + 2] > array[i + 1]:
                    perimeter = array[i] + array[i + 1] + array[i + 2]
                    break

    return perimeter


print(largest_perimeter([2, 1, 2]))
