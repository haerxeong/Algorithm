from collections import deque

def BFS(x, y, rain):
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            if 0 <= x + dx < N and 0 <= y + dy < N:
                if not visited[x + dx][y + dy] and graph[x + dx][y + dy] > rain:
                    visited[x + dx][y + dy] = True
                    queue.append((x + dx, y + dy))

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

ans = [0] * 101

for k in range(101):
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > k:
                BFS(i, j, k)
                ans[k - 1] += 1

print(max(ans))