def max_gift(price, length, p):
    prices = price.split()
    prices = [int(prices[x]) for x in range(length)]
    prices_st = sorted(prices)

    if length <= 2:
        if p >= max(prices_st[0], prices_st[1]):
            return 2
        elif p >= prices_st[1]:
            return 1
        else:
            return 0

    gifts = 0
    for i in range(length-2):
        if p >= prices_st[i] + max(prices_st[i+1], prices_st[i+2]):
            p -= prices_st[i]
            gifts += 1
            continue
        elif p >= max(prices_st[i], prices_st[i+1]):
            p -= (prices_st[i] + prices_st[i+1])
            gifts += 2
            break
        elif p >= prices_st[i]:
            p -= prices_st[i]
            gifts += 1
            break

    if p >= max(prices_st[-1], prices_st[-2]):
        gifts += 2
    elif p >= prices_st[-2]:
        gifts += 1


    return gifts


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        n, p, k = input().split()
        prices = input()
        print(max_gift(prices, int(n), int(p)))


main()



