N = int(input())
P = [0] + list(map(int, input().split())) # 카드가 i개 들어있는 팩 가격이 P[i]
dp = P

for i in range(1, N + 1):
    if i == 1:
        dp[i] = P[i]
    else:
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], dp[j] + dp[i - j])

print(dp[N])