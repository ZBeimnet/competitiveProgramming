def find_possibilities(commands, number_of_commands):
    left_count = 0
    right_count = 0

    for i in range(number_of_commands):
        if commands[i] == "L":
            left_count += 1
        else:
            right_count += 1

    return left_count + right_count + 1


def main():
    num_of_commands = eval(input())
    commands = input()
    print(find_possibilities(commands, num_of_commands))


main()


