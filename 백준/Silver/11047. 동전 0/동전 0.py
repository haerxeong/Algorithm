N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

ans = 0
N -= 1

while K:
    if K < coins[N]:
        N -= 1
    else:
        K -= coins[N]
        ans += 1

print(ans)