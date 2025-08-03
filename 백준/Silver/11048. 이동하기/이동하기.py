import sys
input = sys.stdin.readline

N, M = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 위에서 오는 경우
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        # 왼쪽에서 오는 경우
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        # 대각선 위에서 오는 경우
        if i > 0 and j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        # 현재 위치의 사탕 추가
        dp[i][j] += candy[i][j]

print(dp[N-1][M-1])