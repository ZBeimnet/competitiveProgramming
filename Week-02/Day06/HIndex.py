def h_index(citations):
    citations.sort()
    N = len(citations)
    h = 0

    for i in range(N):
        if citations[i] >= N-i:
            h = N-i
            break

    return h


print(h_index([3, 0, 6, 1, 5]))
