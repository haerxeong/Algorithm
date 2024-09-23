# 완전탐색

#BOJ1051
def isSquare(n):
    for i in range(N - n):
        for j in range(M - n):
            if li[i][j] == li[i + n][j] == li[i][j + n] == li[i + n][j + n]:
                return n + 1
    return 1

N, M = map(int, input().split())
li = [[int(num) for num in input()] for _ in range(N)]
ans = 1

for n in range(1, min(N, M)):
    ans = max(ans, isSquare(n))

print(ans**2)