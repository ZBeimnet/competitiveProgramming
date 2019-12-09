def beautiful_contest(results, length):
    medalists = ""

    # finding the exact start point of non-medalist
    middle_point = length // 2
    end_point = middle_point
    for i in range(middle_point-1, -1, -1):
        if results[middle_point] == results[i]:
            end_point = i
        else:
            break

    gold = silver = bronze = 0

    # counting gold medalists
    for i in range(end_point):
        gold += 1
        if results[i+1] != results[i]:
            break

    # counting silver medalists
    for i in range(gold, end_point):
        silver += 1
        if results[i+1] != results[i] and silver > gold:
            break

    # counting bronze medalists
    for i in range(gold + silver, end_point):
        bronze += 1

    # checking for the rules
    if gold < 0 or silver < 0 or bronze < 0:
        medalists = "0 0 0"
    elif gold >= silver or gold >= bronze:
        medalists = "0 0 0"
    else:
        medalists = str(gold) + " " + str(silver) + " " + str(bronze)

    return medalists


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        length = eval(input())
        test = input()
        print(beautiful_contest(test.split(), length))


main()
