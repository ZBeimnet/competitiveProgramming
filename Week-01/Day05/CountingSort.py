def counting_sort(li):
    list_length = len(li)
    sorted_list = []

    # finding the biggest element in the list
    biggest_element = find_max(li)

    # initializing count from 0 ---> biggest_element
    count = [0] * (biggest_element + 1)

    # iterating over the unsorted-list and increasing count of each element
    for element in range(list_length):
        count[li[element]] += 1

    # populating a sorted-list based on count
    for element in range(len(count)):
        if count[element] != 0:
            for i in range(count[element]):
                sorted_list.append(element)

    return sorted_list


def find_max(li):
    biggest_element = li[0]

    for element in range(1, len(li)):
        if li[element] > biggest_element:
            biggest_element = li[element]

    return biggest_element


def main():
    li = [100, 3, 2, 2, 1]
    print(counting_sort(li))


main()



