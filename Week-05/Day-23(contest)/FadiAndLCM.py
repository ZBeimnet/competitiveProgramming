import math


def fadi_and_lcm(x):
    minn = [1, x]
    for i in range(2, math.ceil(math.sqrt(x))):
        if x % i == 0:
            if lcm(i, x//i) == x:
                if max(i, x//i) < max(minn[0], minn[1]):
                    minn = [i, x//i]

    return str(minn[0]) + " " + str(minn[1])


def gcd(num1, num2):
    if num1 == 0:
        return num2
    return gcd(num2 % num1, num1)


def lcm(a, b):
    return (a*b)//gcd(a, b)


def main():
    num = input()
    print(fadi_and_lcm(int(num)))


main()
