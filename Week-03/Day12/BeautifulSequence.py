

def beautiful_sequence(numbers):
    str_count = numbers.split()
    num_count = [int(x) for x in range(len(str_count))]
    # num_count.append(-1)
    result = ""

    previous_number = -10
    index = 0
    counter = num_count[0] + num_count[1] + num_count[2] + num_count[3]
    while counter > 0:
        max_index = 0
        for i in range(1, len(num_count)):
            if num_count[i] > num_count[max_index]:
                if index == 0:
                    max_index = i
                else:
                    if abs(previous_number - i) == 1:
                        max_index = i
        if max_index == 4:
            return -1
        else:
            result = result + " " + str(max_index)
            previous_number = max_index
            num_count[max_index] -= 1
            counter -= 1
            index += 1

    return result


print(beautiful_sequence("1 1 1 1"))


