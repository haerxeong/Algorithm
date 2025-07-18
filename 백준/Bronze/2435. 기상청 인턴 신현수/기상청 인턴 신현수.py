N, K = map(int, input().split())
temp = list(map(int, input().split()))
prefix = [0] * N

for i in range(N):
    if i < K: prefix[i] = prefix[i - 1] + temp[i]
    else: prefix[i] = prefix[i - 1] + temp[i] - temp[i - K]
    
print(max(prefix[K - 1::]))