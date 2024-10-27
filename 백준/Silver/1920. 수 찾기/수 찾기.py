def binary_search(n):
    left, right = 0, N - 1
    while left <= right < N:
        mid = (left + right) // 2
        if A[mid] == n:
            return 1
        elif A[mid] > n:
            right = mid - 1
        else:
            left = mid + 1
    return 0

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
li = list(map(int, input().split()))

for i in li:
    print(binary_search(i))