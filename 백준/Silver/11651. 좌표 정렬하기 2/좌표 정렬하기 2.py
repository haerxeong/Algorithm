from heapq import heappush, heappop
hq = []

for _ in range(int(input())):
    x, y = map(int, input().split())
    heappush(hq, [y, x])

while hq:
    y, x = heappop(hq)
    print(x, y)