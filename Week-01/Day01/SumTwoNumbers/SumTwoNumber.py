# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:00:12 2019

@author: Beimnet.Z
"""

# Global Variable
carry = 0


def calculate_sum(first_number, second_number):
    global carry
    first_number_length = len(first_number)
    second_number_length = len(second_number)
    result = ""

    if first_number_length > second_number_length:
        length = first_number_length
        difference = first_number_length - second_number_length
        second_number = make_number_length_equal(difference, second_number)
    elif first_number_length == second_number_length:
        length = first_number_length
    else:
        length = second_number_length
        difference = second_number_length - first_number_length
        first_number = make_number_length_equal(difference, first_number)

    for index in range(length - 1, -1, -1):
        sum_at_index = int(first_number[index]) + int(second_number[index]) + carry
        result = str(check_sum_at_index(index, sum_at_index)) + result

    return result


def make_number_length_equal(difference, number):
    return "0" * difference + number


def check_sum_at_index(index, sum_at_index):
    global carry
    if sum_at_index > 9 and index != 0:
        carry = sum_at_index // 10
        return sum_at_index % 10
    carry = 0
    return sum_at_index


def is_smaller(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 < n2:
        return True
    if n2 < n1:
        return False

    for i in range(n1):
        if str1[i] < str2[i]:
            return True
        elif str1[i] > str2[i]:
            return False

    return False


def calculate_difference(str1, str2):
    if is_smaller(str1, str2):
        temp = str1
        str1 = str2
        str2 = temp

    str3 = ""

    n1 = len(str1)
    n2 = len(str2)

    str1 = str1[::-1]
    str2 = str2[::-1]

    carry_for_difference = 0

    for i in range(n2):
        sub = ((ord(str1[i]) - ord('0')) - (ord(str2[i]) - ord('0')) - carry_for_difference)

        if sub < 0:
            sub = sub + 10
            carry_for_difference = 1
        else:
            carry_for_difference = 0

        str3 = str3 + str(sub)

    for i in range(n2, n1):
        sub = ((ord(str1[i]) - ord('0')) - carry_for_difference)

        if sub < 0:
            sub = sub + 10
            carry_for_difference = 1
        else:
            carry_for_difference = 0

        str3 = str3 + str(sub)

    str3 = str3[::-1]

    return str3


def check_input(num1, num2):
    if num1[0] == "-" and num2[0] == "-":
        return "BOTH_-VE"
    elif num1[0] == "-":
        return "NUM_ONE_-VE"
    elif num2[0] == "-":
        return "NUM_TWO_-VE"
    else:
        return "BOTH_+VE"


def main():
    num1 = input("Enter Num1: ")
    num2 = input("Enter Num2: ")
    verdict = check_input(num1, num2)
    result = "Result: "

    if verdict == "BOTH_-VE":
        result = result + "-" + calculate_sum(num1[1:], num2[1:])
    elif verdict == "NUM_ONE_-VE":
        result = result + calculate_difference(num1[1:], num2)
    elif verdict == "NUM_TWO_-VE":
        result = result + calculate_difference(num1, num2[1:])
    else:
        result = result + calculate_sum(num1, num2)

    print(result)


# main()
