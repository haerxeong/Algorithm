import heapq

N = int(input())
q = []

for i in range(N):
    age, name = input().split()
    heapq.heappush(q, (int(age), i, name))

while q:
    age, order, name = heapq.heappop(q)
    print(age, name)