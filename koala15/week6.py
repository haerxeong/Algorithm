#BFS, DFS

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

#2644번: 촌수 계산 #pass
from collections import deque

n = int(input())
target = [input()]
li = [i for i in range(n + 1)]

for _ in range(int(input())):
    li[int(input())].append(int(input()))