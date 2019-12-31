def build_garland(lamp):
    lamps = [int(lamp[x]) for x in range(len(lamp))]
    lamps.append(0)
    previous_index = 5
    count = lamps[0] + lamps[1] + lamps[2]
    while count > 0:
        max_index = 3
        for i in range(len(lamps)):
            if lamps[max_index] < lamps[i] \
                    and previous_index != i:
                max_index = i

        if max_index == 3:
            return "No"
        else:
            lamps[max_index] -= 1
            previous_index = max_index
            count -= 1

    return "Yes"


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        lamps = input()
        print(build_garland(lamps.split()))


main()
