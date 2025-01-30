N, M = map(int, input().split()) # 총 강의 수, 블루레이 개수
videos = list(map(int, input().split()))

left, right = max(videos), max(videos) * N
ans = 0

while left <= right:
    mid = (left + right) // 2  # 블루레이 크기
    
    blurays = 1 # 블루레이 크기가 mid일 때의 블루레이 개수
    temp = 0 # 블루레이 하나의 크기

    for i in range(N):
        if temp + videos[i] <= mid:
            temp += videos[i]
        else:
            blurays += 1
            temp = videos[i]

    if blurays <= M:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)