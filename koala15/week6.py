#BFS, DFS

#BFS
#2606번: 바이러스
from collections import deque

def bfs(x):
    Q = deque([x])
    cnt = 0
    visited[x] = True

    while Q:
        node = Q.popleft()
        #visited[node] = True

        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                Q.append(n)
                cnt += 1
    return cnt

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(1))

#1012번: 유기농 배추
from collections import deque

def BFS(x, y):
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]

    queue = deque([(x, y)]) #queue = deque((x, y))하면 unpack
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            if 0 <= x + dx < M and 0 <= y + dy < N:
                if not visited[x + dx][y + dy] and graph[x + dx][y + dy]:
                    visited[x + dx][y + dy] = True
                    queue.append((x + dx, y + dy))
    
for _ in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    ans = 0
    
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and graph[i][j]:
                BFS(i, j)
                ans += 1

    print(ans)

#2644번: 촌수 계산 #pass
from collections import deque

def BFS(x):
    queue = deque([x])
    
    while queue:
        node = queue.popleft()
        for n in node:
            if not check[n]:
                check[n] = check[node] + 1

n = int(input())
u, v = map(int, input().split())
graph = [[] for i in range(n + 1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

check = [[0] for _ in range(n)]
BFS(u)
print(check[v] if check[v] else -1)

#DFS
#2606번: 바이러스
def DFS(node):
    visited[node] = True

    for n in node:
        if not visited[n]:
            DFS(n)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

DFS(1)
print(visited.count(True))