from collections import deque

N = int(input())
stones = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1  # 인덱스 0부터 시작
b -= 1

visited = [False] * N

def bfs():
    queue = deque()
    queue.append((a, 0))
    visited[a] = True

    while queue:
        curr, jumps = queue.popleft()
        if curr == b:
            return jumps

        step = stones[curr]

        for i in range(1, N):
            next_pos = curr + step * i
            if next_pos >= N:
                break
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jumps + 1))

        for i in range(1, N):
            next_pos = curr - step * i
            if next_pos < 0:
                break
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jumps + 1))

    return -1

print(bfs())