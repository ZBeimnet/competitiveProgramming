def pancake_sorting(li):
    k_values = []

    current_index = len(li)
    while current_index > 0:
        # find the index of the maximum element in the list
        k = find_max(li, current_index)

        # if the maximum element is at the end of the list, do not flip
        if k == current_index - 1:
            current_index -= 1
        # else reverse the list upto the maximum element and then
        # reverse the list upto current_index --> to make maximum element at the end
        else:
            li = flip_list(li, k)
            k_values.append(k + 1)
            li = flip_list(li, current_index - 1)
            k_values.append(current_index)
            current_index -= 1
    print(li)
    return k_values


def flip_list(li, k):

    return li[:(k+1)][::-1] + li[(k+1):]


def find_max(li, n):
    maximum = li[0]
    maximum_index = 0

    for i in range(1, n):
        if li[i] > maximum:
            maximum = li[i]
            maximum_index = i

    return maximum_index


print(pancake_sorting([5, 2, 7, 8, 4, 1]))
