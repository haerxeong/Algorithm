for _ in range(int(input())):
    N = int(input())
    dp = [[0, 0] for _ in range(N + 1)]
    for i in range(N + 1):
        if i == 0 or i == 1: dp[i][i] = 1
        else:
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

    print(dp[N][0], dp[N][1])