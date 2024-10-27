N, M = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)
ans = 0

while left <= right:
    temp = 0
    mid = (left + right) // 2
    
    # 현재 mid 높이로 잘랐을 때 얻는 나무 길이 계산
    for t in trees:
        if t > mid:
            temp += t - mid

    # 필요한 나무 길이와 비교하여 left 또는 right 조정
    if temp >= M:
        ans = mid  # 최대 높이를 갱신
        left = mid + 1
    else:
        right = mid - 1

print(ans)