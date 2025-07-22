N = int(input())
points = [int(input()) for _ in range(N)]
prev = points[-1]
ans = 0

for i in range(N - 2, -1, -1):
    while points[i] >= prev:
        points[i] -= 1
        ans += 1
    prev = points[i]

print(ans)