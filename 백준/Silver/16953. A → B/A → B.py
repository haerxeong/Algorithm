from collections import deque

A, B = map(int, input().split())

def bfs():
    queue = deque()
    queue.append((A, 1))
    visited = set()
    visited.add(A)

    while queue:
        num, cnt = queue.popleft()
        if num == B:
            return cnt
        for next_num in (num * 2, num * 10 + 1):
            if next_num <= B and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, cnt + 1))
    return -1

print(bfs())