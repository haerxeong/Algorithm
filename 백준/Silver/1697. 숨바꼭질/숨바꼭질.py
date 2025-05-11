from collections import deque

N, K = map(int, input().split())
MAX = 100001  # 범위는 0 ~ 100000
visited = [False] * MAX

def bfs():
    queue = deque()
    queue.append((N, 0))
    visited[N] = True

    while queue:
        pos, time = queue.popleft()
        if pos == K:
            return time
        for next_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= next_pos < MAX and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

print(bfs())
