import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = [0] + [int(input()) for _ in range(N)]  # 1-based 인덱스
    visited = [False] * (N + 1)

    cur = 1
    cnt = 0

    while not visited[cur]:
        visited[cur] = True
        cnt += 1
        if A[cur] == N:
            print(cnt)
            break
        cur = A[cur]
    else:
        # while이 중간에 break 없이 종료 → 사이클만 돌고 N에 못 감
        print(0)