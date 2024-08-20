#1260: DFS와 BFS
'''from collections import deque

def dfs(start):
    visited[start] = 1
    print(start, end = ' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        x = q.popleft()
        print(x, end = ' ')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n + 1):
    graph[i].sort()

dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)'''
    

#2644: 촌수계산
'''from collections import deque

n = int(input())
q = deque([9])
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    q[x].append(y)

def bfs()'''

#13023: ABCDE
'''n, m = map(int, input().split())

def dfs(x):
    pass

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)'''

#2468: 안전 영역
'''n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
'''
#7576: 토마토
'''from collections import deque

m, n = map(int, input().split())
arr = [map(int, input().split()) for _ in range(n)]

cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    '''

#11725: 트리의 부모 찾기
'''input = __import__('sys').stdin.readline
from collections import deque

n = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = [0] * (n + 1)
q = deque([1])

def bfs():
    while q:
        x = q.popleft()
        for i in arr[x]:
            if not ans[i]:
                ans[i] = x
                q.append(i)
bfs()
print('\n'.join(map(str, ans[2:])))'''
########
from collections import deque
input = __import__('sys').stdin.readline

n = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = [0] * (n + 1)
q = deque([1])

def bfs(q):
    while q:
        x = q.popleft()
        for i in arr[x]:
            if ans[i] == 0:
                ans[i] = x
                q.append(i)

bfs(q)
print('\n'.join(map(str, ans[2:])))

'''input = __import__('sys').stdin.readline
from collections import deque

N = int(input())
arr = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in arr[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
res = ans[2:]
for x in res:
    print(x)'''