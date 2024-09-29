N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
ans = [0] * N
for i in range(N):  # 순위 당사자
    rank = 1
    for j in range(N):  # 비교 대상
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            rank += 1
    ans[i] = rank

print(' '.join(map(str, ans)))