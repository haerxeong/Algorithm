X, Y = map(int, input().split())
Z = 100 * Y // X
ans = 0
left, right = 0, X

if Z >= 99: ans  = -1

else:
    while left <= right:
        mid = (left + right) // 2
        temp = 100 * (Y + mid) // (X + mid)
        if temp != Z:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1 

print(ans)