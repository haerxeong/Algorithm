from collections import deque

def bfs(x, y):
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            if 0 <= x + dx < N and 0 <= y + dy < N:
                if not visited[x + dx][y + dy] and graph[x][y] == graph[x + dx][y + dy]:
                    visited[x + dx][y + dy] = True
                    queue.append((x + dx, y + dy))

N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
ans = [0, 0]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            ans[0] += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G': graph[i][j] = 'R'

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            ans[1] += 1

print(*ans)