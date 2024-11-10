from collections import deque

def BFS(node):
    queue = deque([node])
    visited[node] = True

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True    # 까먹지말기!
                queue.append(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

connected = 0

for i in range(1, N + 1):
    if not visited[i]:
        BFS(i)
        connected += 1

print(connected)