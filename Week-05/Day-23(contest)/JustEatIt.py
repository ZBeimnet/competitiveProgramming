def is_yasser_happy(cakes, no_of_cakes):
    cakes = [int(cakes[x]) for x in range(no_of_cakes)]
    yasser_total = sum(cakes)

    for i in range(no_of_cakes - 1):
        current_adel_sum = max(cakes[i], sum(cakes[:i+1]))
        if current_adel_sum >= yasser_total:
            return "NO"

    if cakes[no_of_cakes-1] >= yasser_total:
        return "NO"

    return "YES"


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        no_of_cakes = eval(input())
        cakes = input()
        print(is_yasser_happy(cakes.split(), no_of_cakes))


main()

