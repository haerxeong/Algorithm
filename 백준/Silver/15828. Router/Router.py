from collections import deque

N = int(input())
Q = deque()

while True:
    info = int(input())
    if info == -1: break

    if info:
        if len(Q) < N:
            Q.append(info)
    else:
        Q.popleft()

print(' '.join(map(str, Q)) if Q else "empty")