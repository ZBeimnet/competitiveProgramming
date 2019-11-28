def radix_sort(li):
    biggest_number = find_max(li)

    exponent = 1
    while biggest_number // exponent > 0:
        counting_sort(li, exponent)
        exponent *= 10

    return li


def counting_sort(li, exponent):
    list_length = len(li)
    temp_sorted_list = [0] * list_length
    count = [0] * 10
    print("list --->", li)

    for i in range(0, list_length):
        index = li[i] // exponent
        count[index % 10] += 1
    print("count --->", count)

    for i in range(1, 10):
        count[i] += count[i - 1]
    print("count --->", count)

    i = list_length - 1
    while i >= 0:
        index = li[i] // exponent
        temp_sorted_list[count[index % 10] - 1] = li[i]
        count[index % 10] -= 1
        i -= 1
    print("count --->", count)
    print("temp_sorted_list --->", temp_sorted_list)

    for i in range(0, list_length):
        li[i] = temp_sorted_list[i]
    print()


def find_max(li):
    biggest_element = li[0]

    for element in range(1, len(li)):
        if li[element] > biggest_element:
            biggest_element = li[element]

    return biggest_element


def main():
    li = [100, 3, 2, 2, 1]
    print(radix_sort(li))


main()
