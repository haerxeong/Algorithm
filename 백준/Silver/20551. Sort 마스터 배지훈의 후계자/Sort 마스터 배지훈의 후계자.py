N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = sorted(A)

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

for _ in range(M):
    q = int(input())
    idx = lower_bound(B, q)
    if idx < N and B[idx] == q:
        print(idx)
    else:
        print(-1)