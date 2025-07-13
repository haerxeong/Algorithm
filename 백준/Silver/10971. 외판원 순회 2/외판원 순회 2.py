import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')

for path in permutations(range(N)):
    valid = True
    cost = 0
    for i in range(N - 1):
        if W[path[i]][path[i + 1]] == 0:
            valid = False
            break
        cost += W[path[i]][path[i + 1]]

    # 마지막 도시 → 출발 도시
    if valid and W[path[-1]][path[0]] != 0:
        cost += W[path[-1]][path[0]]
        min_cost = min(min_cost, cost)

print(min_cost)