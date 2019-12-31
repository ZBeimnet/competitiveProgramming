def dailyTemperatures(T):
    temp_length = len(T)
    result = [0] * temp_length

    for i in range(temp_length):
        for j in range(i + 1, temp_length):
            if T[j] > T[i]:
                result[i] = j - i
                break

    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))