def find_time(positions):
    positions = positions.split()
    point1 = int(positions[0])
    point2 = int(positions[1])
    base = int(positions[2])
    radius = int(positions[3])

    if point1 > point2:
        point1, point2 = point2, point1

    min_pt = base - radius
    max_pt = base + radius
    if min_pt <= point1 and max_pt >= point2:
        return 0
    elif (point1 <= min_pt <= point2) and (point1 <= max_pt <= point2):
        return (min_pt - point1) + (point2 - max_pt)
    elif (min_pt <= point1) and (point1 < max_pt < point2):
        return point2 - max_pt
    elif (max_pt >= point2) and (point1 < min_pt < point2):
        return min_pt - point1
    else:
        return point2 - point1


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        positions = input()
        print(find_time(positions))


main()
