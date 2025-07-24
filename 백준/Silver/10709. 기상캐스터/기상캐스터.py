H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]
ans = [[-1] * W for _ in range(H)]

for i in range(W):
    for j in range(W - i):
        for k in range(H):
            if sky[k][j] == 'c' and ans[k][j + i] == -1:
                ans[k][j + i] = i

for i in range(H):
    print(*ans[i])