from collections import deque

N = int(input())
numbers = list(map(int, input().split()))

# 풍선 번호와 해당 숫자를 튜플로 저장
balloons = deque((i + 1, numbers[i]) for i in range(N))
result = []

while balloons:
    index, move = balloons.popleft()  # 풍선을 터뜨림
    result.append(index)

    if balloons:
        move = move - 1 if move > 0 else move  # 현재 풍선이 제거되었으므로 인덱스 조정
        balloons.rotate(-move)  # 양수면 오른쪽(시계 방향), 음수면 왼쪽(반시계 방향)

print(*result)