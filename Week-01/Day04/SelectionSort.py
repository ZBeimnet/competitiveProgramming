
def selection_sort(li):
    list_length = len(li)

    for i in range(list_length):
        index_of_minimum = i

        for j in range(i+1, list_length):
            if li[j] < li[index_of_minimum]:
                index_of_minimum = j

        li[i], li[index_of_minimum] = li[index_of_minimum], li[i]

    return li


print(selection_sort([7, 3, 2, 1, 4, 7]))
