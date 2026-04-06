from collections import deque
from itertools import combinations as cb

def bfs():
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if test_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            if 0 <= x + dx < N and 0 <= y + dy < M and [x + dx, y + dy]:
                if test_graph[x + dx][y + dy] == 0:
                    test_graph[x + dx][y + dy] = 2
                    queue.append((x + dx, y + dy))

    cnt = 0
    for i in range(N): cnt += test_graph[i].count(0)

    return cnt

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)] # 0 빈칸, 1 벽, 2 바이러스
empty = []
ans = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0: empty.append([i, j])

for walls in cb(empty, 3):
    test_graph = [row[:] for row in graph]
    for x, y in walls:
        test_graph[x][y] = 1
    ans = max(bfs(), ans)

print(ans)