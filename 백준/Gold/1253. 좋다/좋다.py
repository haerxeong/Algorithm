N = int(input())
A = sorted(list(map(int, input().split())))
ans = 0

for i in range(N):
    left, right = 0, N - 1

    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        else:
            if A[left] + A[right] == A[i]:
                ans += 1
                break
            elif A[left] + A[right] < A[i]:
                left += 1
            else:
                right -= 1

print(ans)