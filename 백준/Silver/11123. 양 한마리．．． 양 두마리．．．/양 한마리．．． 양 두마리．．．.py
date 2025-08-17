import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]

    def bfs(sx, sy):
        q = deque([(sx, sy)])
        visited[sx][sy] = True
        while q:
            x, y = q.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):  # 상하좌우
                nx, ny = x+dx, y+dy
                if 0 <= nx < H and 0 <= ny < W:
                    if not visited[nx][ny] and grid[nx][ny] == '#':
                        visited[nx][ny] = True
                        q.append((nx, ny))

    cnt = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)