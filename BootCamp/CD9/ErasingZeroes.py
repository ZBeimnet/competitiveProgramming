def erase_zeroes(s):
    one_found = False
    one_index = 0
    no_zeroes = 0

    for i in range(len(s)):
        if s[i] == '1' and not one_found:
            one_index = i
            one_found = True
        elif s[i] == '1' and one_found:
            if i - one_index > 1:
                no_zeroes += i - one_index - 1
                one_index = i
            else:
                one_index = i
        breakpoint()

    return no_zeroes


def main():
    test = eval(input())
    for i in range(test):
        s = input()
        print(erase_zeroes(s))


main()
