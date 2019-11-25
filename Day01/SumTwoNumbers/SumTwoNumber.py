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


def main():
    num1 = input("Enter Num1: ")
    num2 = input("Enter Num2: ")
    result = calculate_sum(num1, num2)
    print("Result: " + result)


main()
