def get_different_number(arr):
    for i in range(len(arr)):
        temp = arr[i]
        while temp < len(arr) and arr[temp] != temp:
            t = temp
            temp = arr[temp]
            arr[temp] = t

    for i, num in enumerate(arr):
        if i != num:
            return i
    return len(arr)

print(get_different_number([2, 0, 1, 3]))