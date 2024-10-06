for _ in range(int(input())):
    n = int(input())
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        if i == 2: dp[i] = dp[i - 1] + 1
        elif i == 3: dp[i] = dp[i - 1] + dp[i - 2] + 1
        else: dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[n])