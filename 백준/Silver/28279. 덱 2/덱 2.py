import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
D = deque()
ans = []

for _ in range(N):
    command = list(map(int, input().split()))

    if command[0] == 1:
        D.appendleft(command[1])
    elif command[0] == 2:
        D.append(command[1])
    elif command[0] == 3:
        ans.append(str(D.popleft() if D else -1))
    elif command[0] == 4:
        ans.append(str(D.pop() if D else -1))
    elif command[0] == 5:
        ans.append(str(len(D)))
    elif command[0] == 6:
        ans.append(str(1 if not D else 0))
    elif command[0] == 7:
        ans.append(str(D[0] if D else -1))
    elif command[0] == 8:
        ans.append(str(D[-1] if D else -1))

print("\n".join(ans))