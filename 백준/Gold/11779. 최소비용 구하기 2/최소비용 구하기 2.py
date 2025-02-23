import sys
import heapq

def dijkstra(n, graph, start, end):
    INF = float('inf')
    distance = [INF] * (n + 1)
    prev = [-1] * (n + 1)  # 경로 추적을 위한 배열
    distance[start] = 0

    pq = [(0, start)]  # (비용, 도시)

    while pq:
        cost, now = heapq.heappop(pq)

        if distance[now] < cost:
            continue
        
        for next_node, next_cost in graph[now]:
            new_cost = cost + next_cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                prev[next_node] = now  # 경로 저장
                heapq.heappush(pq, (new_cost, next_node))

    return distance, prev

def reconstruct_path(prev, start, end):
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()
    return path

def solve():
    # 입력 처리
    n = int(sys.stdin.readline())  # 도시 수
    m = int(sys.stdin.readline())  # 버스 수
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, cost = map(int, sys.stdin.readline().split())
        graph[u].append((v, cost))

    start, end = map(int, sys.stdin.readline().split())

    # 다익스트라 실행
    distance, prev = dijkstra(n, graph, start, end)

    # 경로 복원
    path = reconstruct_path(prev, start, end)

    # 결과 출력
    print(distance[end])  # 최소 비용
    print(len(path))  # 경로에 포함된 도시 개수
    print(*path)  # 경로 출력

# 실행
solve()