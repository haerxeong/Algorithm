input = __import__('sys').stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp_big, dp_small = [1] * N, [1] * N

for i in range(1, N):
    if arr[i - 1] <= arr[i]:
        dp_big[i] = dp_big[i - 1] + 1
    if arr[i - 1] >= arr[i]:
        dp_small[i] = dp_small[i - 1] + 1

print(max(max(dp_big), max(dp_small)))