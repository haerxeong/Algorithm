N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # if j == 0: dp[i][j] = li[i][j]
        # else: dp[i][j] = dp[i][j - 1] + li[i][j]
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + li[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # sum = 0

    # for i in range(x1 - 1, x2):
    #     if y1 == 1: sum += dp[i][y2 - 1]
    #     else: sum += (dp[i][y2 - 1] - dp[i][y1 - 2])
        
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])