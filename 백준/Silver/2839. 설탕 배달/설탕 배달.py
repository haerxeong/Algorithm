N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    if i == 3 or i == 5: dp[i] = 1
    elif dp[i - 3] and dp[i - 5]: dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    elif dp[i - 3]: dp[i] = dp[i - 3] + 1
    elif dp[i - 5]: dp[i] = dp[i - 5] + 1

print(dp[N] if dp[N] else -1)