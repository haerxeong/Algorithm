from collections import deque

n = int(input())  # 동기 수
m = int(input())  # 친구 관계 수

graph = [[] for _ in range(n + 1)]

# 친구 관계 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True

q = deque([(1, 0)])  # (현재 사람, 깊이)
invite = 0

while q:
    cur, depth = q.popleft()

    # 친구의 친구까지만 탐색
    if depth >= 2:
        continue

    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            invite += 1
            q.append((nxt, depth + 1))

print(invite)