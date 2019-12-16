def find_optimal_distance(distances):
    distance = distances.split()
    distance = [int(distance[i]) for i in range(len(distance))]
    distance = sorted(distance)

    if are_equal(distance):
        return 0
    elif distance[0] == distance[1]:
        distance[2] -= 1
        if are_equal(distance):
            return 0
        else:
            distance[0] += 1
            distance[1] += 1
    elif distance[1] == distance[2]:
        distance[0] += 1
        if are_equal(distance):
            return 0
        else:
            distance[1] -= 1
            distance[2] -= 1
    else:
        distance[0] += 1
        distance[2] -= 1

    optimal_distance = abs(distance[0] - distance[1]) + abs(distance[1] - distance[2]) + abs(distance[0] - distance[2])

    return optimal_distance


def are_equal(distance):
    if distance[0] == distance[1] and distance[1] == distance[2] \
            and distance[0] == distance[2]:
        return True
    return False


def main():
    tests = eval(input())
    for i in range(tests):
        test = input()
        print(find_optimal_distance(test))


main()