
def insertion_sort(li):
    list_length = len(li)

    for i in range(1, list_length):
        element_to_be_inserted = li[i]

        j = i - 1
        while j >= 0 and element_to_be_inserted < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = element_to_be_inserted
    return li


print(insertion_sort([7, 3, 2, 1, 4, 7]))
