for _ in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    prefix = max_sum = X[0]

    for i in range(1, N):
        prefix = max(X[i], prefix + X[i])
        max_sum = max(max_sum, prefix)

    print(max_sum)