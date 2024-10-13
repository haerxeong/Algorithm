# 3주차 모의 테스트
from collections import deque
for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    cnt = 0
    while q:
        maxq = max(q)
        front = q.popleft()
        m -= 1

        if maxq == front:
            cnt += 1
            if m < 0: print(cnt); break
        else: 
            q.append(front)
            if m < 0: 
                m = len(q) - 1