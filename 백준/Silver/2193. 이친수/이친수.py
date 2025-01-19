N = int(input())
dp = [[0, 0] for _ in range(N + 1)]  # 0: 끝자리가 0인 이친수 개수, 1: 끝 자리가 1인 이친수 개수

for i in range(1, N + 1):
    if i == 1:
        dp[i][1] = 1  # 1자리 이친수는 1 하나뿐
    else:
        dp[i][0] = dp[i-1][0] + dp[i-1][1]  # 이전 자리가 0이든 1이든 끝에 0을 붙일 수 있음
        dp[i][1] = dp[i-1][0]  # 이전 자리가 0일 때만 끝에 1을 붙일 수 있음

print(sum(dp[N]))
