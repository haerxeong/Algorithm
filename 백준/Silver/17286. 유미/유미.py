import sys
import math
import itertools

input = sys.stdin.readline

# 입력
yumi = tuple(map(int, input().split()))
people = [tuple(map(int, input().split())) for _ in range(3)]

def dist(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

ans = float("inf")

# 모든 방문 순서 시도
for order in itertools.permutations(people):
    d = dist(yumi, order[0]) + dist(order[0], order[1]) + dist(order[1], order[2])
    ans = min(ans, d)

print(int(ans))  # 소수점 버림