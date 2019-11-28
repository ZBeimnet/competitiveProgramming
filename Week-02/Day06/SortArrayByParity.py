def sort_by_parity(li):
    list_length = len(li)
    sorted_list = [0] * list_length

    even_count = 0
    odd_count = 1
    for i in range(list_length):
        if li[i] % 2 == 0:
            sorted_list[even_count] = li[i]
            even_count += 2
        else:
            sorted_list[odd_count] = li[i]
            odd_count += 2

    return sorted_list


print(sort_by_parity([4, 2, 5, 7]))
