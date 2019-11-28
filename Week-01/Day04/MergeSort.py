
def merge_sort(li):
    list_length = len(li)
    if list_length > 1:
        middle_index = list_length // 2
        left_list = li[:middle_index]
        right_list = li[middle_index:]

        merge_sort(left_list)
        merge_sort(right_list)

        left_index = right_index = merge_index = 0

        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
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


print(merge_sort([7, 3, 2, 1, 4, 7]))
