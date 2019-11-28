import math


def calculate_division(number, divisor):
    ans = ""

    idx = 0
    temp = ord(number[idx]) - ord('0')
    while temp < divisor:
        temp = (temp * 10 + ord(number[idx + 1]) - ord('0'))
        idx += 1

    idx += 1

    while (len(number)) > idx:
        ans += chr(math.floor(temp // divisor) + ord('0'))

        temp = ((temp % divisor) * 10 + ord(number[idx]) - ord('0'))
        idx += 1

    ans += chr(math.floor(temp // divisor) + ord('0'))

    if len(ans) == 0:
        return "0"

    return ans


def main():
    number = input("Enter number: ")
    divider = eval(input("Enter divisor: "))

    print(calculate_division(number, divider))


main()
