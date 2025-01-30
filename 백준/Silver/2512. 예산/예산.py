N = int(input()) # 지방 수
li = list(map(int, input().split()))
M = int(input()) # 총 예산

left, right = 0, max(li)
ans = 0

while left <= right:
    mid = (left + right) // 2
    temp = 0

    for i in range(N):
        if li[i] <= mid:
            temp += li[i]
        else:
            temp += mid
    
    if temp <= M:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)