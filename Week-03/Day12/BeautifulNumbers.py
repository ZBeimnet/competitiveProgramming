def beautiful_number(num, num_length):
    pos_array = [0] * num_length
    result = ""

    # populating the position array
    for i in range(num_length):
        pos_array[int(num[i])-1] = i + 1

    minimum = pos_array[0]
    maximum = pos_array[0]
    # checking beautifulness of the numbers
    for i in range(0, num_length):
        if maximum - minimum == i:
            result += "1"
        else:
            result += "0"
        if i != num_length - 1:
            if pos_array[i+1] > maximum:
                maximum = pos_array[i+1]
            if pos_array[i+1] < minimum:
                minimum = pos_array[i+1]

    return result


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        num_length = eval(input())
        test = input()
        print(beautiful_number(test.split(), num_length))


main()
