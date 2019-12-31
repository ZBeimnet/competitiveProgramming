import math


def a_and_b(nums):
    nums = nums.split()
    a, b = int(nums[0]), int(nums[1])

    if a == b:
        return 0

    if a > b:
        a, b = b, a

    diff = b - a
    count = 1
    while True:
        num = 1 + 8 * diff
        root = math.sqrt(num)
        if int(root + 0.5) ** 2 == num:
            break
        else:
            diff -= count
        count += 1

    if count == 1:
        return int((root - 1)//2)
    else:
        return int((root - 1) // 2)


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        nums = input()
        print(a_and_b(nums))


main()
