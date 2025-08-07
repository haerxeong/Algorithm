from collections import deque

def BFS(x, y, area):
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if not visited[x + dx][y + dy] and graph[x + dx][y + dy]:
                    visited[x + dx][y + dy] = True
                    area += 1
                    queue.append((x + dx, y + dy))
    return area 

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = []
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            ans.append(BFS(i, j, 1))

if not ans: print("0\n0")
else: print(f"{len(ans)}\n{max(ans)}")