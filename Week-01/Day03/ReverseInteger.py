
def reverse(x: int) -> int:
    if x >= 2 ** 31 - 1 or x <= -2 ** 31:
        return 0
    else:
        num_in_string = str(x)
        if x >= 0:
            reversed_string = num_in_string[::-1]
        else:
            temp = num_in_string[1:]
            temp2 = temp[::-1]
            reversed_string = "-" + temp2
        if int(reversed_string) >= 2 ** 31 - 1 or int(reversed_string) <= -2 ** 31:
            return 0
        else:
            return int(reversed_string)

