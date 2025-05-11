from collections import deque

n = int(input())
A = list(map(int, input().split()))
s = int(input()) - 1  # 인덱스 0부터 시작

visited = [False] * n
queue = deque()
queue.append(s)
visited[s] = True
count = 1

while queue:
    curr = queue.popleft()
    for next_pos in (curr + A[curr], curr - A[curr]):
        if 0 <= next_pos < n and not visited[next_pos]:
            visited[next_pos] = True
            queue.append(next_pos)
            count += 1

print(count)