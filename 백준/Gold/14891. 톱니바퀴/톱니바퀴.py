from collections import deque

def rotate(num, direction):
    if direction == 1: # 오른쪽
        chain[num].appendleft(chain[num].pop())
    else: chain[num].append(chain[num].popleft())

    if num > 0: # 0이 아니면
        if arr[num - 1][0] != arr[num - 1][1]:
            arr[num - 1][0], arr[num - 1][1] = 0, 0
            rotate(num - 1, -direction)
    if num < 3: # 3이 아니면
        if arr[num][0] != arr[num][1]:
            arr[num][0], arr[num][1] = 0, 0
            rotate(num + 1, -direction)

chain = [deque(input()) for _ in range(4)] # 0이 N극 1이 S극 / 0번째가 12시 방향, 2번째가 오른쪽, 6번째가 왼쪽

for _ in range(int(input())):
    num, direction = map(int, input().split()) # 1이 오른쪽 -1 왼쪽
    arr = [[chain[0][2], chain[1][6]], [chain[1][2], chain[2][6]], [chain[2][2], chain[3][6]]]

    rotate(num - 1, direction)

ans = 0
for i in range(4):
    if int(chain[i][0]): ans += 2**i # S극(1)이면 집계

print(ans)