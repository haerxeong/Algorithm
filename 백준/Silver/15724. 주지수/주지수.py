import sys

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(sys.stdin.readline())

# 누적 합 배열 생성
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = grid[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# 질의 처리 및 출력
result = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    result.append(str(answer))

sys.stdout.write("\n".join(result) + "\n")  # 빠른 출력