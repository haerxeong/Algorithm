from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    country = [[x, y]]
    total = A[x][y]

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and [nx, ny] in graph[x][y]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    country.append([nx, ny])
                    total += A[nx][ny]

    for r, c in country: A[r][c] = total // len(country)

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
days = 0
is_open = True

while is_open:
    graph = [[[] * N for _ in range(N)] for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 국경선 열기
    is_open = False

    for x in range(N):
        for y in range(N):
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if L <= abs(A[x][y] - A[nx][ny]) <= R:
                        is_open = True
                        graph[x][y].append([nx, ny])

    if not is_open:
        break

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)

    days += 1

print(days)