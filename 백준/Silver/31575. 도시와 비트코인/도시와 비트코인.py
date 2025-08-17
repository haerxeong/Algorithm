import sys
input = sys.stdin.readline

N, M = map(int, input().split())   # N: 가로(열), M: 세로(행)
grid = [list(map(int, input().split())) for _ in range(M)]

reachable = [[False]*N for _ in range(M)]
reachable[0][0] = (grid[0][0] == 1)

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            continue
        if i == 0 and j == 0:
            continue
        up  = reachable[i-1][j] if i > 0 else False
        left = reachable[i][j-1] if j > 0 else False
        reachable[i][j] = up or left

print("Yes" if reachable[M-1][N-1] else "No")