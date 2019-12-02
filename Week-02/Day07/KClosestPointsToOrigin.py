def k_closest(points, k):
    # points_length = len(points)
    #     #
    #     # if k == points_length:
    #     #     return points
    #     #
    #     # for i in range(points_length):
    #     #     index_of_minimum = i
    #     #
    #     #     for j in range(i+1, points_length):
    #     #         if square(points[index_of_minimum]) > square(points[j]):
    #     #             index_of_minimum = j
    #     #
    #     #     points[i], points[index_of_minimum] = points[index_of_minimum], points[i]
    #     #
    #     #     if i == k:
    #     #         break
    points = merge_sort_based_on_square(points)

    return points[:k]

def merge_sort_based_on_square(li):
    list_length = len(li)
    if list_length > 1:
        middle_index = list_length // 2
        left_list = li[:middle_index]
        right_list = li[middle_index:]

        merge_sort_based_on_square(left_list)
        merge_sort_based_on_square(right_list)

        left_index = right_index = merge_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if square(left_list[left_index]) < square(right_list[right_index]):
                li[merge_index] = left_list[left_index]
                left_index += 1
            else:
                li[merge_index] = right_list[right_index]
                right_index += 1
            merge_index += 1

        while left_index < len(left_list):
            li[merge_index] = left_list[left_index]
            left_index += 1
            merge_index += 1

        while right_index < len(right_list):
            li[merge_index] = right_list[right_index]
            right_index += 1
            merge_index += 1

    return li


def square(point):
    return (point[0]*point[0]) + (point[1]*point[1])


# print(merge_sort([[3, 3], [5, -1], [-2, 4]], 2))
print(k_closest([[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]],
5))