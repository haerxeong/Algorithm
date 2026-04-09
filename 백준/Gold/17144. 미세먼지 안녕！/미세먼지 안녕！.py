def dust(x, y):
    cnt = 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if [nx, ny] not in machine:
                new_A[nx][ny] += A[x][y] // 5
                cnt += 1

    new_A[x][y] += A[x][y] - (A[x][y] // 5) * cnt

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
machine = []

# 공기청정기 위치
for i in range(R):
    for j in range(C):
        if A[i][j] == -1: machine.append([i, j])

for _ in range(T):
    # 미세먼지 확산
    new_A = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if A[i][j] > 0: dust(i, j)

    for x, y in machine: new_A[x][y] = -1

    A = new_A

    # 공기청정기
    ## 윗부분
    x, y = machine[0]
    i, j = x - 1, 0

    ### 아래로 이동
    while i > 0:
        A[i][j] = A[i - 1][j]
        i -= 1

    ### 왼쪽으로 이동
    while j < C - 1:
        A[i][j] = A[i][j + 1]
        j += 1

    ### 위로 이동
    while i < x:
        A[i][j] = A[i + 1][j]
        i += 1

    ### 오른쪽으로 이동
    while j > 1:
        A[i][j] = A[i][j - 1]
        j -= 1

    A[i][j] = 0

    ## 아랫부분
    x, y = machine[1]
    i, j = x + 1, 0

    ### 위로 이동
    while i < R - 1:
        A[i][j] = A[i + 1][j]
        i += 1

    ### 왼쪽으로 이동
    while j < C - 1:
        A[i][j] = A[i][j + 1]
        j += 1

    ### 아래로 이동
    while i > x:
        A[i][j] = A[i - 1][j]
        i -= 1

    ### 오른쪽으로 이동
    while j > 1:
        A[i][j] = A[i][j - 1]
        j -= 1

    A[i][j] = 0

ans = 0
for i in range(R):
    for j in range(C):
        if A[i][j] > 0: ans += A[i][j]

print(ans)