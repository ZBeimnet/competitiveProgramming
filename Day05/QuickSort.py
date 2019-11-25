
def quick_sort(li, low, high):
    if low < high:
        dividing_index = divide(li, low, high)

        quick_sort(li, low, dividing_index - 1)
        quick_sort(li, dividing_index + 1, high)

    return li


def divide(li, low, high):
    i = low - 1
    pivot = li[high]

    for j in range(low, high):
        if li[j] < pivot:
            i += 1
            li[i], li[j] = li[j], li[i]

    li[i + 1], li[high] = li[high], li[i + 1]

    return i + 1


def main():
    li = [7, 3, 2, 1, 4, 7]
    list_length = len(li)
    print(quick_sort(li, 0, list_length - 1))


main()
