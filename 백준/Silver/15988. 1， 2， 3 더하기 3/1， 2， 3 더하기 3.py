for _ in range(int(input())):
    n = int(input())
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1 or i == 2: dp[i] = i
        elif i == 3: dp[i] = 4
        else: dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

    print(dp[n])