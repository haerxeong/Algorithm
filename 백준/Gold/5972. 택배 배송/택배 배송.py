import sys
import heapq

# 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 그래프 저장 (인접 리스트)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))  # 양방향 길

# 다익스트라 알고리즘
def dijkstra(start):
    INF = float('inf')
    dist = [INF] * (N + 1)  # 거리 배열
    dist[start] = 0
    pq = [(0, start)]  # (비용, 현재 노드)

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > dist[node]:  # 이미 최소 비용이면 스킵
            continue

        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost

            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

    return dist[N]

# 시작점 1에서 다익스트라 실행
print(dijkstra(1))