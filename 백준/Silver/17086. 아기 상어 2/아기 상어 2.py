from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 8방향 이동
dirs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

# 모든 상어(1)의 위치를 큐에 담는다
q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i, j))

# BFS 시작
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            board[nx][ny] = board[x][y] + 1
            q.append((nx, ny))

# 안전 거리의 최댓값 = (가장 큰 값 - 1)
max_dist = max(map(max, board)) - 1
print(max_dist)