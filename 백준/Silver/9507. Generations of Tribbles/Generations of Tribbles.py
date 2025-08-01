dp = [1] * 68

for i in range(2, 68):
    if i == 2: dp[i] = 2
    elif i == 3: dp[i] = 4
    else: dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

for _ in range(int(input())): print(dp[int(input())])