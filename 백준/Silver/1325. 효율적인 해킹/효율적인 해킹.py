import sys
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    count = 1  # 자기 자신 포함
    
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                count += 1
    
    return count

# 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 그래프 초기화 (역방향 그래프)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)  # B → A (역방향 간선)

# 각 노드에서 BFS 실행하여 최대 해킹 가능한 노드 개수 계산
max_hack = 0
result = []

for i in range(1, N + 1):
    hack_count = bfs(i)
    
    if hack_count > max_hack:
        max_hack = hack_count
        result = [i]  # 새로운 최대값이 나오면 초기화
    elif hack_count == max_hack:
        result.append(i)  # 최대값과 동일하면 추가

# 오름차순 출력
print(*sorted(result))