n = int(input())
left, right = 0, n

while left <= right:
    mid = (left + right) // 2
    val = mid ** 2

    if n <= val:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)