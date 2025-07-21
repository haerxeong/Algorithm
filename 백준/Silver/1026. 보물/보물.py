N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))
ans = 0

for i in range(N):
    ans += A[i] * B[i]

print(ans)