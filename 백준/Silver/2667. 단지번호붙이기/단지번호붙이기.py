import sys
sys.setrecursionlimit(10**6)

def DFS(x, y):
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]

    visited[x][y] = True
    ans[-1] += 1  # 현재 마지막 단지의 집 개수 증가

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and graph[nx][ny]:
                DFS(nx, ny)
    
N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

ans = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            ans.append(0)  # 새로운 단지를 추가
            DFS(i, j)

ans.sort()
print(len(ans))  # 총 단지 수 출력
print('\n'.join(map(str, ans)))  # 각 단지의 집의 수 오름차순 출력