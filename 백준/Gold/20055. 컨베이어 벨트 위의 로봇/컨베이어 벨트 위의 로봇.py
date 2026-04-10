from collections import deque

N, K = map(int, input().split())
A = deque(map(int, input().split()))

level = 1
robots = [0] * N

while A.count(0) < K:
    # 벨트 + 로봇 회전
    A.appendleft(A.pop())
    for i in range(N - 2, -2, -1):
        robots[i + 1] = robots[i]
        if robots[-1]: robots[-1] = 0

    # 로봇 이동
    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and A[i + 1] > 0:
            robots[i + 1], robots[i] = 1, 0
            A[i + 1] -= 1

            if robots[-1]: robots[-1] = 0

    # 로봇 올리기
    if A[0] > 0:
        robots[0] = 1
        A[0] -= 1

    level += 1

print(level - 1)