K, N = map(int, input().split())
lengths = sorted([int(input()) for _ in range(K)])
left, right = 1, lengths[-1]

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for length in lengths:
        cnt += length // mid
    
    if cnt >= N:
        maxLen = mid
        left = mid + 1
    
    else:
        right = mid - 1

print(maxLen)