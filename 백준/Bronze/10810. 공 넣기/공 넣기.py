N, M = map(int, input().split())
baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split()) # i번 ~ j번 바구니에 k공 넣기
    
    for l in range(i - 1, j):
        baskets[l] = k

print(' '.join(map(str, baskets)))