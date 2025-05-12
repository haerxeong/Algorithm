import heapq

N, M = map(int, input().split()) # 엣지, 노드
visibility = list(map(int, input().split()))

INF = float("inf") # 혹은 int(1e9)
graph = [[] for _ in range(N)]
distance = [INF] * N

for _ in range(M):
    a, b, t = map(int, input().split()) # a <-> b의 가중치 t
    graph[a].append((b, t))
    graph[b].append((a, t))

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0)) # (거리, 노드번호)
    distance[0] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if now == N - 1:
            return distance[now]
        if distance[now] < dist or visibility[now]:
            continue
        for neighbor, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(q, (new_cost, neighbor))

    return -1

print(dijkstra())