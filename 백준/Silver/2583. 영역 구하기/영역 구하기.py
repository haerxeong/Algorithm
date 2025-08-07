from collections import deque

def BFS(x, y, area):
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            if 0 <= x + dx < M and 0 <= y + dy < N:
                if not visited[x + dx][y + dy] and not graph[x + dx][y + dy]:
                    visited[x + dx][y + dy] = True
                    area += 1
                    queue.append((x + dx, y + dy))
    return area

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]

for _ in range(K):
    a, b, c, d = map(int, input().split())

    for i in range(b, d):
        for j in range(a, c):
            graph[i][j] = 1

ans = []
visited = [[False] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if not visited[i][j] and not graph[i][j]:
            ans.append(BFS(i, j, 1))

print(len(ans))
print(* sorted(ans))