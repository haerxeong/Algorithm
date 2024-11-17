def sol(s, e):
    from collections import defaultdict
    import heapq
    updated_w = defaultdict(lambda : float('inf'))
    updated_w[s] = 0
    
    will_visit = [(updated_w[s],s)]

    while will_visit:
        vw, vn = heapq.heappop(will_visit)

        if updated_w[vn] < vw : continue 

        for adjn, adjw in graph[vn]:
            if vw + adjw < updated_w[adjn]: 
                updated_w[adjn] = vw + adjw
                heapq.heappush(will_visit, (vw + adjw, adjn))
    return updated_w[e]

import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
start, end = map(int, input().split())

print(sol(start,end))