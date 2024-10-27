N = int(input())
arr1 = sorted(list(map(int, input().split())))
M = int(input())
arr2 = list(map(int, input().split()))
ans = ['0'] * M

for i in range(M):
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if arr1[mid] == arr2[i]:
            ans[i] = '1'
            break
        elif arr1[mid] > arr2[i]:
            right = mid - 1
        else:
            left = mid + 1

print(' '.join(ans))
