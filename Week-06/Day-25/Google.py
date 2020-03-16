import sys


def solution(T):
    result = list(T)

    if T[0] == '?':
        if int(T[1]) <= 3:
            result[0] = '2'
        else:
            result[0] = '1'

    if T[1] == '?':
        if T[0] == '2':
            result[1] = '3'
        else:
            result[1] = '9'

    if T[3] == '?':
        result[3] = '5'

    if T[4] == '?':
        result[4] = '9'

    return ''.join(result)


# print(solution('2?:?8'))



def solution2(A):
    booking_count = [[0 for _ in range(26)] for _ in range(10)]
    max_booked = [0, 0]

    # counting how many times rooms are booked
    for booked in A:
        if booked[0] == '+':
            booking_count[int(booked[1])][ord(booked[2].lower()) - 97] += 1

    # finding the maximum booked room
    for i in range(len(booking_count)):
        for j in range(len(booking_count[0])):
            if booking_count[i][j] > booking_count[max_booked[0]][max_booked[1]]:
                max_booked = [i, j]

    return str(max_booked[0]) + chr(max_booked[1] + 97).upper()