N = int(input())
arr = [float(input()) for _ in range(N)]
dp = arr.copy()

for i in range(1, N):
    dp[i] = max(dp[i - 1] * arr[i], arr[i])

print(f"{max(dp):.3f}")