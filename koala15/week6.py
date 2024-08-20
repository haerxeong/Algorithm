#BFS, DFS

#2644번: 촌수 계산
from collections import deque

n = int(input())
target = [input()]
li = [i for i in range(n + 1)]

for _ in range(int(input())):
    li[int(input())].append(int(input()))