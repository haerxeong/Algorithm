import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())

g = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def bfs(start, target):
    q = deque([start])
    dist = [-1] * (N + 1)
    dist[start] = 0

    while q:
        x = q.popleft()
        if x == target:
            return dist[x]

        # 텔레포트 이웃
        for y in g[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)

        # x-1, x+1 이웃
        if x - 1 >= 1 and dist[x - 1] == -1:
            dist[x - 1] = dist[x] + 1
            q.append(x - 1)
        if x + 1 <= N and dist[x + 1] == -1:
            dist[x + 1] = dist[x] + 1
            q.append(x + 1)

    return -1  # 문제 조건상 도달 가능하므로 보통 여기 오지 않음

print(bfs(S, E))