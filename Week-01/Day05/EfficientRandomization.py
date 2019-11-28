import random


def randomize(n):
    # initializing the list with 0
    li = [0] * n

    # populating with ordered number
    for i in range(n):
        li[i] = i

    # randomizing the list (finding element at random_index and swapping it with the current element)
    for i in range(n):
        random_index = random.randrange(i, n)
        li[i], li[random_index] = li[random_index], li[i]

    return li


print(randomize(1000))
