#Dijkstra
#1753번: 최단경로
import heapq

V, E = map(int, input().split())    # 모든 정점은 1부터 V까지
K = int(input())    # 정점 시작 번호

graph = [[] * (V + 1) for _ in range(V + 1)]
min_dist = [float('inf') * (V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split()) # u -> v
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # (거리, 현재 노드)
    min_dist[start] = 0     # 시작 경로는 0

    while q:
        dist, now = heapq.heappop(q)
        if min_dist[now] > dist:   
            for i in graph[now]:    #i[0]은 갈 수 있는 노드, i[1]은 가중치
                temp = dist + i[1]  
                if temp < dist[i[0]]:
                    min_dist[i[0]] = temp
                    heapq.heappush(q, (temp, i[0])) # 연결된 노드 push

dijkstra(K)

for i in range(1, V + 1):
    print("INF" if min_dist[i] == float('inf') else min_dist[i])