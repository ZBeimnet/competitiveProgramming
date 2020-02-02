def fractional_knapsack(arr, weight):
    ratio_arr = []

    for i in range(len(arr)):
        ratio_arr.append((arr[i][0] / arr[i][1], i))

    ratio_arr.sort(reverse=True)
    total_value = 0
    for item in ratio_arr:
        if arr[item[1]][1] <= weight:
            total_value += arr[item[1]][0]
            weight -= arr[item[1]][1]
        else:
            total_value += int(arr[item[1]][0] * (weight / arr[item[1]][1]))
            break

    return total_value


print(fractional_knapsack([(60, 10), (100, 20), (120, 30)], 50))
