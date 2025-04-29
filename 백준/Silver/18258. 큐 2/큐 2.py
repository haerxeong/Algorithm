import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력
Q = deque()
output = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == "push":
        Q.append(int(command[1]))
    elif command[0] == "pop":
        output.append(str(Q.popleft() if Q else -1))
    elif command[0] == "size":
        output.append(str(len(Q)))
    elif command[0] == "empty":
        output.append("0" if Q else "1")
    elif command[0] == "front":
        output.append(str(Q[0] if Q else -1))
    elif command[0] == "back":
        output.append(str(Q[-1] if Q else -1))

print('\n'.join(output))