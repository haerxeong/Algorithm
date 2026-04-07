from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
cnt, year = 0, 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j]: # 방문한 적 없고 빙산이면
            bfs(i, j)
            cnt += 1

while cnt < 2: # 아직 두덩어리 이상이 아닐 때
    year += 1
    new_graph = [row[:] for row in graph]

    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                for di, dj in zip(dxs, dys):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and not graph[ni][nj] and new_graph[i][j]: # 인접한 바다인 경우 + 음수 방지
                        new_graph[i][j] -= 1 # 빙산 높이 감소

    graph = new_graph

    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j]:
                bfs(i, j)
                cnt += 1

    if not cnt:
        year = 0
        break

print(year)