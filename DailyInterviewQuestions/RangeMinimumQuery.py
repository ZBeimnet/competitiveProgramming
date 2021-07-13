def find_min(left, right, m, log):
    length = right - left + 1
    k = log[length]
    return min(m[left][k], m[right-(1<<k)+1][k])

def main():
    n = int(input())
    nums = input().split()
    nums = [int(x) for x in nums]
    
    log = [0] * (n + 1)
    for i in range(2, len(log)):
        log[i] = log[i // 2] + 1
    
    m = [[x for x in range(log[n])] for _ in range(n)]
    for k in range(1, log[n]):
        for i in range(n - (1<<k) + 1):
            m[i][k] = min(m[i][k-1], m[i+(1<<(k-1))][k-1])
    
    queries = int(input())
    for _ in range(queries):
        query = input().split()
        left, right = int(query[0]), int(query[1])
        print(find_min(left, right, m, log))




    

if __name__ == "__main__":
    main()

