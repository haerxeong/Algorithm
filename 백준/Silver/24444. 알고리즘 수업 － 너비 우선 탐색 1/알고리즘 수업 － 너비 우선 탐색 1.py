from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    order[start] = 1  # 시작 정점의 방문 순서는 1
    cnt = 2  # 방문 순서 카운트

    while queue:
        node = queue.popleft()
        for neighbor in sorted(graph[node]):  # **오름차순 정렬 후 방문**
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                order[neighbor] = cnt
                cnt += 1

# 입력 받기
N, M, R = map(int, input().split())  # 정점 수, 간선 수, 시작 정점
graph = {i: [] for i in range(1, N + 1)}  # **인접 리스트 생성**

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부 및 방문 순서 배열 초기화
visited = [False] * (N + 1)
order = [0] * (N + 1)  # 각 정점의 방문 순서를 저장

bfs(R)  # BFS 실행

# 방문 순서 출력
for i in range(1, N + 1):
    print(order[i])