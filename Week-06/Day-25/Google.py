# import sys
#
#
# def solution(T):
#     result = list(T)
#
#     if T[0] == '?':
#         if int(T[1]) <= 3:
#             result[0] = '2'
#         else:
#             result[0] = '1'
#
#     if T[1] == '?':
#         if T[0] == '2':
#             result[1] = '3'
#         else:
#             result[1] = '9'
#
#     if T[3] == '?':
#         result[3] = '5'
#
#     if T[4] == '?':
#         result[4] = '9'
#
#     return ''.join(result)
#
#
# # print(solution('2?:?8'))
#
#
#
# def solution2(A):
#     booking_count = [[0 for _ in range(26)] for _ in range(10)]
#     max_booked = [0, 0]
#
#     # counting how many times rooms are booked
#     for booked in A:
#         if booked[0] == '+':
#             booking_count[int(booked[1])][ord(booked[2].lower()) - 97] += 1
#
#     # finding the maximum booked room
#     for i in range(len(booking_count)):
#         for j in range(len(booking_count[0])):
#             if booking_count[i][j] > booking_count[max_booked[0]][max_booked[1]]:
#                 max_booked = [i, j]
#
#     return str(max_booked[0]) + chr(max_booked[1] + 97).upper()

# import heapq
#
#
# class Marketplace:
#     def __init__(self):
#         self.offers_to_buy = []
#         self.offers_to_sell = []
#
#     def buy(self, price):
#         if not self.offers_to_sell or self.offers_to_sell[0] > price:
#             heapq.heappush(self.offers_to_buy, -1 * price)
#             return -1
#         return heapq.heappop(self.offers_to_sell)
#
#     def sell(self, price):
#         if not self.offers_to_buy or abs(self.offers_to_buy[0]) < price:
#             heapq.heappush(self.offers_to_sell, price)
#             return -1
#         return abs(heapq.heappop(self.offers_to_buy))
#
#
# test = Marketplace()
# print(test.buy(10))
# print(test.buy(30))
# print(test.sell(13))
# print(test.sell(12))
# print(test.buy(20))


def largest_table(grid):
    result = []
    for i in range(len(grid)):
        result.append([])
        for j in range(len(grid[0])):
            result[i].append(None)

    maxx = float("-inf")

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            prevLeft = j - 1
            prevTop = i - 1

            x = y = 0
            if grid[i][j] == 1:
                if prevLeft >= 0:
                    y = result[i][prevLeft][1] + 1
                else:
                    y = 1
                if prevTop >= 0:
                    x = result[prevTop][j][0] + 1
                else:
                    x = 1

            result[i][j] = (x, y)
            if x * y > maxx:
                maxx = x * y
    return maxx


# print(largest_table([ [0,1,1,1,0,0],
#   [0,1,1,0,1,1],
#   [0,1,1,0,1,1],
#   [0,1,1,0,1,1]  ]))


#  [task_no, priorty] → [[1, 10], [2, 10], [3, 6], [4, 15]], k = 2
# [[4, 15], [1, 10]]

def k_priority(tasks, k):
    count_priority = [[] for _ in range(101)]
    for i in range(len(tasks)):
        count_priority[tasks[i][1]].append(tasks[i])

    result = []
    count = 0
    for i in range(len(count_priority) - 1, -1, -1):
        for j in range(len(count_priority[i])):
            if count >= k:
                break
            result.append(count_priority[i][j])
            count += 1

    return result


# print(k_priority([[1, 10], [2, 10], [3, 6], [4, 15]], 3))

def max_sum(grid):
    if not grid:
        return

    maximum = float("-inf")

    # sum the first row
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]

    # sum the first column
    for i in range(1, len(grid)):
        grid[i][0] += grid[i-1][0]

    # find sum of rectangle b/n each point and top left corner
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]


