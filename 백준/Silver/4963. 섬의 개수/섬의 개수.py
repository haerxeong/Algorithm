import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    dxs = [0, 1, 1, 1, 0, -1, -1, -1]
    dys = [1, 1, 0, -1, -1, -1, 0, 1]

    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        if 0 <= x + dx < h and 0 <= y + dy < w:
            if not visited[x + dx][y + dy] and graph[x + dx][y + dy]:
                DFS(x + dx, y + dy)

while True:
    w, h = map(int, input().split())
    if w == h == 0: break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    ans = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]:
                DFS(i, j)
                ans += 1

    print(ans)